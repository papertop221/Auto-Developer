import os
import sys

# Professional Minimalist Palette
DIM = "\033[2m"
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
BOLD = "\033[1m"
RESET = "\033[0m"

def render_pro_box(header, body, color=CYAN):
    width = 64
    # Clean header with block character
    print(f"\n{color}█ {BOLD}{header.upper()}{RESET}")
    
    # Minimalist borderless content
    for line in body.split('\n'):
        while len(line) > (width - 4):
            idx = line[:width-4].rfind(' ')
            if idx <= 0: idx = width-4
            print(f"{DIM}│{RESET} {line[:idx]}")
            line = line[idx:].strip()
        print(f"{DIM}│{RESET} {line}")
    print()

def main():
    if len(sys.argv) < 3:
        render_pro_box("auto-developer", "Professional Engineering Suite Active.", BLUE)
        sys.exit(0)

    mode = sys.argv[1]
    msg = sys.argv[2]

    if mode == "phase":
        render_pro_box("phase status", msg, YELLOW)
    elif mode == "success":
        render_pro_box("verification pass", msg, GREEN)
    elif mode == "info":
        render_pro_box("technical note", msg, BLUE)
    elif mode == "error":
        render_pro_box("critical failure", msg, RED)

if __name__ == "__main__":
    main()
