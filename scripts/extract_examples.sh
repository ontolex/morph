#!/bin/bash

python scripts/extract_examples.py 

for f in examples/*.ttl
do
    python scripts/convert_to_dot.py $f > ${f/%.ttl/.dot}
    dot -Tpng ${f/%.ttl/.dot} -o ${f/%.ttl/.png}
done
