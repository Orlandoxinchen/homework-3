#!/usr/bin/env python3
"""Build the Homework 3 solution PDF."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    HRFlowable,
    CondPageBreak,
)

FONT = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
pdfmetrics.registerFont(TTFont("TNR", FONT))
pdfmetrics.registerFont(TTFont("TNR-B", FONT.replace(".ttf", " Bold.ttf")))
pdfmetrics.registerFont(TTFont("TNR-I", FONT.replace(".ttf", " Italic.ttf")))
pdfmetrics.registerFont(TTFont("TNR-BI", FONT.replace(".ttf", " Bold Italic.ttf")))
pdfmetrics.registerFontFamily(
    "TNR", normal="TNR", bold="TNR-B", italic="TNR-I", boldItalic="TNR-BI"
)

GITHUB = "https://github.com/Orlandoxinchen/homework-3"
OUT = "/Users/orlando-alex/Documents/Homework3/Xinchen_Leng_Homework3.pdf"

NAVY = colors.HexColor("#1a1a1a")
RULE = colors.HexColor("#222222")
HAIR = colors.HexColor("#666666")
HEAD_BG = colors.HexColor("#f3f3f3")


def S(name, **kw):
    base = dict(
        fontName="TNR",
        fontSize=11,
        leading=15,
        textColor=NAVY,
        alignment=TA_JUSTIFY,
    )
    base.update(kw)
    return ParagraphStyle(name, **base)


styles = {
    "kicker": S("kicker", fontName="TNR", fontSize=10, leading=13, alignment=TA_CENTER, textColor=HAIR),
    "title": S("title", fontName="TNR-B", fontSize=18, leading=22, alignment=TA_CENTER, spaceAfter=2),
    "author": S("author", fontName="TNR-I", fontSize=12, leading=16, alignment=TA_CENTER, spaceBefore=4),
    "h1": S("h1", fontName="TNR-B", fontSize=13, leading=16, alignment=TA_LEFT, spaceBefore=14, spaceAfter=6),
    "h2": S("h2", fontName="TNR-B", fontSize=12, leading=15, alignment=TA_LEFT, spaceBefore=11, spaceAfter=4),
    "body": S("body", spaceAfter=6),
    "eq": S(
        "eq",
        fontName="TNR-I",
        alignment=TA_LEFT,
        leftIndent=18,
        spaceBefore=2,
        spaceAfter=6,
    ),
    "ans": S("ans", fontName="TNR", alignment=TA_LEFT, leftIndent=18, spaceBefore=1, spaceAfter=8),
    "note": S("note", fontSize=10.5, leading=14, spaceAfter=6),
    "link": S("link", alignment=TA_LEFT, textColor=colors.HexColor("#0b3a82"), spaceBefore=2, spaceAfter=8),
    "footer_note": S("footer_note", fontSize=9, leading=12, alignment=TA_LEFT, textColor=HAIR),
}


def P(text, style="body"):
    return Paragraph(text, styles[style])


def eq(text):
    return Paragraph(text, styles["eq"])


def answer(text):
    return Paragraph("<b>Answer.</b>  " + text, styles["ans"])


def booktabs(data, col_widths):
    style_cmds = [
        ("FONTNAME", (0, 0), (-1, 0), "TNR-B"),
        ("FONTNAME", (0, 1), (-1, -1), "TNR"),
        ("FONTSIZE", (0, 0), (-1, -1), 10.5),
        ("LEADING", (0, 0), (-1, -1), 14),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEABOVE", (0, 0), (-1, 0), 1.0, RULE),
        ("LINEBELOW", (0, 0), (-1, 0), 0.4, RULE),
        ("LINEBELOW", (0, -1), (-1, -1), 1.0, RULE),
        ("BACKGROUND", (0, 0), (-1, 0), HEAD_BG),
    ]
    t = Table(data, colWidths=col_widths, hAlign="CENTER")
    t.setStyle(TableStyle(style_cmds))
    return t


def header_footer(canvas, doc):
    canvas.saveState()
    w, h = letter
    canvas.setFillColor(NAVY)
    canvas.setFont("TNR", 9)
    canvas.drawString(0.85 * inch, h - 0.52 * inch, "Xinchen Leng")
    canvas.drawRightString(w - 0.85 * inch, h - 0.52 * inch, "Homework 3")
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.6)
    canvas.line(0.85 * inch, h - 0.62 * inch, w - 0.85 * inch, h - 0.62 * inch)
    canvas.setFont("TNR", 9)
    canvas.drawCentredString(w / 2, 0.48 * inch, str(doc.page))
    canvas.restoreState()


def build():
    doc = SimpleDocTemplate(
        OUT,
        pagesize=letter,
        leftMargin=0.85 * inch,
        rightMargin=0.85 * inch,
        topMargin=0.82 * inch,
        bottomMargin=0.7 * inch,
        title="Homework 3",
        author="Xinchen Leng",
    )
    story = []

    story.append(P("Probability and a fraud-detection simulation", "kicker"))
    story.append(Spacer(1, 6))
    story.append(P("Homework 3", "title"))
    story.append(P("Xinchen Leng", "author"))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=8))
    story.append(
        P(
            "Part 1 works the four analytical problems in full. Part 2 is the simulation "
            "of Question 1. The code, with seed 42 and 100,000 transactions, is at the "
            "GitHub link below. That link is the Part 2 deliverable."
        )
    )
    story.append(P(f'<link href="{GITHUB}">{GITHUB}</link>', "link"))

    # ----- Q1 -----
    story.append(P("Part 1. Analytical problems", "h1"))
    story.append(P("1. Amazon fraud detection", "h2"))
    story.append(
        P(
            "The system has sensitivity P(Flagged | Fraud) = 0.98, specificity "
            "P(Not flagged | Legitimate) = 0.95, and base rate P(Fraud) = 0.001. "
            "Specificity fixes the false-positive rate:"
        )
    )
    story.append(eq("P(Flagged | Legitimate) = 1 − 0.95 = 0.05."))
    story.append(eq("P(Legitimate) = 1 − 0.001 = 0.999."))

    story.append(P("1(a). Probability that a flagged transaction is fraud", "h2"))
    story.append(
        P(
            "Bayes’ theorem writes the target as the joint probability of a true detection "
            "divided by the probability of any flag:"
        )
    )
    story.append(
        eq("P(Fraud | Flagged) = P(Flagged | Fraud) P(Fraud) / P(Flagged).")
    )
    story.append(
        P(
            "The law of total probability splits flags into those that come from fraud "
            "and those that come from legitimate transactions:"
        )
    )
    story.append(
        eq(
            "P(Flagged) = P(Flagged | Fraud) P(Fraud) "
            "+ P(Flagged | Legitimate) P(Legitimate)"
        )
    )
    story.append(eq("= (0.98)(0.001) + (0.05)(0.999)"))
    story.append(eq("= 0.00098 + 0.04995"))
    story.append(eq("= 0.05093."))
    story.append(
        P(
            "The numerator is the first of those two pieces, the true detections. "
            "Dividing gives"
        )
    )
    story.append(eq("P(Fraud | Flagged) = 0.00098 / 0.05093 = 98/5093 ≈ 0.01924."))
    story.append(
        answer(
            "0.01924, or about 1.92 percent. A flag is weak evidence of fraud. "
            "Fraud is rare, and a 5 percent false-positive rate applied to the "
            "99.9 percent of transactions that are legitimate produces almost all of the flags."
        )
    )

    story.append(P("1(b). Specificity raised to 0.99", "h2"))
    story.append(
        P(
            "Specificity 0.99 means P(Flagged | Legitimate) = 0.01. Sensitivity and "
            "the base rate stay the same, so the true-detection term is unchanged:"
        )
    )
    story.append(eq("P(Flagged) = (0.98)(0.001) + (0.01)(0.999)"))
    story.append(eq("= 0.00098 + 0.00999 = 0.01097."))
    story.append(eq("P(Fraud | Flagged) = 0.00098 / 0.01097 = 98/1097 ≈ 0.08933."))
    story.append(
        answer(
            "0.08933, or about 8.93 percent. The posterior is about 4.6 times the "
            "answer in part (a)."
        )
    )
    story.append(
        P(
            "The business change is in the review queue, not in the share of fraud "
            "that is caught. Sensitivity is still 0.98, so the same fraction of "
            "fraudulent transactions is flagged. What falls is the false-positive "
            "rate, from 5 percent to 1 percent. Flags drop from about 5.09 percent "
            "of all transactions to about 1.10 percent, and a reviewed flag is much "
            "more likely to be a real case. Automatic blocking is still a poor rule: "
            "even after the change, about 91 percent of flags are legitimate. The "
            "gain is a shorter queue and fewer good customers pulled into review."
        )
    )

    # ----- Q2 -----
    story.append(P("2. Portfolio of two independent tech stocks", "h2"))
    story.append(
        P(
            "Returns are written as decimals. Stock A and Stock B are independent, "
            "so Cov(X, Y) = 0."
        )
    )
    story.append(Spacer(1, 2))
    story.append(
        booktabs(
            [
                ["Stock A return", "−2%", "0%", "3%", "5%"],
                ["P(X)", "0.1", "0.3", "0.4", "0.2"],
                ["Stock B return", "3%", "1%", "4%", ""],
                ["P(Y)", "0.2", "0.5", "0.3", ""],
            ],
            [1.45 * inch, 1.15 * inch, 1.15 * inch, 1.15 * inch, 1.15 * inch],
        )
    )
    story.append(Spacer(1, 8))

    story.append(P("2(a). Expected returns", "h2"))
    story.append(eq("E[X] = (−0.02)(0.1) + (0)(0.3) + (0.03)(0.4) + (0.05)(0.2)"))
    story.append(eq("= −0.002 + 0 + 0.012 + 0.010 = 0.020."))
    story.append(eq("E[Y] = (0.03)(0.2) + (0.01)(0.5) + (0.04)(0.3)"))
    story.append(eq("= 0.006 + 0.005 + 0.012 = 0.023."))
    story.append(answer("E[X] = 0.020 (2.00 percent). E[Y] = 0.023 (2.30 percent)."))

    story.append(P("2(b). Variances, shortcut formula", "h2"))
    story.append(P("The shortcut is Var(X) = E[X<sup>2</sup>] − (E[X])<sup>2</sup>."))
    story.append(eq("E[X<sup>2</sup>] = (−0.02)<sup>2</sup>(0.1) + (0.03)<sup>2</sup>(0.4) + (0.05)<sup>2</sup>(0.2)"))
    story.append(eq("= (0.0004)(0.1) + (0.0009)(0.4) + (0.0025)(0.2)"))
    story.append(eq("= 0.00004 + 0.00036 + 0.00050 = 0.00090."))
    story.append(eq("Var(X) = 0.00090 − (0.020)<sup>2</sup> = 0.00090 − 0.00040 = 0.00050."))
    story.append(eq("E[Y<sup>2</sup>] = (0.03)<sup>2</sup>(0.2) + (0.01)<sup>2</sup>(0.5) + (0.04)<sup>2</sup>(0.3)"))
    story.append(eq("= (0.0009)(0.2) + (0.0001)(0.5) + (0.0016)(0.3)"))
    story.append(eq("= 0.00018 + 0.00005 + 0.00048 = 0.00071."))
    story.append(eq("Var(Y) = 0.00071 − (0.023)<sup>2</sup> = 0.00071 − 0.000529 = 0.000181."))
    story.append(answer("Var(X) = 0.00050. Var(Y) = 0.000181."))

    story.append(P("2(c). Portfolio R = 0.6X + 0.4Y", "h2"))
    story.append(
        P(
            "Linearity of expectation does not need independence. Independence is used "
            "for the variance, where the covariance term drops out."
        )
    )
    story.append(eq("E[R] = 0.6 E[X] + 0.4 E[Y] = 0.6(0.020) + 0.4(0.023)"))
    story.append(eq("= 0.012 + 0.0092 = 0.0212."))
    story.append(
        eq(
            "Var(R) = (0.6)<sup>2</sup> Var(X) + (0.4)<sup>2</sup> Var(Y)"
        )
    )
    story.append(eq("= (0.36)(0.00050) + (0.16)(0.000181)"))
    story.append(eq("= 0.000180 + 0.00002896 = 0.00020896."))
    story.append(
        answer(
            "E[R] = 0.0212 (2.12 percent). Var(R) = 0.00020896."
        )
    )

    # ----- Q3 -----
    story.append(P("3. Server response time", "h2"))
    story.append(
        P(
            "The density is f(x) = (3/8) x<sup>2</sup> for 0 ≤ x ≤ 2, and f(x) = 0 otherwise."
        )
    )

    story.append(P("3(a). Valid PDF", "h2"))
    story.append(
        P(
            "On [0, 2], x<sup>2</sup> ≥ 0 and 3/8 &gt; 0, so f(x) ≥ 0. Outside that interval "
            "the density is zero, which is also nonnegative. The integral is"
        )
    )
    story.append(eq("∫ (3/8) x<sup>2</sup> dx from 0 to 2 = (3/8) · (x<sup>3</sup>/3) from 0 to 2"))
    story.append(eq("= (1/8) x<sup>3</sup> from 0 to 2 = (1/8)(8) − 0 = 1."))
    story.append(
        answer(
            "The function is nonnegative and integrates to 1, so it is a valid PDF."
        )
    )

    story.append(P("3(b). CDF on [0, 2]", "h2"))
    story.append(eq("F(x) = P(X ≤ x) = ∫ (3/8) t<sup>2</sup> dt from 0 to x"))
    story.append(eq("= (1/8) t<sup>3</sup> from 0 to x = x<sup>3</sup>/8, &nbsp;&nbsp; 0 ≤ x ≤ 2."))
    story.append(answer("F(x) = x<sup>3</sup>/8 for 0 ≤ x ≤ 2."))

    story.append(P("3(c). Three probabilities", "h2"))
    story.append(eq("P(X ≤ 1) = F(1) = 1<sup>3</sup>/8 = 1/8 = 0.125."))
    story.append(
        eq(
            "P(0.5 ≤ X ≤ 1.5) = F(1.5) − F(0.5) = (1.5)<sup>3</sup>/8 − (0.5)<sup>3</sup>/8"
        )
    )
    story.append(eq("= (3.375)/8 − (0.125)/8 = 3.250/8 = 0.40625."))
    story.append(
        P(
            "In fractions, (1.5)<sup>3</sup> = 27/8 and (0.5)<sup>3</sup> = 1/8, so"
        )
    )
    story.append(eq("F(1.5) − F(0.5) = (27/64) − (1/64) = 26/64 = 13/32."))
    story.append(eq("P(X &gt; 1.5) = 1 − F(1.5) = 1 − 27/64 = 37/64 = 0.578125."))
    story.append(
        answer(
            "P(X ≤ 1) = 1/8 = 0.125. "
            "P(0.5 ≤ X ≤ 1.5) = 13/32 = 0.40625. "
            "P(X &gt; 1.5) = 37/64 = 0.578125."
        )
    )

    # ----- Q4 -----
    story.append(
        KeepTogether(
            [
                P("4. Binomial and hypergeometric", "h2"),
                P("4(a). Binomial clicks", "h2"),
                P(
                    "Each of 10 users clicks with probability 0.20, independently, so "
                    "X ~ Binomial(n = 10, p = 0.20). The point mass is"
                ),
            ]
        )
    )
    story.append(eq("P(X = 3) = C(10, 3) (0.20)<sup>3</sup> (0.80)<sup>7</sup>."))
    story.append(eq("C(10, 3) = 120."))
    story.append(eq("(0.20)<sup>3</sup> = 0.008."))
    story.append(eq("(0.80)<sup>7</sup> = 0.2097152."))
    story.append(eq("P(X = 3) = 120 × 0.008 × 0.2097152 = 0.201326592."))
    story.append(
        P(
            "The same value as a reduced fraction is 393,216 / 1,953,125, "
            "from C(10, 3) (1/5)<sup>3</sup> (4/5)<sup>7</sup>."
        )
    )
    story.append(answer("P(X = 3) = 0.201326592."))

    story.append(P("4(b). Hypergeometric defects", "h2"))
    story.append(
        P(
            "The batch has N = 20 products, of which K = 4 are defective. The inspector "
            "draws n = 5 products without replacement, so Y ~ Hypergeometric(N = 20, K = 4, n = 5). "
            "Exactly one defective item in the sample means 1 defective chosen from 4 and "
            "4 non-defective chosen from 16:"
        )
    )
    story.append(eq("P(Y = 1) = C(4, 1) C(16, 4) / C(20, 5)."))
    story.append(eq("C(4, 1) = 4."))
    story.append(eq("C(16, 4) = (16 × 15 × 14 × 13) / (4 × 3 × 2 × 1) = 1,820."))
    story.append(eq("C(20, 5) = (20 × 19 × 18 × 17 × 16) / 120 = 15,504."))
    story.append(eq("P(Y = 1) = (4 × 1,820) / 15,504 = 7,280 / 15,504 = 455/969 ≈ 0.46956."))
    story.append(answer("P(Y = 1) = 455/969 ≈ 0.46956."))

    # ----- Part 2 -----
    story.append(P("Part 2. Coding problem", "h1"))
    story.append(
        P(
            "The simulation follows the assignment steps: seed 42, 100,000 transactions, "
            "fraud drawn at rate 0.001, fraudulent transactions flagged with probability 0.98, "
            "and legitimate transactions flagged with probability 0.05. "
            "The file is <font face='TNR-I'>fraud_simulation.py</font>."
        )
    )
    story.append(P(f'<link href="{GITHUB}">{GITHUB}</link>', "link"))
    story.append(
        P(
            "With this seed the draw contains 102 fraudulent transactions, not the expected "
            "100. Of those 102, 98 are flagged. Legitimate transactions contribute 4,894 flags. "
            "The empirical conditional probability is therefore"
        )
    )
    story.append(eq("P̂(Fraud | Flagged) = 98 / 4,992 = 0.0196,"))
    story.append(
        P(
            "printed to four decimals, against the Part 1(a) value 0.0192. "
            "The two agree to three decimals. The gap is ordinary binomial noise "
            "in a rare-event sample: only about 100 frauds are expected, so the "
            "numerator moves by a few counts."
        )
    )
    story.append(Spacer(1, 4))
    story.append(
        KeepTogether(
            [
                booktabs(
                    [
                        ["", "Not flagged", "Flagged"],
                        ["Not fraud", "95,004", "4,894"],
                        ["Fraud", "4", "98"],
                    ],
                    [1.6 * inch, 1.7 * inch, 1.7 * inch],
                ),
                Spacer(1, 8),
                P(
                    "True positive = 98 (fraud and flagged). "
                    "False positive = 4,894 (not fraud and flagged). "
                    "True negative = 95,004 (not fraud and not flagged). "
                    "False negative = 4 (fraud and not flagged). "
                    "The false positives dominate the flagged column, which is the same fact "
                    "Part 1(a) produced from Bayes’ theorem."
                ),
            ]
        )
    )

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print("wrote", OUT)


if __name__ == "__main__":
    build()
