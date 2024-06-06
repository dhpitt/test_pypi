#try:                                                                                                                                                                                                         
#    from setuptools import setup, find_packages
#except ImportError:
#    from distutils.core import setup, find_packages

import argparse
import re
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument(
        "--version",
        type=str,
        required=True
        )

if __name__ == "__main__":
    args = parser.parse_args()
    print(f"Releasing v{args.version}")
