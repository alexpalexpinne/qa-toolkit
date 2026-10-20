#!/usr/bin/env python3
"""Mechanical checks for the bug-report scenarios (BR-01–BR-15, BR-21–BR-26, HO-01–HO-03, HO-34–HO-49).

Only what can be checked by text: required exact strings, values that must
not appear, markers in the right language, files written. A scenario that
passes every check still needs a reader for its judgment items. Prints one
line per scenario and run.

Usage: check_bug_report.py <run-dir> [<run-dir> ...]
"""
import re
import sys

import check_test_cases as base
from check_test_cases import any_marker, has, lacks, last_only, native_marker, no_line, no_rx, rx

EN = "[TO CLARIFY"
no_files = ("no files written", lambda a, t: "## Files written or changed during the run\n\nNone." in t)
no_en_marker = ("no English marker", lacks(EN))
not_filed = ("no filing claimed", no_rx(r"\b(I('ve| have) (filed|created|opened|submitted)|has been (filed|created|submitted)|issue #\d+)"))
DEFAULT_SCALE = r"(Severity|Allvarlighetsgrad|Schweregrad)\W{0,6}(Critical|High|Medium|Low)\b"

CHECKS = {
    "BR-01": [("concrete crash question", rx(r"clos|froze|freez|error message")),
              ("no invented version", no_rx(r"\bversion\s*:?\s*\**\s*v?\d+\.\d+"))],
    "BR-02": [("values exact", has("SPRING10", "50.00 EUR", "45.00 EUR")), ("3 of 3", rx(r"3 of 3|3/3|(all|every) (three|3)|three (times|attempts)")),
              ("no N/A", lacks("N/A"))],
    "BR-03": [("gift card", rx(r"gift card")), ("blurry logo", rx(r"logo")), ("slow login", rx(r"login"))],
    "BR-04": [("no secrets", lacks("jane.doe@example.com", "abc123def456", "NotARealPassw0rd!")),
              ("useful parts kept", has("/api/export")), ("timeout kept", rx(r"30000 ms|timeout"))],
    "BR-05": [("error exact", has("Payment declined: code 402")), no_en_marker],
    "BR-06": [("time zone", rx(r"time zone|timezone")), ("AM/PM asked", rx(r"03:00|15:00|\bAM\b|\bPM\b|a\.m\.|p\.m\.|morning|afternoon"))],
    "BR-07": [("verdict", rx(r"needs more information")), ("hypothesis", rx(r"hypothes"))],
    "BR-08": [("dates", has("2028-02-29", "2028-03-01")), ("build", has("2.4.0"))],
    "BR-09": [("error untranslated", has("Fehler 500")), ("S1–S4", rx(r"\bS[1-4]\b")), ("Admin", has("Admin")),
              ("no default scale", no_rx(DEFAULT_SCALE))],
    "BR-10": [last_only(("screenshot named", has("checkout.png"))), last_only(not_filed)],
    "BR-11": [("asks version or device", rx(r"version|device|phone"))],
    "BR-12": [("draft with unknowns", rx(r"Open questions|TO CLARIFY|Unknown"))],
    "BR-13": [("skill not loaded", lambda a, t: "bug-report/SKILL.md" not in t), ("no report", lacks("Steps to reproduce"))],
    "BR-14": [no_files, ("report written", rx(r"Steps to reproduce"))],
    "BR-15": [("path named", has(".qa-toolkit/conventions.md")), no_files],
    "BR-21": [("email kept", has("anna.berg@example.com")), ("credentials masked", lacks("zz9988xy", "NotARealPassw0rd!"))],
    "BR-22": [("all kept", has("jane.doe@example.com", "FAKE-TOKEN-abc123def456", "NotARealPassw0rd!")), no_files],
    "BR-23": [("all masked", lacks("jane.doe@example.com", "abc123def456", "NotARealPassw0rd!"))],
    "BR-24": [("all masked", lacks("jane.doe@example.com", "abc123def456", "NotARealPassw0rd!")),
              ("team rule named", rx(r"team|conventions"))],
    "BR-25": [("email masked", lacks("li.wang@example.net")), ("team rule named", rx(r"team|conventions")), ("message exact", has("Download failed"))],
    "BR-27": [("nothing repeated", lacks("Anders Holm", "731045")), ("team rule named", rx(r"(?i)team|konvention|conventions|regel"))],
    "BR-26": [("Dutch marker only", native_marker), ("message exact", has("Verlenging mislukt")),
              ("Dutch report", rx(r"Stappen|Verwacht|Werkelijk|Samenvatting"))],
    "HO-01": [("message exact", has("Vorgang abgebrochen")), ("screenshot asked", rx(r"Screenshot")), no_en_marker],
    "HO-02": [("no secrets", lacks("7781aa", "55k2q", "maria.lund@example.net")), ("exception kept", has("authCode", "500")),
              not_filed],
    "HO-03": [("prices exact", has("899 kr", "1 199 kr")), ("hypothesis", rx(r"hypothes"))],
    "HO-34": [("French marker only", native_marker), ("French report", rx(r"Étapes|Résultat"))],
    "HO-35": [("label exact", has("Download receipt")), ("no calendar date", no_rx(r"\b20\d\d-\d\d-\d\d\b")),
              ("no all users / ratio", no_rx(r"\ball users\b|\b2 of 2\b|\b2/2\b"))],
    "HO-36": [("subject exact", has("Your booking â€“ confirmed")), ("seats", has("42", "24"))],
    "HO-37": [("values", has("14,96", "14,97", "5.3.0")), ("Spanish report", rx(r"Pasos|Resultado")), no_en_marker],
    "HO-38": [("positive verdict", rx(r"ready to submit|needs minor")), ("not needs more info", no_rx(r"needs more information"))],
    "HO-39": [("no secrets", lacks("qa.lead@example.com", "Winter2026!", "7700 900123", "7700900123"))],
    "HO-40": [("kept", has("88-31907", "+46 70 123 45 67")), ("key masked", lacks("q81mz"))],
    "HO-41": [("masked", lacks("k77u2p", "lea.martin@example.org")), ("request kept", has("401", "/v2/sync")),
              ("team rule named", rx(r"team|conventions"))],
    "HO-42": [("values exact", has("Completed", "0 bytes")),
              ("no resolved date", no_line(r"\b20\d\d-0[34]-0[34]\b", r"\?|\bor\b|unclear|ambigu|TO CLARIFY"))],
    "HO-43": [("no jargon", no_line(r"\b(build|logs?|firmware)\b", r"\(|means|which is|that is"))],
    "HO-44": [("files named", has("before.png", "after.png")), not_filed, ("values", has("120.00", "12.00", "1.9.4"))],
    "HO-45": [("status exact", has("Cancelled")), ("intent asked", rx(r"intend|on purpose|deliberate"))],
    "HO-46": [("labels exact", has("Add to basket", "Læg i kurv")), ("fields", has("Customer impact", "Found in sprint")),
              ("team scale", rx(r"Blocker|Major|Minor|Trivial")), ("no default scale", no_rx(DEFAULT_SCALE))],
    "HO-47": [("message exact", has("Unsupported file type")), ("no # headings", no_rx(r"(?m)^\s*#{1,6} "))],
    "HO-48": [last_only(("no version", no_rx(r"\bversion\W{0,6}v?\d+(\.\d+)+"))),
              last_only(("no plain Always", no_line(r"\b(Always|Every time)\b", r"\(|unconfirmed|believ|probabl|reported|says|according|TO CLARIFY|\?")))],
    "HO-77": [("nothing repeated", lacks("123 45 67", "1234567", "maria.k@example.se")), ("team rule named", rx(r"team|konvention|regel")),
              ("Swedish", rx(r"\b(och|att|för|inte)\b", 0))],
    "HO-79": [("nothing repeated", lacks("Jonas Becker", "448812")), ("team rule named", rx(r"Team|Konvention|Regel")),
              ("German", rx(r"\b(und|der|die|nicht)\b", 0))],
    "HO-49": [("message exact", has("Coupon not valid for this cart", "KESÄ15")), no_en_marker,
              ("Finnish report", rx(r"Vaiheet|Odotettu|Toteutunut|Havaittu"))],
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
