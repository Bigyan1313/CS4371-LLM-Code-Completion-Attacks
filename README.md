# CS 4371 Group Project 5: Security Attacks on LLM-based Code Completion Tools

CS 4371 Computer System Security, Fall 2026, Texas State University. Instructor: Heena Rathore

> **Topic change (Oct 5, 2026):** The team first picked CAN-MIRGU (CAN bus attack dataset). We switched to the paper below and renamed this repo from CS4371-CAN-MIRGU.

## Paper

**Security Attacks on LLM-based Code Completion Tools**
Wen Cheng, Ke Sun, Xinyu Zhang, Wei Wang. *Proceedings of the AAAI Conference on Artificial Intelligence*, 39(22), 23669–23677, 2025.

- AAAI page: https://ojs.aaai.org/index.php/AAAI/article/view/34537
- DOI: https://doi.org/10.1609/aaai.v39i22.34537
- arXiv: https://arxiv.org/abs/2408.11006
- Authors' code: https://github.com/sensente/security-attacks-on-lccts

**In short:** The paper shows that code completion tools such as GitHub Copilot and Amazon Q can be tricked. It tests two kinds of attacks: jailbreaking (getting the tool to answer harmful questions by hiding them inside code) and training data extraction (getting the tool to leak private info such as emails and addresses). The authors report a 99.4% jailbreak success rate on GitHub Copilot.

```bibtex
@inproceedings{cheng2025security,
  title     = {Security Attacks on LLM-based Code Completion Tools},
  author    = {Cheng, Wen and Sun, Ke and Zhang, Xinyu and Wang, Wei},
  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
  volume    = {39},
  number    = {22},
  pages     = {23669--23677},
  year      = {2025}
}
```

## Team and roles

| Role | Member | Main job |
|------|--------|----------|
| Reviewer | Mustafa Hassan | Proposal Task 1: own summary of the paper + AI Review Disagreement Table |
| Student Researcher | Adan Torres | Proposal Task 2: topic we will dig into + AI Idea Appendix (3 AI ideas, labeled) |
| Reproducibility Checker | Daniel Delgado | Proposal Task 3: idea we will build + small experiment to check the paper's claims. Logs every AI coding mistake |
| Archaeologist | Bigyan Dhakal | One older paper this paper builds on + one newer paper that cites it (see below). Keeps this repo and AI_AUDIT.md set up |
| Quanta Correspondent | Bruce C Ngere | Plain-language article on the paper + 5-minute stand-up talk. Leads the final presentation |

Everyone speaks in the final presentation.

## Due dates (from Canvas)

| What | Due |
|------|-----|
| Project Proposal (one upload for the whole group) | Mon Oct 5, 2026, 11:59 PM |
| Quanta Correspondent | Wed Oct 7, 2026, 11:59 PM |
| Midway stand-up + blind AI-article vote | Nov 3, 2026 |
| Project Code (this repo, README, AI_AUDIT.md) | Nov 24, 2026 |
| Demo + final presentations | Weeks 14–15 |

## What is in this repo

| Path | What it is |
|------|------------|
| `README.md` | This file: paper, team, how to run, what works, background papers |
| `AI_AUDIT.md` | Team log of every AI output we used and how we checked it (graded under Project Code) |
| `course-files/` | Project files from Canvas (slides, rubric, proposal template, AI_AUDIT template, Quanta template) + text copies |
| `CLAUDE.md` | Quick project notes: roles, due dates, grading, open items |

More folders (code, data, docs) will be added once the team picks the idea for Task 3.

## How to clone and run

```bash
git clone https://github.com/Bigyan1313/CS4371-LLM-Code-Completion-Attacks.git
cd CS4371-LLM-Code-Completion-Attacks
```

*Build and run steps will be filled in once our Task 3 code exists.*

Notes from the authors' repo, for reproducing their setup:
- The attacks on code completion tools need VS Code with the GitHub Copilot and/or Amazon Q extensions installed by hand.
- The tests on general LLMs (GPT models) need an API key and `pip install -r requirements.txt` from the authors' repo.
- The authors did not release their automation scripts. They suggest building your own with PyAutoGUI.

**Responsible use:** The authors' code is for research only. We only test on our own accounts and test data, and we do not use or share any real personal data a tool might leak.

## What works / what doesn't

| Part | Status |
|------|--------|
| Repo + AI_AUDIT.md set up | Done |
| Task 3 code | Not started |

*Update this table before the final version so it is clear what works and what doesn't.*

## Background papers (Archaeologist)

The rubric asks for two scholarly papers here: one older paper that the current paper builds on, and one newer paper that cites the current paper and builds on it. Each one must be checked by hand: the paper exists, and the citation link is real. Any fake or wrong reference an AI gave us goes in `AI_AUDIT.md`.

**Prior work (older paper cited by Cheng et al. 2025):**
*To be added.* Checked that it exists: ☐  Checked that Cheng et al. cite it: ☐

**Follow-up work (newer paper that cites Cheng et al. 2025):**
*To be added.* Checked that it exists: ☐  Checked that it cites Cheng et al.: ☐

## AI use

AI use is required in this project. Every AI output we rely on is logged and checked in [AI_AUDIT.md](AI_AUDIT.md).
