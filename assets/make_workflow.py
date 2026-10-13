#!/usr/bin/env python3
"""Generate the README workflow illustration in light and dark versions.

Run from the repository root: python3 assets/make_workflow.py
Every preview text is an excerpt from a real run in examples/.
"""
from xml.sax.saxutils import escape

W, H = 1280, 470
CARD_W, CARD_H, GAP, LEFT, TOP = 200, 270, 55, 30, 130
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

THEMES = {
    "light": dict(text="#1f2328", muted="#59636e", card="#ffffff", stroke="#d1d9e0",
                  inner="#f6f8fa", accent="#8250df", chip="#fbefff", passed="#1a7f37",
                  failed="#cf222e", notrun="#d1d9e0", arrow="#8c959f"),
    "dark": dict(text="#e6edf3", muted="#9198a1", card="#161b22", stroke="#3d444d",
                 inner="#0d1117", accent="#b083f0", chip="#2a1f3d", passed="#3fb950",
                 failed="#f85149", notrun="#3d444d", arrow="#656c76"),
}

# (step title, command, preview lines). Preview line kinds:
#   ("quote", text) italic muted, ("text", text), ("bold", text),
#   ("mono", text), ("chip", text), ("small", text), ("gap", None), ("bar", None)
CARDS = [
    ("Review requirements", "/review-requirements", [
        ("quote", "“The reset link should"),
        ("quote", "be valid for a"),
        ("quote", "reasonable time.”"),
        ("gap", None),
        ("text", "How long is the link"),
        ("text", "valid, …?"),
        ("gap", None),
        ("chip", "[TO CLARIFY: …]"),
    ]),
    ("Design test cases", "/test-cases", [
        ("small", "STEP 1"),
        ("text", "Enter the voucher and"),
        ("text", "select 'Apply'."),
        ("bold", "Total is reduced by 25%."),
        ("gap", None),
        ("small", "STEP 2"),
        ("text", "Select 'Place order'."),
        ("chip", "[TO CLARIFY: …]"),
    ]),
    ("Create test data", "/test-data", [
        ("mono", "Åsa Solvind"),
        ("mono", "Rhys O'Harper"),
        ("mono", "…@example.org"),
        ("mono", "+447700900000"),
        ("gap", None),
        ("small", "NAME LENGTH"),
        ("text", "0 · 1 · 50 · 51"),
        ("small", "reserved and fictional values"),
    ]),
    ("Report defects", "/bug-report", [
        ("bold", "SPRING10 leaves total"),
        ("bold", "unchanged"),
        ("gap", None),
        ("small", "EXPECTED"),
        ("mono", "45.00 EUR"),
        ("small", "ACTUAL"),
        ("mono", "50.00 EUR"),
        ("text", "High (suggested)"),
    ]),
    ("Summarize results", "/test-summary", [
        ("small", "OF 80 PLANNED TESTS"),
        ("bar", None),
        ("gap", None),
        ("key", ("passed", "47 passed")),
        ("key", ("failed", "3 failed")),
        ("key", ("notrun", "30 not run")),
        ("gap", None),
        ("small", "94% of the 50 tests run"),
    ]),
]


def card_x(i):
    return LEFT + i * (CARD_W + GAP)


def text(x, y, s, size, fill, family=SANS, weight="normal", style="normal", anchor="start",
         spacing=None):
    sp = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" font-style="{style}" text-anchor="{anchor}"{sp}>'
            f"{escape(s)}</text>")


def render(t):
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
         f'height="{H}" role="img" aria-labelledby="title desc">',
         '<title id="title">From requirement to release report</title>',
         '<desc id="desc">Five skills in a row: review requirements, design test cases, '
         'create test data, then run the tests, report defects, and summarize results. '
         'Each card shows a short excerpt of real output.</desc>',
         "<defs>",
         f'<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
         f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
         f'fill="{t["arrow"]}"/></marker>',
         "</defs>"]

    o.append(text(LEFT, 46, "From requirement to release report", 28, t["text"], weight="700"))
    o.append(text(LEFT, 76, "Five skills for one test round. Each one asks instead of guessing.",
                  16, t["muted"]))

    # checkpoint between card 3 and card 4
    cx = card_x(3) - GAP / 2
    o.append(f'<line x1="{cx}" y1="124" x2="{cx}" y2="425" stroke="{t["accent"]}" '
             f'stroke-width="1.5" stroke-dasharray="5 5"/>')
    o.append(f'<rect x="{cx - 58}" y="96" width="116" height="26" rx="13" fill="{t["chip"]}" '
             f'stroke="{t["accent"]}" stroke-width="1"/>')
    o.append(text(cx, 114, "▶ Run the tests", 12.5, t["accent"], weight="600", anchor="middle"))

    # results path from the checkpoint to the summary card
    sx = card_x(4) + CARD_W / 2
    o.append(f'<path d="M{cx},425 L{sx},425 L{sx},{TOP + CARD_H + 4}" fill="none" '
             f'stroke="{t["arrow"]}" stroke-width="1.5" marker-end="url(#arrow)"/>')
    o.append(text(card_x(3) + CARD_W / 2, 419, "all results", 11.5, t["muted"], anchor="middle"))

    # arrows between cards
    mid = TOP + CARD_H / 2
    for i in range(4):
        x1, x2 = card_x(i) + CARD_W + 4, card_x(i + 1) - 4
        o.append(f'<line x1="{x1}" y1="{mid}" x2="{x2}" y2="{mid}" stroke="{t["arrow"]}" '
                 f'stroke-width="1.5" marker-end="url(#arrow)"/>')

    for i, (title, cmd, lines) in enumerate(CARDS):
        x, y = card_x(i), TOP
        o.append(f'<rect x="{x}" y="{y}" width="{CARD_W}" height="{CARD_H}" rx="12" '
                 f'fill="{t["card"]}" stroke="{t["stroke"]}" stroke-width="1"/>')
        o.append(f'<circle cx="{x + 26}" cy="{y + 26}" r="11" fill="{t["accent"]}"/>')
        o.append(text(x + 26, y + 30.5, str(i + 1), 12.5, t["card"], weight="700",
                      anchor="middle"))
        o.append(text(x + 16, y + 62, title, 16, t["text"], weight="700"))
        o.append(text(x + 16, y + 81, cmd, 12, t["accent"], family=MONO))
        ix, iy, iw, ih = x + 12, y + 96, CARD_W - 24, CARD_H - 108
        o.append(f'<rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" rx="8" '
                 f'fill="{t["inner"]}"/>')
        ly = iy + 22
        for kind, s in lines:
            px = ix + 10
            if kind == "gap":
                ly += 7
                continue
            if kind == "bar":
                bw = iw - 20
                widths = [bw * 47 / 80, bw * 3 / 80, bw * 30 / 80]
                colors = [t["passed"], t["failed"], t["notrun"]]
                bx = px
                for wpart, c in zip(widths, colors):
                    o.append(f'<rect x="{bx:.1f}" y="{ly - 10}" width="{wpart:.1f}" height="12" '
                             f'fill="{c}"/>')
                    bx += wpart
                ly += 16
                continue
            if kind == "quote":
                o.append(text(px, ly, s, 13, t["muted"], style="italic"))
            elif kind == "key":
                color, label = s
                o.append(f'<rect x="{px}" y="{ly - 10}" width="10" height="10" rx="2" fill="{t[color]}"/>')
                o.append(text(px + 16, ly, label, 13.5, t["text"]))
            elif kind == "text":
                o.append(text(px, ly, s, 13.5, t["text"]))
            elif kind == "bold":
                o.append(text(px, ly, s, 13.5, t["text"], weight="700"))
            elif kind == "mono":
                o.append(text(px, ly, s, 13, t["text"], family=MONO))
            elif kind == "small":
                o.append(text(px, ly, s, 10, t["muted"], weight="600", spacing="0.4"))
            elif kind == "chip":
                cw = len(s) * 7.0 + 14
                o.append(f'<rect x="{px - 2}" y="{ly - 13}" width="{cw}" height="19" rx="9.5" '
                         f'fill="{t["chip"]}" stroke="{t["accent"]}" stroke-width="1"/>')
                o.append(text(px + 5, ly, s, 11.5, t["accent"], family=MONO, weight="600"))
            ly += 18.5 if kind != "small" else 15

    o.append(text(W / 2, 458, "Previews are excerpts from real runs. See the examples folder.",
                  12, t["muted"], anchor="middle"))
    o.append("</svg>")
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    for name, theme in THEMES.items():
        with open(f"assets/workflow-{name}.svg", "w", encoding="utf-8") as f:
            f.write(render(theme))
        print(f"wrote assets/workflow-{name}.svg")
