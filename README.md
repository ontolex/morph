# OntoLex Module for Morphology

The Morphology Module (*morph*) extends the [OntoLex-Lemon](https://ontolex.github.io/ontolex/) model to represent
the morphology of lexical entries in RDF. It covers the segmentation of words into morphs (stems, roots and affixes),
the grammatical meaning these morphs carry, and the rules that relate lexical entries and forms to each other: word
formation rules (derivation and compounding) and inflection rules, including the generation of inflected forms from
inflection classes and paradigms.

The module is developed by the [W3C Ontology-Lexica Community Group](https://www.w3.org/community/ontolex/). Its
namespace is `http://www.w3.org/ns/lemon/morph#` (prefix `morph:`).

The live version of the draft specification is available at https://ontolex.github.io/morph/

## Repository Layout

- `index.md`: the specification, which is the source of both the document and the ontology
- `morph.ttl`: the ontology, extracted from the specification
- `examples/`: the Turtle files of the examples in the specification
- `OntoLex Morph.drawio.svg` / `.png`: the diagram of the model (Figure 1)
- `respec.template`, `expand_tags.py`, `build_ontology.py`, `scripts/`: the build tools
- `data/`: sample data and experiments for agglutinative, fusional and polysynthetic languages and for form generation
- `doc/`, `minutes/`, `minutes_txt/`: background material, reviews and meeting minutes
- `related/`: related vocabularies (including [MMoOn](https://github.com/MMoOn-Project/MMoOn) as a Git submodule)

## Building the Specification

The specification uses [ReSpec](https://respec.org/docs/) and is generated from the Markdown file `index.md`. A GitHub
action builds the specification on every push to `master` and deploys it to https://ontolex.github.io/morph/. It
also runs on every pull request, where it fails if the build or the checks fail.

To build it locally you need [Pandoc](https://pandoc.org/) and the Python packages `beautifulsoup4` and `rdflib`. Run,
from the root directory of the repository:

```bash
pandoc --template respec.template -f markdown-auto_identifiers --wrap=none index.md -o index.html
python3 expand_tags.py index.html index.html
```

`expand_tags.py` expands the shorthand tags in the specification into RDFa and draws the diagram of each example
(as a [Mermaid](https://mermaid.js.org/) flowchart) from its Turtle file.

## Extracting the Ontology

The ontology is encoded in RDFa within the specification. To extract it to `morph.ttl` you also need
[`rapper`](https://librdf.org/raptor/rapper.html) (from `raptor2-utils`). After building `index.html` as above, run:

```bash
rapper -i rdfa index.html -o turtle | python3 build_ontology.py morph
```

Please regenerate and commit `morph.ttl` whenever a change to `index.md` affects the ontology.

## Examples

The listings in `index.md` are the source of the examples. Each example is written in an
`<aside class="example" src="examples/example_N.ttl">` block, and the files in `examples/` are generated from these
listings with:

```bash
python3 scripts/extract_examples.py
```

The GitHub action runs `python3 scripts/extract_examples.py --check` and fails if any file is out of date, so run the
script and commit the result whenever you change an example. To preview the diagram of a single example, run
`python3 scripts/convert_to_mermaid.py examples/example_N.ttl`.

## Google Drive Mirror

Some older material of the group is on Google Drive (see the
[wiki](https://www.w3.org/community/ontolex/wiki/Morphology) for the link) and is only mirrored here, in `minutes/`
and `data/gdrive/`. To update the mirror, run

```bash
bash -e ./sync-gdrive.sh
```

See the notes in `sync-gdrive.sh` for how to configure `rclone`. The script also writes a text export of the minutes
to `minutes_txt/` to make them searchable.

## Contributing

We welcome contributions to the Morphology Module. If you find issues, have suggestions, or want to contribute new
examples, please open an issue or a pull request in this repository. Changes to the specification should follow the
OntoLex style guide.

More information on the module and the work of the group is on the
[wiki](https://www.w3.org/community/ontolex/wiki/Morphology).
