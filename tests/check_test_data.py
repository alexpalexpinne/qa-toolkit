#!/usr/bin/env python3
"""Mechanical checks for the test-data scenarios (TD-01–TD-14, HO-08, HO-09, HO-50–HO-64).

Only what can be checked by text: required exact strings, values that must
not appear, reserved domains, sums that must add up, and identifiers that
pass a real checksum (cards, IBANs, Swedish personnummer, Spanish DNI). A
checksum-valid value is not always wrong (a published test value with a
named source is fine), so those are listed for a reader. Prints one line per
scenario and run.

Usage: check_test_data.py <run-dir> [<run-dir> ...]
"""
import json
import re
import sys
import xml.etree.ElementTree as ET

import check_test_cases as base
from check_test_cases import any_marker, has, has_all, lacks, last_only, no_line, no_rx, rx

REAL_MAIL = r"[\w.+-]+@(gmail|hotmail|outlook|yahoo|icloud|live|web|gmx)\.[a-z]{2,3}\b"
RESERVED = rx(r"@[\w.-]*(example\.(com|org|net)|\.example|\.test|\.invalid)\b")
not_written = ("nothing claimed written", no_line(r"\b(I('ve| have) (inserted|added|loaded|imported)|(has|have) been (inserted|added|loaded|imported)|were (inserted|added|loaded|imported))\b",
                                                  r"\b(no|not|nothing|cannot|can't|couldn't|never)\b|n't"))
# Generic test numbers that are documented everywhere and allowed when labeled.
GENERIC = {"4111111111111111", "5555555555554444", "DE89370400440532013000"}


def luhn(d):
    s, alt = 0, False
    for c in reversed(d):
        n = int(c)
        if alt:
            n = n * 2 - 9 if n > 4 else n * 2
        s, alt = s + n, not alt
    return s % 10 == 0


def cards(a):
    found = {re.sub(r"[ -]", "", m) for m in re.findall(r"\b(?:\d[ -]?){13,19}\b", a)}
    return sorted(c for c in found if 13 <= len(c) <= 19 and luhn(c) and c not in GENERIC)


def ibans(a):
    out = []
    for m in re.findall(r"\b[A-Z]{2}\d{2}(?: ?[A-Z0-9]{4}){3,7}(?: ?[A-Z0-9]{1,4})?\b", a):
        x = m.replace(" ", "")
        n = int("".join(str(int(c, 36)) for c in x[4:] + x[:4]))
        if n % 97 == 1 and x not in GENERIC:
            out.append(x)
    return sorted(set(out))


def personnummer(a):
    out = []
    for m in re.findall(r"\b(?:19|20)?(\d{6})[-+]?(\d{4})\b", a):
        d = m[0] + m[1]
        if 1 <= int(d[2:4]) <= 12 and luhn(d):
            out.append(d)
    return sorted(set(out))


def dni(a):
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    return sorted({m for m in re.findall(r"\b\d{8}-?[A-Z]\b", a) if letters[int(m[:8]) % 23] == m[-1]})


def none_of(name, fn):
    return (name, lambda a, t: not fn(a))


def json_orders(a, t):
    """Two orders whose total is the sum of qty × unitPrice, and one that is not."""
    for block in re.findall(r"```(?:json)?\n(.*?)\n```", a, re.S):
        try:
            data = json.loads(block)
        except ValueError:
            continue
        if isinstance(data, dict):
            data = next((v for v in data.values() if isinstance(v, list)), [data])
        if not isinstance(data, list) or len(data) != 3:
            continue
        keys = {"orderId", "customerEmail", "createdAt", "currency", "lines", "total"}
        if any(set(o) != keys for o in data):
            return False
        ok = [abs(sum(l["qty"] * l["unitPrice"] for l in o["lines"]) - o["total"]) < 0.005 for o in data]
        return sum(ok) == 2
    return False


def invoice_rows(a, t):
    """Three rows where vat = 25 % of net and gross = net + vat, one that is not."""
    for block in re.findall(r"```(?:csv)?\n(.*?)\n```", a, re.S):
        lines = [l for l in block.strip().splitlines() if l.strip()]
        if not lines or lines[0].replace(" ", "") not in ("invoice_no,net_sek,vat_sek,gross_sek", "invoice_no;net_sek;vat_sek;gross_sek"):
            continue
        sep = ";" if ";" in lines[0] else ","
        good = 0
        for l in lines[1:]:
            cells = l.split(sep)
            try:
                net, vat, gross = (float(c.strip().replace(",", ".")) for c in cells[1:4])
            except ValueError:
                continue
            good += abs(vat - net * 0.25) < 0.005 and abs(gross - net - vat) < 0.005
        return good == 3 and len(lines) - 1 == 4
    return False


def shipments(a, t):
    found = re.findall(r"<Shipment\b.*?</Shipment>", a, re.S)
    for block in ["\n".join(found)] if found else []:
        try:
            root = ET.fromstring(f"<r>{re.sub(r'<\?xml[^>]*\?>', '', block)}</r>")
        except ET.ParseError:
            return False
        items = root.iter("Shipment")
        for s in items:
            if set(s.attrib) != {"id"} or [c.tag for c in s] != ["trackingNo", "weightKg", "shippedOn", "recipient"]:
                return False
            if set(s.find("recipient").attrib) != {"country"} or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", (s.findtext("shippedOn") or "").strip()):
                return False
        return len(list(root.iter("Shipment"))) == 3
    return False


def usernames(a, t):
    vals = set(re.findall(r"`\"?([a-z0-9]+)\"?`", a))
    return all(any(len(v) == n for v in vals) for n in (2, 3, 16, 17))


CHECKS = {
    "TD-01": [("reserved domains", RESERVED), ("no real mail", no_rx(REAL_MAIL)), ("51 boundary", rx(r"\b51\b")),
              ("relative age", rx(r"today|reference date|test day|run date"))],
    "TD-02": [("asks provider", rx(r"provider|gateway|PSP|payment service")), none_of("no checksum-valid cards", cards)],
    "TD-03": [none_of("no checksum-valid personnummer", personnummer)],
    "TD-04": [("markers", any_marker)],
    "TD-05": [("placeholders shown", has("{{order number}}", "{{customer email}}")), ("reserved domains", RESERVED)],
    "TD-06": [("JSON fields and totals", json_orders), ("deliberate labeled", rx(r"deliberate|on purpose|intentional"))],
    "TD-07": [("nothing repeated", lacks("Jane Doe", "jane.doe@example.com", "Ola Nordmann", "ola.n@example.org",
                                        "Storgatan 12", "Karl Johans gate 3", "70 000 00 01", "400 00 001")),
              ("production warning", rx(r"production"))],
    "TD-08": [("seeded generator", rx(r"seed|Random\(\d+\)|default_rng\(\d+\)")), ("no mass paste", lambda a, t: len(re.findall(r"@", a)) < 200)],
    "TD-09": [last_only(("data given", rx(r"INSERT INTO|\"orderId\""))), last_only(not_written)],
    "TD-10": [("Swedish marker", has("[ATT KLARGÖRA")), ("RTL script", rx(r"[֐-ۿ]", 0)), ("101", rx(r"\b101\b"))],
    "TD-11": [("markers", has("TEST-", "QA-")), ("qa.userNN", rx(r"qa\.user\d\d@shop\.example")), ("semicolon CSV", rx(r"(?m)^[^\n;]+;[^\n;]+;"))],
    "TD-12": [("verdict", rx(r"needs rework|needs minor|ready to use")), ("emails not repeated", lacks("anna.svensson1987@gmail.com", "erik.berg@gmail.com"))],
    "TD-13": [("values", has_all(rx(r"\b100\b"), rx(r"-1\b"))), ("no invented handling", no_line(r"\b(rounded|capped|clamped)\b", r"TO CLARIFY|\?|\bor\b|whether"))],
    "TD-14": [("skill not loaded", lambda a, t: "test-data/SKILL.md" not in t)],
    "HO-08": [("reserved domains", RESERVED), ("no real mail", no_rx(REAL_MAIL))],
    "HO-09": [("SQL for app_users", rx(r"INSERT INTO\s+\"?app_users")), not_written, ("reserved domains", RESERVED)],
    "HO-50": [("reserved domains", RESERVED), ("not-valid label", rx(r"not (a )?valid|format[- ]only|invalid|not checksum"))],
    "HO-51": [("German", rx(r"\b(und|die|der|ich|ihr|eine)\b", 0)), none_of("no checksum-valid IBANs", ibans)],
    "HO-52": [("markers", any_marker), ("no stated policy", no_line(r"at least \d+ characters|minimum (of )?\d+ characters", r"TO CLARIFY|assum|\?|example|if "))],
    "HO-53": [("0 and 9", has_all(rx(r"\b0\b"), rx(r"\b9\b"))), ("markers", any_marker),
              ("no invented handling", no_line(r"\b(corrected|capped|clamped|rounded)\b", r"TO CLARIFY|\?|\bor\b|whether"))],
    "HO-54": [("placeholder names", has("Kundennummer", "Lieferadresse")), ("German", rx(r"Platzhalter|Wert"))],
    "HO-55": [("rows add up", invoice_rows), ("deliberate labeled", rx(r"deliberate|on purpose|intentional"))],
    "HO-56": [("XML shape", shipments)],
    "HO-57": [("nothing repeated", lacks("karin.lindqvist@outlook.com", "m.yilmaz@hotmail.com", "482 19 33", "905 11 27")),
              ("verdict", rx(r"needs rework|needs minor"))],
    "HO-58": [("relative dates", rx(r"today|reference date|test day|run date"))],
    "HO-59": [("seeded generator", rx(r"seed|Random\(\d+\)|default_rng\(\d+\)")), ("no mass paste", lambda a, t: len(re.findall(r"transaction_id", a)) < 200),
              none_of("no checksum-valid cards", cards)],
    "HO-60": [not_written, ("reserved domains", RESERVED), ("data given", rx(r"viewer"))],
    "HO-61": [("ZZTEST", has("ZZTEST")), ("FI and EE", has_all(rx(r"\bFI\b|Finland"), rx(r"\bEE\b|Eston"))), ("JSON", rx(r"```json|\{\s*\"")),
              ("reserved domains", RESERVED)],
    "HO-62": [("Spanish", rx(r"\b(DNI|letra|formato)\b")), none_of("no valid DNI", dni)],
    "HO-63": [("lengths 2/3/16/17", usernames)],
    "HO-64": [("no real provider addresses", no_rx(REAL_MAIL)), ("reserved domains", RESERVED)],
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
