"""
Sprint OS — Startup Onboarding Agent
Generates a structured 6-month sprint plan for a startup
given their name, vertical, and stage.
"""

import json
import datetime
import textwrap
import sys

VERTICALS = {
    "ai_for_work": {
        "focus_areas": [
            "Workflow automation audit",
            "LLM integration strategy",
            "Internal tool consolidation",
            "Agent deployment pilot",
            "Adoption and change management",
            "Scale and iteration"
        ],
        "key_risks": [
            "Over-engineering before product-market fit",
            "Low user adoption of AI tools",
            "Data privacy and compliance gaps"
        ]
    },
    "energy_resilience": {
        "focus_areas": [
            "Grid resilience mapping",
            "Regulatory landscape audit",
            "Pilot site identification",
            "Technical feasibility study",
            "Partnership and offtake agreements",
            "Fundraising preparation"
        ],
        "key_risks": [
            "Long regulatory approval cycles",
            "Capital intensity before revenue",
            "Dependency on single offtake partner"
        ]
    },
    "defense": {
        "focus_areas": [
            "Customer discovery with defence primes",
            "Compliance and clearance roadmap",
            "MVP definition for dual-use case",
            "Pilot contract structuring",
            "IP protection strategy",
            "Government grant identification"
        ],
        "key_risks": [
            "Long procurement cycles",
            "Export control restrictions",
            "Talent acquisition in cleared environments"
        ]
    }
}

MONTH_TEMPLATES = [
    {
        "month": 1,
        "theme": "Diagnose",
        "description": "Deep dive into the startup's current state. Map the team, product, customers, and blockers.",
        "deliverables": [
            "Company diagnostic report (team, product, GTM, financials)",
            "Top 3 blocking issues identified with owners assigned",
            "Sprint goals confirmed and signed off by founders"
        ],
        "partner_actions": [
            "Introductory calls with all co-founders",
            "First board-level strategic alignment session",
            "Network introductions: 3 relevant experts or potential customers"
        ]
    },
    {
        "month": 2,
        "theme": "Focus",
        "description": "Narrow the company's focus to the highest-leverage activity. Kill distractions.",
        "deliverables": [
            "Prioritised OKRs for the next 90 days",
            "Weekly cadence and reporting rhythm established",
            "First set of action items cleared from Month 1 diagnostic"
        ],
        "partner_actions": [
            "Weekly 60-minute working session with founders",
            "Fundraising narrative review if applicable",
            "Intro to 2 potential investors or strategic partners"
        ]
    },
    {
        "month": 3,
        "theme": "Build",
        "description": "Execute. The startup is heads-down building or selling. Partner provides unblocking support.",
        "deliverables": [
            "Mid-sprint milestone review against Month 1 goals",
            "Updated financial model or runway projection",
            "At least 1 new customer conversation or pilot initiated"
        ],
        "partner_actions": [
            "Bi-weekly check-ins (30 min)",
            "One deep-dive session on a specific blocker",
            "Help close 1 key hire or advisor if needed"
        ]
    },
    {
        "month": 4,
        "theme": "Validate",
        "description": "Test assumptions with the market. Get external signal. Adjust based on evidence, not opinion.",
        "deliverables": [
            "Customer feedback synthesis (min. 5 conversations)",
            "Revised product or GTM hypothesis if signal warrants it",
            "Competitive landscape updated"
        ],
        "partner_actions": [
            "Customer introduction pipeline review",
            "Press or visibility opportunity identified",
            "Fundraising data room review if applicable"
        ]
    },
    {
        "month": 5,
        "theme": "Accelerate",
        "description": "Double down on what is working. Cut what is not. Prepare for the next phase.",
        "deliverables": [
            "Growth metric baseline established",
            "Next funding round or revenue target defined",
            "Team gaps identified and hiring plan drafted"
        ],
        "partner_actions": [
            "Warm introductions to 3 Series A investors if pre-seed/seed",
            "Help define the post-Sprint roadmap",
            "Alumni network activation for distribution or partnership"
        ]
    },
    {
        "month": 6,
        "theme": "Launch",
        "description": "Exit the Sprint programme with momentum. Public signal, investor narrative, and a clear next chapter.",
        "deliverables": [
            "Sprint retrospective and lessons learned document",
            "Updated investor deck and data room",
            "Demo Day preparation: pitch, narrative, metrics"
        ],
        "partner_actions": [
            "Demo Day organisation and coaching",
            "Final network introductions",
            "Post-Sprint support plan agreed"
        ]
    }
]

STAGE_ADVICE = {
    "pre_seed": "Focus is on founder-market fit, problem validation, and first 10 customers. Avoid building too early.",
    "seed": "Product exists. Focus on repeatable customer acquisition and early retention signals.",
    "series_a": "Unit economics matter now. Focus on scalable GTM and team structure for growth."
}


def generate_sprint_plan(name: str, vertical: str, stage: str) -> dict:
    vertical_key = vertical.lower().replace(" ", "_")
    stage_key = stage.lower().replace(" ", "_").replace("-", "_")

    vertical_data = VERTICALS.get(vertical_key, VERTICALS["ai_for_work"])
    stage_note = STAGE_ADVICE.get(stage_key, "Focus on what gets you to the next milestone.")

    months = []
    for i, template in enumerate(MONTH_TEMPLATES):
        month = dict(template)
        if i < len(vertical_data["focus_areas"]):
            month["vertical_focus"] = vertical_data["focus_areas"][i]
        months.append(month)

    plan = {
        "startup": name,
        "vertical": vertical,
        "stage": stage,
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "stage_context": stage_note,
        "key_risks": vertical_data["key_risks"],
        "sprint_plan": months,
        "next_best_actions": [
            f"Schedule Month 1 diagnostic call with {name} founders this week",
            "Share this plan with the startup for co-creation and buy-in",
            "Assign a primary partner contact for weekly cadence",
            "Add to Sprint OS dashboard and set Month 1 milestone reminders"
        ]
    }
    return plan


def print_plan(plan: dict):
    sep = "=" * 60

    print(f"\n{sep}")
    print(f"  SPRINT OS — 6-MONTH PLAN")
    print(f"  Startup : {plan['startup']}")
    print(f"  Vertical: {plan['vertical']}")
    print(f"  Stage   : {plan['stage']}")
    print(f"  Generated: {plan['generated_at']}")
    print(f"{sep}\n")

    print(f"STAGE CONTEXT\n{'-'*40}")
    print(textwrap.fill(plan['stage_context'], width=60))
    print()

    print(f"KEY RISKS\n{'-'*40}")
    for risk in plan['key_risks']:
        print(f"  ! {risk}")
    print()

    print(f"6-MONTH SPRINT PLAN\n{'-'*40}")
    for month in plan['sprint_plan']:
        print(f"\n  MONTH {month['month']}: {month['theme'].upper()}")
        if 'vertical_focus' in month:
            print(f"  Vertical Focus: {month['vertical_focus']}")
        print(f"  {textwrap.fill(month['description'], width=56, subsequent_indent='  ')}")
        print(f"\n  Deliverables:")
        for d in month['deliverables']:
            print(f"    - {d}")
        print(f"\n  Partner Actions:")
        for a in month['partner_actions']:
            print(f"    > {a}")

    print(f"\n{sep}")
    print(f"NEXT BEST ACTIONS")
    print(f"{'-'*40}")
    for i, action in enumerate(plan['next_best_actions'], 1):
        print(f"  {i}. {action}")
    print(f"{sep}\n")


def save_plan(plan: dict, filename: str):
    with open(filename, 'w') as f:
        json.dump(plan, f, indent=2)
    print(f"Plan saved to {filename}")


def get_input(prompt: str, options: list = None) -> str:
    while True:
        value = input(prompt).strip()
        if not value:
            print("  Input cannot be empty. Please try again.")
            continue
        if options and value.lower().replace(" ", "_").replace("-", "_") not in options:
            print(f"  Please choose from: {', '.join(options)}")
            continue
        return value


def main():
    print("\nSPRINT OS — Startup Onboarding Agent")
    print("--------------------------------------")
    print("This tool generates a structured 6-month sprint plan")
    print("for a portfolio startup.\n")

    if len(sys.argv) == 4:
        name = sys.argv[1]
        vertical = sys.argv[2]
        stage = sys.argv[3]
        print(f"Running with: {name} | {vertical} | {stage}\n")
    else:
        name = get_input("Startup name: ")
        print(f"\nVerticals available: {', '.join(VERTICALS.keys())}")
        vertical = get_input("Vertical (ai_for_work / energy_resilience / defense): ",
                             list(VERTICALS.keys()))
        print(f"\nStages available: pre_seed, seed, series_a")
        stage = get_input("Stage (pre_seed / seed / series_a): ",
                          ["pre_seed", "seed", "series_a"])

    plan = generate_sprint_plan(name, vertical, stage)
    print_plan(plan)

    save = input("Save plan as JSON? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"{name.lower().replace(' ', '_')}_sprint_plan.json"
        save_plan(plan, filename)


if __name__ == "__main__":
    main()
