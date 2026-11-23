# Project notes: CS 4371 Group Project 5

Quick reference for this repo. The course files (slides, rubric, templates) are on Canvas only and are not kept in this repo.

## Course

- CS 4371 Computer System Security, Fall 2026, Texas State. Instructor: Heena Rathore. Class: Mon/Wed 12:30–1:50 PM, DERR 234.
- Canvas course: https://canvas.txstate.edu/courses/2742404 (files are in Modules → "Group Project")

## Paper (picked Oct 5, 2026)

**Security Attacks on LLM-based Code Completion Tools**. Wen Cheng, Ke Sun, Xinyu Zhang, Wei Wang. AAAI 2025, vol. 39 no. 22, pp. 23669–23677. DOI 10.1609/aaai.v39i22.34537. arXiv 2408.11006. Authors' code: https://github.com/sensente/security-attacks-on-lccts

- The team first picked CAN-MIRGU, then talked about IoT-AD (paper #4), and settled on this LLM paper on Oct 5. The repo was renamed from CS4371-CAN-MIRGU to CS4371-LLM-Code-Completion-Attacks.
- The authors' repo says their code is for research only and that they held back their automation scripts.

## Team and roles

| Role | Member | GitHub |
|------|--------|--------|
| Reviewer | Mustafa Hassan | invited by school email (pending) |
| Student Researcher | Adan Torres | Adantorres11 (pending) |
| Reproducibility Checker | Daniel Delgado | invited by school email (pending) |
| Archaeologist | Bigyan Dhakal | Bigyan1313 (repo owner) |
| Quanta Correspondent | Bruce C Ngere | BruceNgere (pending) |

Bruce said he'll lead the final presentation. Per the instructor, everyone has to speak, each about their own part.

## Due dates (Canvas is the source of truth)

| What | Due | Points |
|------|-----|--------|
| Project Proposal (one upload for the whole group) | Mon Oct 5, 2026, 11:59 PM | 20 |
| Quanta Correspondent (stand-up slides, max 2 slides) | Wed Oct 7, 2026, 11:59 PM | 5 on Canvas |
| Midway stand-up + blind AI-article vote | Nov 3, 2026 | |
| Project Code | Nov 24, 2026 | 25 |
| Demo + final presentations | Weeks 14–15 | 25 (rubric) / 30 (slides) |
| Team Participation (peer form) | End of semester | 20 |

Mismatches between files: the rubric PDF says the proposal is due Oct 13 and Quanta is worth 10 points, but Canvas says Oct 5 and 5 points. The slides say Demo is 30 points and the rubric says 25. Go by Canvas, and ask the instructor if it matters.

## What each role does

- **Reviewer** (proposal Task 1, 10 pts): write your own summary and key takeaways first (7 pts). Then compare against the instructor's AI-generated review in the AI Review Disagreement Table, with at least 3 points labeled right / shallow / wrong / fabricated plus evidence from the paper (3 pts).
- **Student Researcher** (proposal Task 2, 5 pts): pick the topic to dig into, explain why, how it ties to class, and where it applies. AI Idea Appendix: 3 AI ideas, each labeled feasible / already published / technically flawed, with one sentence each. Say whether the chosen topic came from the team or the AI.
- **Reproducibility Checker** (proposal Task 3, 5 pts): pick the idea to build for the demo and how. Name the AI coding assistant and how its output will be checked. Small experiment to check the paper's claims, including different hyperparameters. Log every AI coding mistake.
- **Archaeologist** (graded in the Project Code README, part of the 25 pts): at least one **older** paper cited by this paper that strongly shaped it, and at least one **newer** paper that cites it. Look for follow-up work that criticizes it. AI can help find them, but you must check by hand that both papers exist and that the citation link is real. Log any fake or misattributed reference in AI_AUDIT.md (category FC).
- **Quanta Correspondent**: plain-language article and stand-up talk on the problem, why it matters, the main contributions, impact on society, progress so far, and one graphic. The class compares it with an AI-written article in a blind vote on Nov 3.

## Proposal tasks 4–6 (Demo)

- Task 4 (10 pts): working code from Task 3, shown with results.
- Task 5 (10 pts): detailed write-up of the Task 2 topic: what we learned, the tie to class, and where it applies.
- Task 6 (5 pts): what didn't go well, lessons learned, and the 2 biggest AI failures from AI_AUDIT.md and how the team caught them.

## Project Code (due Nov 24)

- 10 pts: clean, commented, formatted code.
- 10 pts: the README explains how to clone, build and run, what works and what doesn't, and has the Archaeologist's 2 papers (older + newer).
- 5 pts: any data needed for the demo is in the repo, the instructor can rerun the results, and AI_AUDIT.md is complete for all roles.

## AI policy

- AI use is required. Every AI output the team relies on (a repeated claim, a citation, committed code, an adopted idea) gets one row in `AI_AUDIT.md`. Throwaway drafts don't need logging.
- Categories: FC fabricated citation, NA nonexistent API, MR misstated result, CW code runs but is wrong, OC overclaim, OK verified.
- Unchecked AI content presented as your own work is graded as wrong. The peer form asks whether each member checked AI output (2.5 of 20 pts).

## Open items (as of Oct 5, 2026)

- The instructor's AI-generated review of our paper (needed for Reviewer Task 1) was not found on Canvas yet.
- Archaeologist papers (older + newer) are not picked yet.
- GitHub invites for Mustafa, Adan, Daniel and Bruce are pending.
- The team proposal doc is a Google Doc Adan shared: "CS 4371 Project Proposal_Fall2026", https://docs.google.com/document/d/1gVUbWT66bIGNAsDLQDGIxsPKjim9I3yc-lZACu95fhk/edit
- Proposal status at 5:40 PM, Oct 5: Task 2 (Adan) is filled in. Paper title, group members, Task 1 (Mustafa) and Task 3 (Daniel) are still empty.
