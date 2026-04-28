# Sprint OS — Startup Onboarding Agent

A command-line tool that generates a structured 6-month sprint plan for any portfolio startup, given their name, vertical, and funding stage.

Built as part of the Hexa Sprint internal tooling stack.

---

## The Problem

When a new startup joins the accelerator, partners spend hours manually structuring the first weeks: setting goals, assigning milestones, identifying risks, and planning their own involvement. This tool automates that scaffolding so partners can spend that time with founders instead.

## What It Does

- Takes a startup's name, vertical (AI for Work / Energy Resilience / Defense), and stage (pre-seed / seed / Series A)
- Generates a month-by-month 6-month sprint plan with themes, deliverables, and partner actions
- Flags key risks specific to the vertical
- Outputs next best actions so the partner knows exactly what to do first
- Optionally saves the plan as a JSON file for ingestion into the Sprint OS dashboard

## How to Run

```bash
# Interactive mode
python3 onboarding_agent.py

# Command-line mode (name, vertical, stage)
python3 onboarding_agent.py "Volta Energy" energy_resilience seed
```

No installs required. Pure Python 3 standard library.

## Sample Output

```
============================================================
  SPRINT OS — 6-MONTH PLAN
  Startup : Volta Energy
  Vertical: energy_resilience
  Stage   : seed
  Generated: 2025-09-01 10:32
============================================================

STAGE CONTEXT
----------------------------------------
Product exists. Focus on repeatable customer acquisition
and early retention signals.

KEY RISKS
----------------------------------------
  ! Long regulatory approval cycles
  ! Capital intensity before revenue
  ! Dependency on single offtake partner

6-MONTH SPRINT PLAN
----------------------------------------

  MONTH 1: DIAGNOSE
  Vertical Focus: Grid resilience mapping
  Deep dive into the startup's current state. Map the
  team, product, customers, and blockers.

  Deliverables:
    - Company diagnostic report (team, product, GTM, financials)
    - Top 3 blocking issues identified with owners assigned
    - Sprint goals confirmed and signed off by founders

  Partner Actions:
    > Introductory calls with all co-founders
    > First board-level strategic alignment session
    > Network introductions: 3 relevant experts or potential customers
...
```

## Design Notes

- Vertical-specific focus areas slot into each month automatically
- Stage context adjusts the strategic framing for pre-seed vs Series A
- JSON output is structured for easy ingestion into a broader Sprint OS dashboard
- Easily extensible: add new verticals or month templates in the config dictionaries at the top of the file

## Stack

- Python 3.11+
- Standard library only (`json`, `datetime`, `textwrap`, `sys`, `argparse`)
