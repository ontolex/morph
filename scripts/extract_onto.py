import re

print("@prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .")
print("@prefix vartrans: <http://www.w3.org/ns/lemon/vartrans#> .")
print("@prefix morph: <http://www.w3.org/ns/lemon/morph#> .")
print("@prefix owl: <http://www.w3.org/2002/07/owl#> .")
print("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .")
print("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .")
print("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .")
print("")

in_entity = False
first = True

tag_regex = r"<(.*?)>(.*?)</(.*?)>"

def map_urls(u):
    if " or " in u:
        elems = u.split(" or ")
        return "[ owl:unionOf ( " + " ".join([map_urls(e) for e in elems]) + " ) ]"
    else:
        return u

with open("index.md") as f:
    for line in f.readlines():
        if "<div class=\"entity\"" in line:
            in_entity = True
        if in_entity:
            if "</div>" in line:
                in_entity = False
                print(" . \n\n")
                continue
            m = re.match(tag_regex, line)
            if m:
                tag = m.group(1)
                content = m.group(2)

                if tag == "class":
                    print(f"morph:{content} a rdfs:Class ")
                elif tag == "objectProperty":
                    print(f"morph:{content} a owl:ObjectProperty ")
                elif tag == "dataProperty":
                    print(f"morph:{content} a owl:DatatypeProperty ")
                elif tag == "subclass":
                    print(f"; rdfs:subClassOf {content}")
                elif tag == "subproperty":
                    print(f"; rdfs:subPropertyOf {content}")
                elif tag == "domain":
                    print(f"; rdfs:domain {map_urls(content)}")
                elif tag == "range":
                    print(f"; rdfs:range {map_urls(content)}")
            

