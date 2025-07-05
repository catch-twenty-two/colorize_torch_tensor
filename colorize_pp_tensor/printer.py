import torch
import re

RESET = '\033[0m'
FG_BLACK = '\033[38;5;16m'
BG_SCALAR = '\033[48;5;250m'

HIGH_CONTRAST_BG_CODES = [
    208, 51, 220, 127, 190, 160, 33, 201, 50,
    94, 45, 203, 99, 165, 178, 118, 172, 106, 63, 81
]

def bg_color_256(dim):
    return f'\033[48;5;{HIGH_CONTRAST_BG_CODES[dim % len(HIGH_CONTRAST_BG_CODES)]}m'

def color_bracket(bracket, depth, bracket_color_map):
    color = bracket_color_map[depth % len(bracket_color_map)]
    return f"{color}{bracket}{RESET}"

def highlight_tensor_str(tensor_str):
    # Stack to track bracket depth for coloring
    depth = 0
    bracket_color_map = [bg_color_256(i) for i in range(20)]

    # Regex to find brackets or numbers (including negative and decimals)
    token_pattern = re.compile(r'([\[\]])|(-?\d+\.?\d*(e[+-]?\d+)?)')

    parts = []
    idx = 0

    for match in token_pattern.finditer(tensor_str):
        start, end = match.span()
        # Append any intermediate text unchanged (spaces, commas, newlines)
        parts.append(tensor_str[idx:start])

        token = match.group()
        if token == '[':
            parts.append(color_bracket('[', depth, bracket_color_map))
            depth += 1
        elif token == ']':
            depth -= 1
            parts.append(color_bracket(']', depth, bracket_color_map))
        else:
            # It's a scalar number; highlight in grey bg + black fg
            # parts.append(f"{BG_SCALAR}{FG_BLACK}{token}{RESET}")\
            parts.append(f"{token}{RESET}")\

        idx = end

    # Append any trailing text
    parts.append(tensor_str[idx:])

    return "".join(parts)

def colorize_pp_tensor(tensor):
    tensor_repr = repr(tensor)
    colored = highlight_tensor_str(tensor_repr)
    print(colored)

    print("\nKey:")
    for i in range(tensor.ndim):
        color = bg_color_256(i)
        print(f"{color} {RESET} dim-{i}")

if __name__ == "__main__":
    t = torch.arange(24).reshape(2, 3, 4)
    colorize_pp_tensor(t)
