#!/usr/bin/env python3
"""Generate the GitHub social preview image (1280×640) as SVG.

Run from the repository root: python3 assets/make_social.py
Render it to PNG for upload under Settings → Social preview.
"""
from xml.sax.saxutils import escape

W, H = 1280, 640
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
TEXT, MUTED, ACCENT, CHIP, CARD, STROKE = (
    "#1f2328", "#59636e", "#8250df", "#fbefff", "#ffffff", "#d1d9e0")
STEPS = ["Review requirements", "Design test cases", "Create test data",
         "Report defects", "Summarize results"]


def text(x, y, s, size, fill, family=SANS, weight="normal", anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{escape(s)}</text>')


def render():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
         f'<rect width="{W}" height="{H}" fill="#f6f8fa"/>',
         f'<rect x="0" y="0" width="{W}" height="10" fill="{ACCENT}"/>',
         text(80, 170, "Test Skills", 84, TEXT, weight="800"),
         text(80, 236, "Five AI skills for software testers,", 38, TEXT, weight="600"),
         text(80, 286, "from requirement to release report.", 38, TEXT, weight="600"),
         text(80, 344, "Built to ask instead of making things up.", 26, MUTED)]
    chip = "[TO CLARIFY: …]"
    cw = len(chip) * 15.5 + 36
    o.append(f'<rect x="{W - 80 - cw}" y="122" width="{cw}" height="56" rx="28" '
             f'fill="{CHIP}" stroke="{ACCENT}" stroke-width="2"/>')
    o.append(text(W - 80 - cw / 2, 160, chip, 26, ACCENT, family=MONO, weight="700",
                  anchor="middle"))

    # five steps as connected cards
    n, gap, y, h = len(STEPS), 28, 410, 110
    cardw = (W - 160 - gap * (n - 1)) / n
    for i, step in enumerate(STEPS):
        x = 80 + i * (cardw + gap)
        o.append(f'<rect x="{x:.1f}" y="{y}" width="{cardw:.1f}" height="{h}" rx="14" '
                 f'fill="{CARD}" stroke="{STROKE}" stroke-width="1.5"/>')
        o.append(f'<circle cx="{x + 30:.1f}" cy="{y + 32}" r="15" fill="{ACCENT}"/>')
        o.append(text(f"{x + 30:.1f}", y + 38.5, str(i + 1), 17, CARD, weight="700",
                      anchor="middle"))
        first, _, second = step.partition(" ")
        o.append(text(f"{x + 18:.1f}", y + 72, first, 21, TEXT, weight="700"))
        o.append(text(f"{x + 18:.1f}", y + 95, second, 21, TEXT, weight="700"))
        if i < n - 1:
            ax = x + cardw + 4
            o.append(f'<path d="M{ax:.1f},{y + h / 2} l{gap - 10},0" stroke="#8c959f" '
                     f'stroke-width="2.5"/>')
            o.append(f'<path d="M{ax + gap - 14:.1f},{y + h / 2 - 6} l7,6 l-7,6" fill="none" '
                     f'stroke="#8c959f" stroke-width="2.5"/>')

    o.append(text(80, 584, "Claude Code  ·  Codex  ·  Agent Skills format  ·  Any language  ·  MIT",
                  22, MUTED))
    o.append("</svg>")
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    with open("assets/social-preview.svg", "w", encoding="utf-8") as f:
        f.write(render())
    print("wrote assets/social-preview.svg")
