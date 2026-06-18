from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any


FIXTURE_PATH = Path(__file__).resolve().parent.parent / "fixtures" / "eval_scenarios.json"


def load_scenarios() -> dict[str, dict[str, Any]]:
    with FIXTURE_PATH.open(encoding="utf-8") as fixture_file:
        data = json.load(fixture_file)
    return {scenario["scenario_id"]: scenario for scenario in data["scenarios"]}


def scenario(scenario_id: str) -> dict[str, Any]:
    return copy.deepcopy(load_scenarios()[scenario_id])
