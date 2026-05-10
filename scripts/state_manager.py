import json
import os
import sys
from datetime import datetime

STATE_FILE = ".auto-dev-state.json"

PHASES = [
    "CONTEXT_ACQUISITION",
    "RISK_ASSESSMENT",
    "SURGICAL_IMPLEMENTATION",
    "INTEGRATION_TESTING",
    "DELIVERY_POSTMORTEM"
]

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {
        "phase_idx": 0,
        "project_id": "DEFAULT",
        "verification_log": [],
        "timestamp": datetime.now().isoformat()
    }

def update_state(phase_idx=None, project_id=None):
    state = load_state()
    if phase_idx is not None:
        state["phase_idx"] = int(phase_idx)
        msg = f"Transitioning to {PHASES[state['phase_idx']]}"
        os.system(f"python3 scripts/visual_terminal.py phase '{msg}'")
    if project_id:
        state["project_id"] = project_id
    
    state["timestamp"] = datetime.now().isoformat()
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def log_verification(result, status="PASS"):
    state = load_state()
    state["verification_log"].append({
        "timestamp": datetime.now().isoformat(),
        "result": result,
        "status": status
    })
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)
    
    color_mode = "success" if status == "PASS" else "error"
    os.system(f"python3 scripts/visual_terminal.py {color_mode} '{result}'")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "set-phase":
        update_state(phase_idx=sys.argv[2])
    elif cmd == "verify":
        log_verification(sys.argv[3], sys.argv[2])
