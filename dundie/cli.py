import argparse
from dundie.core import load

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
    print(*globals()[args.subcommand](args.file_path))