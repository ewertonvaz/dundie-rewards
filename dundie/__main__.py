import argparse

def load(file_path):
    try:
      with open(file_path) as file_:
        for line in file_:
          print(line.strip())
    except FileNotFoundError as e:
       print(f"File not found {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Dunder Muflin Rewards CLI",
        epilog="Enjoy and use with caution"
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="Thr subcommand to run",
        default='help',
        choices=('load', 'show', 'add', 'send')
    )
    parser.add_argument(
        "file_path",
        type=str,
        default=None,
        help="Path to file which will be loaded"
    )
    args = parser.parse_args()
    globals()[args.subcommand](args.file_path)

if __name__ == "__main__":
    main()