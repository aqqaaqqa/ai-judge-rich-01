# ai-judge-rich-01 entry: a single Python file that writes one 30-day plan for growing $100.
# Writes one fixed plan to /output/entry.txt: the plan an AI agent
# would follow to turn $100, a computer with internet access and
# 30 days, with no human doing the work, into the most money.
# The program runs twice with no network, and both runs must write
# the same bytes, so the plan is a constant, written as bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
# for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Plan: sell one $49 spreadsheet rescue, prepaid, over and over.",
        "Day 1: build one reusable Python cleaner (merge, dedupe, fix dates and currency) and a one-page site with a Stripe payment link: $49, 24-hour delivery, refund if late.",
        "Days 2-5: find buyers where they already ask - r/excel, Stack Overflow, Upwork posts - reply with their first 50 rows cleaned free, plus the payment link. No cold outreach to strangers.",
        "Days 6-30: deliver each job in under an hour with the same code, post each review on the site as proof, upsell a $29/month re-clean of the same sheet. Spend $40 on ads only after 10 paid jobs; keep $60 for fees and refunds.",
        "Drop any channel with no paid buyer in 3 days, and double down on the one that pays first. Expected: 15-20 jobs = $735-$980, costs under $60, because the work is templated, prepaid, and the free sample proves it before anyone pays.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
