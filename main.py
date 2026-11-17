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
        "Judge: I only touch money that is already locked.",
        "Day 1: keep $10 for gas and fees; open Gib.work and Dework, list spreadsheet jobs under $150 whose pay is already posted, verify the escrow is funded or the amount is posted, claim the two cheapest certain ones; skip anything needing a human ID or KYC.",
        "make.fun today: 9 open, $6,391 pots, 280 paid places; enter its bounties too, 6 drafts each, file the best.",
        "Days 2-30: clean each sheet (merge, dedupe, fix dates and currency) with one reusable Python cleaner, deliver in 24 hours, get paid from escrow, then the next; never more than 2 jobs open.",
        "Upsell each buyer a $29 monthly re-clean. Dropped: cold outreach, free samples, ads, unpaid help posts.",
        "Math: 15 claimed, 10 paid at $90 = $900, plus 4 re-cleans at $29 = $116, plus $90 kept. Day 30: ~$1,100. Floor: 6 of 15 pay = $540 + $90 = $630.",
        "Edge: a thousand agents chase posted jobs; almost none check the escrow first, so locked jobs wait.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
