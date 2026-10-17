#!/usr/bin/env python3
"""Mechanical checks for the test-cases scenarios (TC-01–TC-22, HO-06, HO-07, HO-13, HO-14–HO-33).

Only what can be checked by text: required exact strings, planted values that
must not appear, clarification markers in the right language, case counts.
A scenario that passes every check still needs a reader for its judgment
items (listed as READ). Prints one line per scenario and run.

Usage: check_test_cases.py <run-dir> [<run-dir> ...]
"""
import os
import re
import sys

MARKER = re.compile(r"\[[A-ZÀ-ÖØ-Þ][A-ZÀ-ÖØ-Þ ]{3,}:")
EN_MARKER = "[TO CLARIFY"


def answers(path):
    t = open(path, encoding="utf-8").read()
    return re.findall(r"### Answer\n\n(.*?)(?=\n## Turn \d|\n## Files written|\Z)", t, re.S), t


def case_count(a):
    """Count case headings, the usual way models write them."""
    heads = re.findall(r"(?m)^#{2,4} .*?\b(?:TC|T|SHOP-\d+-TC|CASE|TF|TS|PC)[- ]?\d+\b", a)
    return len(heads)


def has(*keys):
    return lambda a, t: all(k in a for k in keys)


def lacks(*keys):
    return lambda a, t: not any(k in a for k in keys)


def rx(pattern, flags=re.I):
    return lambda a, t: bool(re.search(pattern, a, flags))


def no_rx(pattern, flags=re.I):
    return lambda a, t: not re.search(pattern, a, flags)


def no_line(pattern, excuse):
    """No line states the pattern, except lines that ask or mark it as open."""
    return lambda a, t: not any(re.search(pattern, l) and not re.search(excuse, l, re.I) for l in a.splitlines())


def has_all(*fns):
    return lambda a, t: all(f(a, t) for f in fns)


def native_marker(a, t):
    return bool(MARKER.search(a)) and EN_MARKER not in a


def any_marker(a, t):
    return bool(MARKER.search(a))


def at_most(n):
    return lambda a, t: case_count(a) <= n


def last_only(pair):
    """Apply a check to the last answer only (for multi-turn scenarios)."""
    name, fn = pair
    wrapped = lambda a, t: fn(a, t)
    wrapped.last = True
    return name, wrapped


CHECKS = {
    "TC-01": [("messages exact", has("Display name must be 1–50 characters",
                                     "Display name contains characters that are not allowed")),
              ("AC4 traced", has("AC4")), ("boundaries 50/51", rx(r"\b51\b")), ("≤15 cases", at_most(15))],
    "TC-02": [("recommends review first", rx(r"review(ing)? (the |this )?requirement|review-requirements|requirements review")),
              ("markers", any_marker), ("not covered", no_rx(r"\|\s*Covered\s*\|"))],
    "TC-03": [("99.99 boundary", has("99.99")), ("threshold basis asked", rx(r"before or after"))],
    "TC-04": [("5 MB", rx(r"5\s?MB")), ("GIF", rx(r"\bgif\b")), ("further ideas", rx(r"further test ideas")),
              ("≤15 cases", at_most(15))],
    "TC-05": [("Swedish marker only", native_marker), ("Givet/När/Så", has("Givet", "När", "Så")),
              ("messages exact", has("Din bokning är avbokad", "Avbokning är inte längre möjlig")),
              ("time zone raised", rx(r"tidszon"))],
    "TC-06": [("IDs", has("SHOP-142-TC-01")), ("P1–P3", rx(r"\bP[123]\b")), ("Given/When/Then", has("Given", "When", "Then")),
              ("title pattern", rx(r"\| .* \|", 0))],
    "TC-07": [("no production data", lacks("jane.doe@realcompany.com", "884213")),
              ("warns about production data", rx(r"production"))],
    "TC-08": [("verdict", rx(r"needs rework|needs minor")), ("dependency flagged", rx(r"TC3.{0,80}TC2|depend")),
              ("duplicate flagged", rx(r"duplicat"))],
    "TC-09": [last_only(("asks which tool", rx(r"which (tool|test management)|what tool|import (it )?into")))],
    "TC-10": [("no manual cases", no_rx(r"(?m)^#{2,4} TC-?\d"))],
    "TC-11": [("identifiers exact", has("CHK-031", "SKU-1001", "SKU-2002", "WINTER25", "'Apply'", "'Place order'",
                                       "ORDERS.VOUCHER_CODE")), ("blocked", rx(r"Blocked")), ("scope", rx(r"Scope OK")),
              ("consistency note", rx(r"consisten|related test"))],
    "TC-12": [("consider split", rx(r"Consider split")), ("statuses exact", has("PAID", "AWAITING_PAYMENT"))],
    "TC-13": [("attachment kept", has("invoice-reference.pdf"))],
    "TC-14": [("SQL exact", has("DELETE FROM user_sessions WHERE last_seen < now() - interval '30 days';")),
              ("<ENV> kept", has("<ENV>")), ("no {{ENV}}", lacks("{{ENV}}")), ("blocked", rx(r"Blocked")),
              ("no invented count", no_rx(r"\b0 rows\b"))],
    "TC-15": [("T6 and T7 listed", has("T6", "T7")), ("asks to continue", rx(r"continue|go on|the rest|remaining"))],
    "TC-16": [("60 minutes", rx(r"60 min")), ("boundary cases", rx(r"\b(59|61)\b"))],
    "TC-17": [("traced to flows", has("UC-12")), ("2a traced", has("2a")),
              ("messages exact", has("Check your email", "Your password has been changed")),
              ("no Given/When/Then", no_rx(r"(?m)^\s*(\*\*)?Given\b", 0))],
    "TC-18": [("design labels exact", has("Display name", "Save changes", "Profile updated"))],
    "TC-19": [("XML exact", has("<Created>2026-01-15T09:30:00Z</Created>", '<Amount currency="EUR">125.50</Amount>',
                                "{{message id}}")), ("names exact", has("PAYMENTS.IN", "PAYMENTS.STATUS", "RECEIVED", "<ENV>"))],
    "TC-20": [("suite title pattern", rx(r"Cart \|", 0)), ("message exact", has("Your cart is empty")),
              ("placeholder", has("{{product}}"))],
    "TC-22": [("standard and express", has_all(rx(r"\b8(\.00)? EUR\b"), rx(r"\b16(\.00)? EUR\b"))),
              ("weight boundary", rx(r"\b20 ?kg\b")), ("combination unknown", any_marker),
              ("no assumed combination", no_line(r"\b(20|24)(\.00)? EUR\b", r"\?|assum|if the|unknown|TO CLARIFY"))],
    "TC-21": [("both tests", has("SHOP-T204", "SHOP-T205")), ("identifiers exact", has("SKU-1001", "WINTER25", "'Remove'"))],
    "HO-06": [("Swedish marker only", native_marker), ("code exact", has("VINTER15")), ("200 kr", rx(r"200 kr")),
              ("time zone or time of day raised", rx(r"tidszon|klockslag|tid på dygnet|vilken tid"))],
    "HO-07": [("ID kept", has("QA-412")), ("password not repeated", lacks("Adm1n-Test-Pass!"))],
    "HO-13": [("IDs", has("SHOP-210-TC-01")), ("P1–P3", rx(r"\bP[123]\b")), ("message exact", has("Din önskelista är full")),
              ("conventions named", rx(r"conventions"))],
    "HO-14": [("codes exact", has("POINTS_OUT_OF_RANGE", "INSUFFICIENT_BALANCE", "remainingPoints")),
              ("boundaries", rx(r"\b(99|5001)\b")), ("step rule unknown", rx(r"\b150\b|multiple of 100|steps? of 100")),
              ("markers", any_marker)],
    "HO-15": [("German marker only", native_marker), ("button exact", has("„Genehmigen“")), ("comment case", rx(r"Kommentar"))],
    "HO-16": [("statuses exact", has("NEW", "PAID", "SHIPPED", "DELIVERED", "CANCELLED")), ("refund", rx(r"refund")),
              ("markers", any_marker)],
    "HO-17": [("untestable as written", rx(r"not (be )?testable|cannot be tested|can't be tested|no measurable|not measurable|needs? measurable")),
              ("no invented thresholds", no_rx(r"under \d+ ?s(ec)?|\b\d+ concurrent|within \d+ ?ms"))],
    "HO-18": [("verdict", rx(r"needs rework|needs minor|ready to use")), ("dependency flagged", rx(r"depend|scenario 1")),
              ("message kept", has("You are already subscribed"))],
    "HO-19": [("Norwegian marker only", native_marker), ("identifiers exact", has("TC-NO-88", "4400-12", "Vipps", "BETALT"))],
    "HO-20": [("traced", has("PAY-2231")), ("double press", rx(r"twice|double")), ("markers", any_marker)],
    "HO-21": [("screen reader", rx(r"screen reader")), ("no WCAG level as required", no_rx(r"WCAG 2\.\d (Level )?AA?\b(?!.{0,40}(not|isn't|does not))", re.I)),
              ("markers", any_marker)],
    "HO-22": [("24 months gap", rx(r"24 months")), ("500/501", rx(r"\b501\b")), ("not covered", rx(r"not covered|partly covered|partially covered"))],
    "HO-23": [("does not run", rx(r"(can(no|')t|do not|don't|does not|doesn't) (run|execute)|not run")),
              ("no pass/fail reported", no_rx(r"\|\s*(Pass|Passed|Fail|Failed)\s*\|"))],
    "HO-24": [("no planted data", lacks("Lars Nilsson", "850709-1234", "lars.nilsson@nordkund.se", "Sommar2024!")),
              ("warns about production data", rx(r"production|real (customer|personal)"))],
    "HO-25": [("recommends clarifying", rx(r"clarif|review(ing)? the requirement|review-requirements")), ("markers", any_marker)],
    "HO-26": [("February", rx(r"-02-2[89]")), ("leap year", rx(r"-02-29")), ("time zone raised", rx(r"time zone|timezone|time of day"))],
    "HO-27": [("Spanish marker only", native_marker), ("messages exact", has("Seleccione importe", "Tarjeta retenida")),
              ("traced", has("CU-04", "3a"))],
    "HO-28": [("≤15 cases", at_most(15)), ("all ACs in coverage", has(*[f"AC{n}" for n in range(1, 11)])),
              ("message exact", has("Please call us"))],
    "HO-29": [("identifiers exact", has("RPT-310", "Reports > Sales", "March 2026")),
              ("both attachments", has("filter-settings.png", "march-totals.xlsx"))],
    "HO-30": [last_only(("updates cases", rx(r"balance"))),
              last_only(("no re-ask of answered points", no_rx(r"\?[^\n]{0,0}.*(balance|shipping).{0,40}\?")))],
    "HO-31": [("conflict case", rx(r"web version|conflict")), ("markers", any_marker)],
    "HO-32": [("positive verdict", rx(r"ready to use|needs minor"))],
    "HO-76": [("10 SEK steps", rx(r"\b(9|11|19|21)(,00)? ?(SEK|kr)|\|\s*(9|11)\s*\|")), ("combination unknown", any_marker),
              ("weekend boundary asked", rx(r"time zone|midnight|weekend (start|begin|end)|which day|Saturday 00")),
              ("no assumed Gold weekend factor", no_line(r"\b(2[.,]5|3)\s?(x|×|times)\b", r"\?|assum|if the|unknown|TO CLARIFY|or\b"))],
    "HO-33": [("age boundaries", has("64", "65", "79", "80")), ("trip boundary", has("30", "31")),
              ("combination unknown", any_marker), ("no assumed combination", no_rx(r"\b(60|50)(\.00)? EUR\b(?!.{0,60}(\?|assum|if the|unknown|TO CLARIFY))"))],
}


def check(run_dir, sid):
    path = f"{run_dir}/{sid}/transcript.md"
    if not os.path.exists(path):
        return None
    ans, raw = answers(path)
    allans, last = "\n".join(ans), (ans[-1] if ans else "")
    fails = []
    for name, fn in CHECKS.get(sid, []):
        a = last if getattr(fn, "last", False) else allans
        if not fn(a, raw):
            fails.append(name)
    return fails, len(CHECKS.get(sid, []))


def main():
    for run_dir in sys.argv[1:]:
        print(f"== {run_dir}")
        for sid in sorted(CHECKS, key=lambda s: (s[:2], int(s[3:]))):
            res = check(run_dir, sid)
            if res is None:
                continue
            fails, n = res
            print(f"{sid}: {n - len(fails)}/{n}" + (f"  missing: {', '.join(fails)}" if fails else ""))


if __name__ == "__main__":
    main()
