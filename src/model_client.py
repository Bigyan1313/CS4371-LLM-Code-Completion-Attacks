"""Small client for talking to a local Ollama server.

Ollama runs the AI model on your own computer. This file is the only
place in the project that sends requests to it, so the filters and the
experiment never need to know how the HTTP calls work.

Uses only the Python standard library, so there is nothing to pip install.
"""

import json
import os
import time
import urllib.error
import urllib.request

# Ollama listens on this address by default. Set OLLAMA_URL to change it.
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434").rstrip("/")

# Main model for the demo, plus the sizes we compare in the experiment.
MAIN_MODEL = "qwen2.5-coder:1.5b"
SIZE_MODELS = ["qwen2.5-coder:0.5b", "qwen2.5-coder:1.5b", "qwen2.5-coder:3b"]


class OllamaError(RuntimeError):
    """Raised when Ollama can't be reached or sends back an error."""


def _request(path, payload=None, timeout=300):
    """Send a request to Ollama and return its JSON reply as a dict.

    With no payload this is a GET request; with a payload it is a POST.
    The long timeout is because the first request loads the model into
    memory, which can take a while on a laptop.
    """
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(OLLAMA_URL + path, data=data, headers=headers)

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        body = err.read().decode("utf-8", errors="replace")
        raise OllamaError(f"Ollama returned HTTP {err.code}: {body}") from err
    except urllib.error.URLError as err:
        raise OllamaError(
            f"Can't reach Ollama at {OLLAMA_URL}. Is the Ollama app running?"
        ) from err


def list_models():
    """Return the names of the models downloaded in Ollama, e.g. 'qwen2.5-coder:1.5b'."""
    reply = _request("/api/tags")
    return [model["name"] for model in reply.get("models", [])]


def generate(prompt, model=MAIN_MODEL, system=None, temperature=0.0, seed=42, max_tokens=256):
    """Send `prompt` to the model and return its answer.

    temperature: 0 means the model always picks its most likely next word,
                 so runs are repeatable. Higher values make it more random.
                 The experiment changes this to see if it affects attacks.
    seed:        fixed so the same settings give the same answer every run.
    max_tokens:  upper limit on how long the answer can be.

    Returns a dict: {"text": the model's answer, "seconds": how long it took}.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,  # wait for the whole answer instead of word by word
        "options": {
            "temperature": temperature,
            "seed": seed,
            "num_predict": max_tokens,
        },
    }
    if system is not None:
        payload["system"] = system

    start = time.perf_counter()
    reply = _request("/api/generate", payload)
    return {
        "text": reply.get("response", ""),
        "seconds": round(time.perf_counter() - start, 2),
    }
