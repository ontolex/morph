import rdflib
from rdflib import Graph, Literal, URIRef
import argparse
import sys

NAMESPACES = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ontolex": "http://www.w3.org/ns/lemon/ontolex#",
    "synsem": "http://www.w3.org/ns/lemon/synsem#",
    "decomp": "http://www.w3.org/ns/lemon/decomp#",
    "vartrans": "http://www.w3.org/ns/lemon/vartrans#",
    "lime": "http://www.w3.org/ns/lemon/lime#",
    "morph": "http://www.w3.org/ns/lemon/morph#",
    "frac": "http://example.org/frac#"
    }

def convert_turtle(input_data, base_url, custom_namespaces=NAMESPACES):
    # 1. Initialize the graph and parse RDF
    g = Graph()
    g.parse(data=input_data, format="turtle", publicID=base_url)

    # 2. Create a new graph for the cleaned output
    cleaned_g = Graph()

    # 3. Bind custom namespaces
    if custom_namespaces:
        for prefix, uri in custom_namespaces.items():
            cleaned_g.bind(prefix, URIRef(uri))

    # 4. Iterate through triples and strip whitespace from Literals
    for s, p, o in g:
        if isinstance(o, Literal):
            # Remove leading/trailing whitespace from the string value
            cleaned_value = str(o).strip()
            # Remove any tags like [=text=]
            cleaned_value = cleaned_value.replace("[=", "").replace("=]", "")
            # Recreate the Literal with original datatype/language tag
            new_o = Literal(cleaned_value, lang=o.language, datatype=o.datatype)
            cleaned_g.add((s, p, new_o))
        else:
            # Keep URIs and Blank Nodes as they are
            cleaned_g.add((s, p, o))

    # 5. Serialize to Turtle
    return cleaned_g.serialize(format="turtle")

if __name__ == "__main__":
    # Run as 
    #    rapper -i rdfa -o turtle index.html | python build_ontology.py module_name
    parser = argparse.ArgumentParser(description="Convert RDFa to Turtle with cleaned literals.")
    parser.add_argument("module", help="The name of the module to convert.")

    base_url = f"https://www.w3.org/ns/lemon/{parser.parse_args().module}#"
    output_file = f"{parser.parse_args().module}.ttl"

    args = parser.parse_args()

    # Read file from STDIN
    input_data = sys.stdin.read()

    # Convert RDFa to Turtle
    turtle_output = convert_turtle(input_data, base_url)

    # Write output to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(turtle_output)
