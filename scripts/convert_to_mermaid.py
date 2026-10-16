"""CLI wrapper for manual/local preview of a single example's diagram.

The build itself does not use this script: expand_tags.py calls
mermaid_lib.turtle_to_mermaid() directly for each `<aside src="...">` it
finds, using the same Turtle file the aside displays as its listing.

Usage: python scripts/convert_to_mermaid.py examples/example_N.ttl
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mermaid_lib import turtle_to_mermaid

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        ttl_text = f.read()
    sys.stdout.write(turtle_to_mermaid(ttl_text))
