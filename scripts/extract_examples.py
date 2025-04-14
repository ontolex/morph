in_example_tag = False
in_example = False
example_no = 0
headers = """@prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix lexinfo: <http://www.lexinfo.net/ontology/3.0/lexinfo#> .
@prefix morph: <http://www.w3.org/ns/lemon/morph#> .
@prefix vartrans: <http://www.w3.org/ns/lemon/vartrans#> .
@prefix paralex: <https://www.paralex-standard.org/paralex_ontology.xml#> .
@prefix : <http://www.example.com/#> ."""
example = headers

with open("index.md") as f:
    for line in f.readlines():
        if "<aside class=\"example\"" in line:
            in_example_tag = True
            example_no += 1
        elif in_example_tag and "```turtle" in line:
            in_example = True
        elif in_example and "```" in line:
            in_example = False
            in_example_tag = False
            with open(f"examples/examples{example_no}.ttl", "w") as ex:
                ex.write(example)
            example = headers
        elif in_example:
            example += line

