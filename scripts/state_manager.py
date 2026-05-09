import json
import os
import sys

STATE_FILE = ".auto-dev-state.json"

VALID_PHASES = [
    "0: Recall",
    "1: Research",
    "2: Requirements",
    "3: Design",
    "4: Implementation",
    "5: Validation",
    "6: Infrastructure",
    "7: Sustainability",
    "8: Evolution"
]

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"current_phase": 0, "completed_tasks": [], "history": []}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def main():
    if len(sys.argv) < 2:
        print("Usage: python state_manager.py [get|set-phase|add-task]")
        sys.exit(1)

    command = sys.argv[1]
    state = load_state()

    if command == "get":
        print(json.dumps(state, indent=2))
    
    elif command == "set-phase":
        phase_idx = int(sys.argv[2])
        if 0 <= phase_idx < len(VALID_PHASES):
            state["current_phase"] = phase_idx
            state["history"].append(f"Moved to phase {VALID_PHASES[phase_idx]}")
            save_state(state)
            print(f"Phase updated to: {VALID_PHASES[phase_idx]}")
        else:
            print("Invalid phase index.")
            sys.exit(1)

    elif command == "add-task":
        task = sys.argv[2]
        state["completed_tasks"].append(task)
        save_state(state)
        print(f"Task recorded: {task}")

if __name__ == "__main__":
    main()
