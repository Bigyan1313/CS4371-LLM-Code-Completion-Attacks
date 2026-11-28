"""Check that this computer is ready to run the demo.

Run it from the repo folder:
    python src/check_setup.py      (Windows)
    python3 src/check_setup.py     (Mac / Linux)

It checks three things, in order:
  1. Python is new enough.
  2. Ollama is running and reachable.
  3. The models are downloaded, and the main model can answer one
     simple, normal coding request.
"""

import sys

import model_client

MIN_PYTHON = (3, 9)

# A normal, harmless coding request, just to prove the model answers.
TEST_PROMPT = "Finish this Python function. Reply with code only.\n\ndef add(a, b):\n"


def main():
    # 1. Python version
    version = sys.version.split()[0]
    if sys.version_info < MIN_PYTHON:
        print(f"FAIL  Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or newer is needed, found {version}")
        return 1
    print(f"OK    Python {version}")

    # 2. Ollama is running
    try:
        installed = model_client.list_models()
    except model_client.OllamaError as err:
        print(f"FAIL  {err}")
        return 1
    print(f"OK    Ollama is running at {model_client.OLLAMA_URL}")

    # 3a. Models are downloaded. The main model is required now; the
    #     other sizes are only needed later for the model-size test.
    for name in model_client.SIZE_MODELS:
        if name in installed:
            print(f"OK    Model {name} is downloaded")
        elif name == model_client.MAIN_MODEL:
            print(f"FAIL  Main model {name} is missing. Run:  ollama pull {name}")
            return 1
        else:
            print(f"WARN  Model {name} is missing (needed for the size test). Run:  ollama pull {name}")

    # 3b. The main model answers a normal request
    print(f"...   Asking {model_client.MAIN_MODEL} a test question (the first run can take a minute)")
    try:
        result = model_client.generate(TEST_PROMPT)
    except model_client.OllamaError as err:
        print(f"FAIL  {err}")
        return 1
    answer = result["text"].strip()
    if not answer:
        print("FAIL  The model sent back an empty answer")
        return 1
    print(f"OK    The model answered in {result['seconds']} seconds:\n")
    print(answer)
    print("\nAll set. This computer is ready for the demo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
