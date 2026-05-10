import os
import sys
import subprocess

# Professional Terminal Styling
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def render_box(title, text, color=CYAN):
    width = 60
    header = f" {BOLD}{title}{RESET} "
    padding = (width - len(title) - 4) // 2
    
    print(f"\n{color}╭" + "─" * padding + header + "─" * (width - padding - len(title) - 4) + "╮" + RESET)
    
    for line in text.split('\n'):
        # Simple word wrap
        while len(line) > (width - 4):
            space_idx = line[:width-4].rfind(' ')
            idx = space_idx if space_idx > 0 else width-4
            print(f"{color}│{RESET} {line[:idx].ljust(width-4)} {color}│{RESET}")
            line = line[idx:].strip()
        print(f"{color}│{RESET} {line.ljust(width-4)} {color}│{RESET}")
        
    print(f"{color}╰" + "─" * (width - 2) + "╯" + RESET)

def main():
    if len(sys.argv) < 3:
        # Default help
        render_box("AUTO-DEVELOPER", "Ready to build something amazing?")
        sys.exit(0)

    mode = sys.argv[1]
    content = sys.argv[2]

    if mode == "phase":
        render_box("PHASE UPDATE", content, YELLOW)
    elif mode == "success":
        render_box("COMPLETED", content, GREEN)
    elif mode == "info":
        render_box("SYSTEM NOTE", content, BLUE)
    elif mode == "error":
        render_box("ATTENTION", content, RED)

if __name__ == "__main__":
    main()
