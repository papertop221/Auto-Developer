import json
import os
import sys
from datetime import datetime

STATE_FILE = ".auto-dev-state.json"

VALID_PHASES = [
    "1: Discovery & Context Mapping",
    "2: Empirical Research & Feasibility",
    "3: Formal Architecture & Design",
    "4: Surgical Implementation",
    "5: Exhaustive Validation & Quality Assurance",
    "6: Documentation & Delivery",
    "7: Post-Mortem & Knowledge Consolidation"
]

TAXONOMY_TYPES = ["ENV_ERR", "LOGIC_ERR", "SPEC_ERR", "OTHER"]

def load_state():
    default_state = {
        "current_phase": 0,
        "completed_tasks": [],
        "requirements": [],
        "error_log": [],
        "decision_log": [],
        "history": []
    }
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                state = json.load(f)
                # Ensure all default keys exist for migration
                for key, value in default_state.items():
                    if key not in state:
                        state[key] = value
                return state
        except json.JSONDecodeError:
            pass
    return default_state

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def main():
    if len(sys.argv) < 2:
        print("Usage: python state_manager.py [get|set-phase|add-task|set-gqm|log-error|log-decision]")
        sys.exit(1)

    command = sys.argv[1]
    state = load_state()

    if command == "get":
        print(json.dumps(state, indent=2))
    
    elif command == "set-phase":
        try:
            phase_idx = int(sys.argv[2])
            if 0 <= phase_idx < len(VALID_PHASES):
                state["current_phase"] = phase_idx
                state["history"].append(f"[{datetime.now().isoformat()}] Moved to phase {VALID_PHASES[phase_idx]}")
                save_state(state)
                print(f"Phase updated to: {VALID_PHASES[phase_idx]}")
            else:
                print("Invalid phase index.")
                sys.exit(1)
        except (IndexError, ValueError):
            print("Usage: python state_manager.py set-phase <index>")
            sys.exit(1)

    elif command == "add-task":
        try:
            task = sys.argv[2]
            state["completed_tasks"].append(task)
            save_state(state)
            print(f"Task recorded: {task}")
        except IndexError:
            print("Usage: python state_manager.py add-task <description>")
            sys.exit(1)

    elif command == "set-gqm":
        try:
            goal = sys.argv[2]
            questions = sys.argv[3].split(",")
            state["gqm"] = {
                "goal": goal,
                "questions": [q.strip() for q in questions],
                "metrics": {}
            }
            save_state(state)
            print(f"GQM set for phase {VALID_PHASES[state['current_phase']]}")
        except IndexError:
            print("Usage: python state_manager.py set-gqm <goal> <question1,question2,...>")
            sys.exit(1)

    elif command == "log-error":
        try:
            taxonomy = sys.argv[2]
            if taxonomy not in TAXONOMY_TYPES:
                print(f"Invalid taxonomy. Must be one of: {TAXONOMY_TYPES}")
                sys.exit(1)
            description = sys.argv[3]
            state["error_log"].append({
                "timestamp": datetime.now().isoformat(),
                "taxonomy": taxonomy,
                "description": description
            })
            save_state(state)
            print(f"Error logged under {taxonomy}")
        except IndexError:
            print("Usage: python state_manager.py log-error <taxonomy> <description>")
            sys.exit(1)

    elif command == "log-decision":
        try:
            choice = sys.argv[2]
            alternatives = sys.argv[3].split(",")
            scores = json.loads(sys.argv[4])
            state["decision_log"].append({
                "timestamp": datetime.now().isoformat(),
                "choice": choice,
                "alternatives": [alt.strip() for alt in alternatives],
                "benchmark_scores": scores
            })
            save_state(state)
            print(f"Decision logged: {choice}")
        except (IndexError, json.JSONDecodeError):
            print("Usage: python state_manager.py log-decision <choice> <alt1,alt2> '{\"choice\": 0.8, \"alt1\": 0.6}'")
            sys.exit(1)

if __name__ == "__main__":
    main()
