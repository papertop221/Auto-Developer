import sys

# ANSI Colors for a high-tech look
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_box(title, message, color=CYAN):
    width = 60
    print(f"\n{color}╭" + "─" * (width-2) + "╮" + RESET)
    print(f"{color}│ {BOLD}{title.ljust(width-4)}{RESET}{color} │" + RESET)
    print(f"{color}├" + "─" * (width-2) + "┤" + RESET)
    for line in message.split('\n'):
        while len(line) > (width-4):
            print(f"{color}│ {line[:width-4]} │{RESET}")
            line = line[width-4:]
        print(f"{color}│ {line.ljust(width-4)} │{RESET}")
    print(f"{color}╰" + "─" * (width-2) + "╯" + RESET)

def main():
    if len(sys.argv) < 3:
        print("Usage: python visual_terminal.py [info|success|error|phase] 'message'")
        sys.exit(1)

    tag = sys.argv[1]
    msg = sys.argv[2]

    if tag == "info":
        print_box("SYSTEM INFO", msg, BLUE)
    elif tag == "success":
        print_box("SUCCESS", msg, GREEN)
    elif tag == "error":
        print_box("CRITICAL ERROR", msg, RED)
    elif tag == "phase":
        print_box("SDLC PHASE UPDATE", msg, YELLOW)

if __name__ == "__main__":
    main()
