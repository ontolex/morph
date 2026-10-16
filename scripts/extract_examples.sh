#!/bin/bash

# Regenerates examples/example_N.ttl from the Turtle embedded in each
# `<aside class="example" src="examples/example_N.ttl">` block in index.md.
# The Mermaid diagram for each example is generated from its .ttl file at
# HTML-build time (see expand_tags.py), not here.

python scripts/extract_examples.py
