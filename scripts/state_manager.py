import json
import os
import sys
from datetime import datetime

# Global State Path
STATE_FILE = ".auto-dev-state.json"

PHASES = [
    "Welcome & Blueprint",
    "Technical Groundwork",
    "Surgical Coding",
    "Stress Test & Polish",
    "Grand Reveal"
]

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {"phase": 0, "project": "New Project", "tasks": []}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def set_phase(index, name=None):
    state = load_state()
    state["phase"] = int(index)
    if name: state["project"] = name
    save_state(state)
    
    # Trigger visual feedback
    phase_name = PHASES[int(index)]
    os.system(f"python3 scripts/visual_terminal.py phase 'Phase {index+1}: {phase_name}'")

def add_log(msg, type="info"):
    # Log to a history file for the user
    with open("PROJECT_LOG.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
    
    # Visual feedback
    os.system(f"python3 scripts/visual_terminal.py {type} '{msg}'")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "set-phase":
        set_phase(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    elif cmd == "log":
        add_log(sys.argv[3], sys.argv[2])
