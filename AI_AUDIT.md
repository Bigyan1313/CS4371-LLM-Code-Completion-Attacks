# AI_AUDIT — Team AI Verification Log

**CS 4371, Fall 2026**

**Team name / number:** Group Project 5

**Team members:** Daniel Delgado, Bigyan Dhakal, Mustafa Hassan, Bruce C Ngere, Adan Torres

**Paper:** Security Attacks on LLM-based Code Completion Tools (Cheng, Sun, Zhang, Wang; AAAI 2025). Switched from CAN-MIRGU on Oct 5, 2026.

**AI assistant(s) used (name and version, e.g., "ChatGPT (GPT-5), Claude (Sonnet 5)"):** Claude (Anthropic). Add each tool and version the team uses.

## How to use this log

AI use in this project is required, not banned. Every AI output your team relies on (a claim you repeat, a citation you include, code you commit, an idea you adopt) must appear here as one row, whether or not it turned out to be correct. You do not need to log throwaway drafts or outputs you discarded without using.

One log per team, kept in the root of your GitHub repository and updated as you work, not reconstructed at the end. Commit history should show it growing over the semester. The completeness and honesty of this log is graded under Project Code; catching an AI error earns credit, hiding one costs it.

## Categories

| Code | Category |
|------|----------|
| FC | Fabricated citation (paper, author, or venue that does not exist or does not say what was claimed) |
| NA | Nonexistent API or function (library, method, flag, or parameter that does not exist) |
| MR | Misstated result (real source, but the number, finding, or claim is wrong) |
| CW | Code runs but is wrong (executes without error, output is incorrect) |
| OC | Overclaim (true in a narrow case, stated as general) |
| OK | Verified correct (the output survived verification) |

## Log

*Role is one of: Reviewer, Archaeologist, Student Researcher, Reproducibility Checker, Quanta Correspondent. Add rows as needed.*

| # | Date | Role | What the AI claimed or produced (short quote or summary) | Category | Verified? (yes / no / partially) | How you checked it (source, test, experiment) | Team member |
|---|------|------|-----------------------------------------------------------|----------|----------------------------------|-----------------------------------------------|-------------|
| 1 | 2026-10-05 | Archaeologist | Claude drafted the README: paper citation (authors, AAAI vol. 39 no. 22, pp. 23669–23677), summary, and setup notes from the authors' repo | OK | yes | Checked the citation against the AAAI page (doi.org/10.1609/aaai.v39i22.34537) and the setup notes against the authors' GitHub README | Bigyan Dhakal |
| 2 | 2026-11-27 | Archaeologist | Prompt to Claude (with web search): find one older paper that Cheng et al. cite and that shaped their work, and one newer paper that cites them, and say where each citation appears. Claude's older pick: Carlini et al., "Extracting Training Data from Large Language Models" (USENIX Security 2021), cited in Cheng et al.'s introduction and Section 2.3 | OK | yes | Opened the Cheng et al. PDF (arXiv 2408.11006), searched for "Carlini", and found it in the introduction, Section 2.3 and the reference list | Bigyan Dhakal |
| 3 | 2026-11-27 | Archaeologist | Same prompt. Claude's newer pick: Grigorenko et al., "Protecting Private Code in IDE Autocomplete using Differential Privacy" (IDE '26 workshop, ACM, 2026; arXiv 2601.22935), which cites Cheng et al. as reference [13] in its introduction | OK | yes | Opened the paper's PDF on arXiv, searched for "Cheng", and found Cheng et al. as reference [13], cited in the introduction | Bigyan Dhakal |
| 4 | 2026-11-27 | Reproducibility Checker | Claude wrote the model setup code: `src/model_client.py` (sends requests to the local Qwen2.5-Coder model through Ollama) and `src/check_setup.py` (checks Python, that Ollama is running, that the 3 models are downloaded, and that the main model answers a test request) | OK | yes | Ran `python3 src/check_setup.py` on a MacBook Air (M4) with Ollama and all 3 models installed. Every line said OK, and qwen2.5-coder:1.5b wrote a correct `add` function in 1.71 seconds. Claude had also tested it against a fake Ollama server for the error cases (Ollama not running, main model missing) | Bigyan Dhakal |
| 5 | | | | | | | |
| 6 | | | | | | | |
| 7 | | | | | | | |
| 8 | | | | | | | |
| 9 | | | | | | | |
| 10 | | | | | | | |

## End-of-semester summary (fill in before the final demo)

**Total AI outputs logged:** ______    **Verified correct:** ______    **Failed verification:** ______

**The two most consequential AI failures (present these in Task 6, lessons learned):**

**Failure 1:**

**Failure 2:**

**Which verification habit saved your team the most time?**
