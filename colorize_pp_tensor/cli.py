import sys
import torch
from .printer import colorize_pp_tensor

def main():
    if len(sys.argv) < 2:
        print("Usage: pretty-tensor <comma-separated tensor shape>")
        print("Example: pretty-tensor 2,3,4")
        sys.exit(1)

    try:
        shape = tuple(int(dim) for dim in sys.argv[1].split(','))
        tensor = torch.arange(torch.prod(torch.tensor(shape))).reshape(shape)
    except Exception as e:
        print(f"Error parsing shape or creating tensor: {e}")
        sys.exit(1)

    colorize_pp_tensor(tensor)


if __name__ == "__main__":
    main()
