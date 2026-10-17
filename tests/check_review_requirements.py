#!/usr/bin/env python3
"""Mechanical checks for the review-requirements scenarios (RR-01–RR-13, HO-04, HO-05, HO-65–HO-75).

Only what can be checked by text: verdicts, required quotes, values that
must not appear, the finding limit, headings in the right language. A
scenario that passes every check still needs a reader for its judgment
items. Prints one line per scenario and run.

Usage: check_review_requirements.py <run-dir> [<run-dir> ...]
"""
import re
import sys

import check_test_cases as base
from check_test_cases import any_marker, has, has_all, lacks, last_only, no_line, no_rx, rx

NEEDS = rx(r"Needs clarification before development")
READY = rx(r"Verdict:?\**:?\s*\**\s*Ready\b")
no_must = ("no Must clarify section", no_rx(r"(?m)^#+\s*Must clarify"))
no_gwt = ("no Given/When/Then", no_rx(r"(?m)^\s*[-*]?\s*\**Given\b", 0))
not_posted = ("nothing claimed posted", no_line(r"\b(I('ve| have) (posted|added|commented)|(has|have) been posted|was posted|posted (it|the (review|comment)))\b",
                                              r"\b(no|not|nothing|cannot|can't|couldn't|never|unable)\b|n't"))


def minor_findings(a, t):
    """At most 7 Should clarify and Consider findings combined."""
    n = 0
    for head in ("Should clarify", "Consider"):
        m = re.search(rf"(?ms)^#+\s*{head}\s*$(.*?)(?=^#+ |\Z)", a)
        if m:
            n += len(re.findall(r"(?m)^\d+\.\s", m.group(1)))
    return n <= 7


CHECKS = {
    "RR-01": [("verdict", NEEDS), ("markers", any_marker), no_gwt,
              ("no invented values", no_line(r"24 hours|12 characters|\b\d+ minutes\b", r"TO CLARIFY|e\.g\.|for example|\?|such as"))],
    "RR-02": [("verdict", READY), no_must],
    "RR-03": [("verdict", rx(r"Verdict"))],
    "RR-04": [("Swedish headings", rx(r"Måste (klargöras|förtydligas)|Bedömning|Behöver")), ("no English headings", lacks("Must clarify", "Should clarify")),
              ("bör flagged", rx(r"\bbör\b")), ("no Givet", no_rx(r"(?m)^\s*[-*]?\s*\**Givet\b", 0))],
    "RR-05": [("German", rx(r"\b(und|die|der|nicht)\b", 0)), ("English keywords", rx(r"\bGiven\b", 0)), ("Kunde", has("Kunde"))],
    "RR-06": [("conflict", rx(r"conflict|contradict")), ("must clarify", rx(r"Must clarify"))],
    "RR-07": [("≤7 minor findings", minor_findings), ("summary line", rx(r"further|more|remaining|other"))],
    "RR-08": [("nothing repeated", lacks("Jane Doe", "jane.doe@example.com", "000 00 00", "FAKE-KEY-1234567890")),
              ("asks to remove", rx(r"remov"))],
    "RR-09": [last_only(not_posted)],
    "RR-10": [("HLR-4 named", has("HLR-4")), ("3 vs 5", rx(r"\b3\b.{0,80}\b5\b|\b5\b.{0,80}\b3\b")), ("email missing", rx(r"email|notif"))],
    "RR-11": [("PDF gap", rx(r"PDF"))],
    "RR-12": [("4a proposed", rx(r"\b4a\b")), no_gwt],
    "RR-13": [("Swedish headings", rx(r"Måste (klargöras|förtydligas)|Bedömning|Behöver")), ("quote untranslated", has("Codes should expire"))],
    "HO-04": [("limits", has("3", "5")), ("right away quoted", rx(r"right away"))],
    "HO-05": [("verdict", READY), ("≤7 minor findings", minor_findings), no_must],
    "HO-65": [("Swedish headings", rx(r"Måste (klargöras|förtydligas)|Bedömning|Behöver")), ("no English marker", lacks("[TO CLARIFY")),
              ("no decided numbers", no_line(r"\b\d+\s?(ms|sekunder|sek\b|s\b|användare)", r"ATT KLARGÖRA|exempel|t\.ex\.|\?|förslag"))],
    "HO-66": [("verdict", READY), no_must],
    "HO-67": [("all rows", has("WISH-1", "WISH-2", "WISH-3", "WISH-4")), ("101st", rx(r"\b101\b|full|limit"))],
    "HO-68": [("refund", rx(r"refund")), ("restart", rx(r"restart|resubscri|reactivat|rejoin|renew")), ("data", rx(r"data|profile"))],
    "HO-69": [("nothing repeated", lacks("Sv7!recon2026", "0583 9825 7466", "05839825", "User=recon")), ("asks to remove", rx(r"remov"))],
    "HO-70": [("glossary named", rx(r"glossary")), ("12 months", rx(r"12 months")), ("anonymized", rx(r"anonymi"))],
    "HO-71": [("French", rx(r"\b(le|la|les|une|est)\b", 0)), ("devrait", has("devrait")), ("no English headings", lacks("Must clarify"))],
    "HO-72": [last_only(not_posted), last_only(("says it cannot", rx(r"can(no|')t|unable|not able|no (GitHub|access|integration)|don't have")))],
    "HO-73": [("must clarify", rx(r"Must clarify")), ("Given/When/Then proposals", rx(r"(?m)^\s*[-*]?\s*\**Given\b", 0))],
    "HO-74": [("no decided standard", no_line(r"WCAG 2\.\d\s?(Level\s)?AA?\b", r"TO CLARIFY|propos|example|e\.g\.|\?|whether|which|such as"))],
    "HO-75": [("exactly 500", rx(r"exactly 500|500 kr exactly|= ?500|of 500 kr\b")), ("discounts", rx(r"discount|before or after"))],
}


def main():
    base.CHECKS = CHECKS
    for run_dir in sys.argv[1:]:
        print(f"== {run_dir}")
        for sid in sorted(CHECKS, key=lambda s: (s[:2], int(s[3:]))):
            res = base.check(run_dir, sid)
            if res is None:
                continue
            fails, n = res
            print(f"{sid}: {n - len(fails)}/{n}" + (f"  missing: {', '.join(fails)}" if fails else ""))


if __name__ == "__main__":
    main()
