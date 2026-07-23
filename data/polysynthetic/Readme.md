# Polysynthetic languages

note:

- this is christian's original proposal, which makes use of ontolex:otherForm to encode contextual variants of the same morph(eme). note that this modelling makes no claim as to whether morph:Morph and its forms are allomorphs or just notational variants, because there is no formal notion of allomorphy here.
- as the proposal to use forms (of morphs) in the rdfs:Seq of ontolex:Forms caused some controversy, we now provide both ways of modelling to better compare.
	- this directory: discussion and original modelling (including both these variants, sources and more details)
	- `one-morph-with-multiple-forms/`: proposal by christian, ttl only
		- 260 triples
	- `every-form-variant-one-morph/`: proposal by max, ttl only
		- 312 triples (+20%)
		- no linking across form variants of the same morph, yet

## TL/DR

- **FAIL**: *this data* requires modelling of allomorphs as form variants of a single morph. so, we cannot connect forms with their morphological segments, but only with the morphemes 
	- **SUGGESTED REVISION**: make ontolex:Form an rdfs:Seq of ontolex:Forms rather than morph:Morphs (preserve current `morph:contains`)
- **ADDITION**: if data sets or tools require the encoding of allomorphs as individual morphs (which is allowed, but not in line with the resource we looked into here), these variants should be linked by `morph:allomorph` (sub-property of `vartrans:lexicalRel`)
- **MINOR**: lexinfo property for attested/correct, constructed/hypothetical (`*`), and incorrect (`**`) forms
- **MINOR**: add 4th person (obviative) to lexinfo
- **MINOR**: add properties for sbuject and object agreement to lexinfo
- **MINOR**: illustrates usage and need for `morph:baseConstraint` (=> example for documentation, also to show grammatical meaning of morphs used for features of derived forms)
- **MINOR**: illustrates need for `lexinfo:StemMorph`. TODO: add to definition that this should be used for cases in which the canonical form cannot be used as a standalone word (but requires additional markers, e.g., inflectional morphology)
- **MINOR** longer descriptions of allomorphy in guidelines

## Inuktitut

Example: Inuktitut, an Eskimo-Aleut* language from the Eastern Canadian Arctic, official language in Nunavut (Canada). Our analysis is based on the Uqialaut analyzer. Uqailaut is an ad-hoc implementation in Java, but roughly equivalent to an FST implementation (as available for the closely related Kalaallisut language from Western Greenland). Inuktitut poses a number of unique challenges because of its extremely rich morphology. 

* We are aware that the exonym "Eskimo" is considered derogative in Canada, and that "Inuit" is preferred. However, "Inuit" excludes the Yupik languages of Alaska, so that in absence of a better designation, we stay with the traditional term when referring to (features of) the group of languages that includes both Inuit and Yupik.

The Uqailaut Inuktitut data was originally included in the OntoLex-Morph GDrive and migrated to OntoLex-Morph GitHub on 2021-10-06.

## Grammar and Data

Features; agglutination, assimilation, incorporation, polypersonal
agreement, head marking

-   Web demo analyzer (sample output):
    > [[http://www.inuktitutcomputing.ca/Uqailaut/Demo/demoword.php?lang=en&demoword=imiqtarvingmunngauliqhlutik]{.underline}](http://www.inuktitutcomputing.ca/Uqailaut/Demo/demoword.php?lang=en&demoword=imiqtarvingmunngauliqhlutik)

-   Morphological inventory:
    > [[http://www.inuktitutcomputing.ca/Technocrats/ILFT.php#morphology]{.underline}](http://www.inuktitutcomputing.ca/Technocrats/ILFT.php#morphology),
    > [[https://uqausiit.ca/morpheme-list/infix]{.underline}](https://uqausiit.ca/morpheme-list/infix)

-   We consider a single full form, *atausiulugu*.

- **sample**
	- [the word *atausiulugu*](atausiulugu.tsv): Verb feat. incorporation and polypersonal agreement, produced by Uqailaut analyzer. Analyzer doesn't disambiguate, so we need to represent all analyses in a compact way
		- Necessary morphemes and allomorphs from parser: [atausiulugu.morphs.tsv](atausiulugu.morphs.tsv)
		- Root and derivational morphology from Spalding (1998): [atausiulugu.spalding.md](atausiulugu.spalding.md), this is to check whether there is additional information in conventional dictionaries that we might need to add

- **modelling**
	- Uqailaut morph(eme) inventory (for atausiulugu.morphs.tsv)
		- direct OntoLex rendering: [atausiulugu.morph.ttl](atausiulugu.morphs.ttl).
	
			> NOTE: no particular problems, but illustrates `morph:baseConstraint` and treatment of lexinfo gaps)
	
	- selected Spalding information (atausiulugu.spalding.md)
		- direct OntoLex rendering: [atausiulugu.spalding.ttl](atausiulugu.spalding.ttl). Also shows the application of an assimilation (allomorphy) rule. A challenge is to mark whether a word form is complete or not. The current workaround is to append a special symbol in replacements, final `-` for Inuktitut. This works nicely, but it would be more natural to encode this directly as a property of morphs.

	- approaches to model full segmentations using the morpheme inventory under [atausiulugu.ttl](atausiulugu.ttl)

## Modelling challenges

### 1. Allomorphy rules

[atausiulugu.spalding.ttl](atausiulugu.spalding.ttl) shows an assimilation (allomorphy) rule implemented as `morph:Replacement` with capturing groups. No particular difficulties, but the translation of human-readable assimilation rules to regular expressions with capturing groups cannot be automatized.

### 2. Cardinality and type restrictions 

- a `vn` morpheme requires a verb and produces a noun
	- implemented using `morph:baseConstraint` and `morph:grammaticalMeaning`. Here, grammatical meaning represents the result state.

### 3. Distinguish complete and incomplete forms

- verbal derviation morphemes cannot be final
	- **CANNOT** be directly modelled at `morph:Morph`, in atausiulugu.spalding.ttl implemented in `morph:Replacement`, using a special placeholder symbol
	- for derived forms, it can be encoded by identifying them as `lexinfo:StemMorph` (i.e., not an `ontolex:Word`, this would be a complete form, then)
		- **TODO**: put this aspect into the definition of `lexinfo:StemMorph`: "lexinfo:StemMorph is to be used only for morphs that do not represent complete words and that require additional markers (e.g., inflection) in order to occur in natural language."

> NOTE: we may need a representation of incomplete or otherwise special forms in lexinfo, e.g., `lexinfo:constructed` (for constructed, reconstructed or hypothetical forms, similar to `*`), `lexinfo:attested` (default, should only be used in resources that provide attested along with (re)constructed or otherwise non-attested forms), `lexinfo:incorrect` (sometimes, resources provide counterexamples, conventionally marked by `**`). With that information, we may flag all automatically predicted forms as `lexinfo:constructed` and if a resource provides an `lexinfo:attested` form, this overrides the constructed forms (and users can provide a SPARQL filter to do that)


### 4. Incorporation 

Incorporation is usually seen as a process separate from other word formation rules such as compounding or derivation. Incorporation is typical for Inuit and Yupik. The Inuktitut data, however, does not require to differentiate between incorporation and the derivation of nouns from verbs.

Uqailaut examples:

- {si:liq/2nv}
- {u:u/1nv}

read: if applied to a noun, return a verb; number is number of lexical entry for a particular lemma

- implemented using `morph:baseConstraint` and `morph:grammaticalMeaning`. Here, grammatical meaning represents the result state. No particular difficulties.

This is fully equivalent to other cases of derivation:
- verb-to-verb: {si:si/2vv}, {si:siq/1vv}, {u:uq/3vv}
- verb-to-noun: {si:siq/2vn}
- noun-to-noun: {u:ut/2nn}


### 5. Encode ambiguity in derivation

-   Many morphemes are ambiguous
	-   It would be good to have a compact representation where all possible  segmentations are represented in a directed acyclic graph (DAG) rather than as a sequence. If not, we run into a combinatoric explosion, here:
	    -   Given *abcedefg*
	    -   If the sequence *bc* can always be analysed as either *b-c* or *bc*
	    -   And the sequence *def* can always be analysed as either *d-e-f* or *de-f* or *d-ef* or *def*
	    -   And everything else is unambiguous
	    -   Then a there are 2 \* 4 possible morphological analyses, with 52 (!) different morphological segments
	    -   But as a DAG, this can be represented as one path (here using \| to separate possible alternative sub-paths):
	        -   *a-(b-c\|bc)-e-(d-e\|de-f\|de-f\|d-ef\|def)-g*
        -   This requires only 15 morphological segments (and clever compression can reduce that a bit)

- two segmentation modelling options under [atausiulugu.ttl](atausiulugu.ttl)
	- current Seq modelling:
		- FAILS to provide more than one segmentation
			=> this is solved with current WordFormationRelation
		- FAILS to identify individual allomorphs (forms)
			=> **suggested REVISION**: make ontolex:Forms a sequence of ontolex:Forms, then, allomorphs are/can be different forms of the same morph(eme)
					(it is still possible -- and, for other resources, requires --, to model each allomorphic variant as separate morph)
	- current WordFormationRelation:
		- works seamlessly for multiple segmentation, encoding as DAG
		- FALS to identify individual allomorphs (forms)
			=> **OPEN ISSUE**: ignore this problem, in most existing resources, there will be a unique segmentation. if a resource (e.g., a software tool) requires that explicitly, the recommended workaround is to create one morph per allomorph and to use these here.
			=> **suggested REVISION**: add a property `morph:allomorph` as a subproperty of `vartrans:lexicalRel` that connects a morph with its allomorphic variants (if these are represented as individual morphs)
			=> **TODO** longer descriptions of allomorphy in guidelines

# Corpus data (FYI)

Corpus data (CoNLL data, not to be modelled in OntoLex, but the individual morphemes and their combinatorics need to be modelled

\# Hansard

1 Hansard Hansard \_ \_

\# nunavut kanata

1 nunavut nunavut {nunavut:nunavut/1n} {Nunavut}

1 nunavut nunavut {nuna:nuna/1n}{vut:vut/tn-nom-s-1p} {(1) land (2)
country}{nominative: our (one thing to us many) }

1 nunavut nunavut {nuna:nuna/1n}{vut:vut/tn-nom-p-1p} {(1) land (2)
country}{nominative: our (many things to us many) }

2 kanata kanata {kanata:kanata/1n} {Canada}

\# nunavut maligaliurvia

1 nunavut nunavut {nunavut:nunavut/1n} {Nunavut}

1 nunavut nunavut {nuna:nuna/1n}{vut:vut/tn-nom-s-1p} {(1) land (2)
country}{nominative: our (one thing to us many) }

1 nunavut nunavut {nuna:nuna/1n}{vut:vut/tn-nom-p-1p} {(1) land (2)
country}{nominative: our (many things to us many) }

2 maligaliurvia maligaliurvia
{maligaliurvi:maligaliurvik/1n}{a:nga/tn-nom-s-4s} {legislative
assembly}{nominative: his;her;its (one thing, different person) }

2 maligaliurvia maligaliurvia
{maliga:maligaq/1n}{liur:liuq/1nv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{bill}{construction in progress: \'to be building s.t.\' (trans.: for
s.o.)}{place where the action of the verb takes place}{nominative:
his;her;its (one thing, different person) }

2 maligaliurvia maligaliurvia
{maliga:maligaq/1n}{li:li/3nv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{bill}{to build, make something (trans.: for s.o.); with certain words:
find s.t.}{frequentative: many subjects; many objects}{place where the
action of the verb takes place}{nominative: his;her;its (one thing,
different person) }

2 maligaliurvia maligaliurvia
{maliga:maligaq/1n}{li:lik/3nv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{bill}{to give, to provide, to offer, to fetch s.t. (trans.: to
s.o.)}{frequentative: many subjects; many objects}{place where the
action of the verb takes place}{nominative: his;her;its (one thing,
different person) }

2 maligaliurvia maligaliurvia
{maliga:maligaq/1n}{li:lik/2nv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{bill}{to go to; to have gone to; to come to; to find by
chance}{frequentative: many subjects; many objects}{place where the
action of the verb takes place}{nominative: his;her;its (one thing,
different person) }

2 maligaliurvia maligaliurvia
{maliga:maligaq/1n}{li:liq/3nv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{bill}{to go to, toward}{frequentative: many subjects; many
objects}{place where the action of the verb takes place}{nominative:
his;her;its (one thing, different person) }

2 maligaliurvia maligaliurvia
{maliga:maligaq/1n}{li:liq/2nv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{bill}{to provide, supply; to put s.t. (trans.: to, on
s.o.)}{frequentative: many subjects; many objects}{place where the
action of the verb takes place}{nominative: his;her;its (one thing,
different person) }

2 maligaliurvia maligaliurvia
{mali:malik/1v}{ga:gaq/2vv}{li:li/2vv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{(1) to follow (trans. \[-mik\]: s.o. or s.t.) (2) to obey (trans.
\[-mik\]: s.o.)}{frequentative: several times}{to make that s.t. or s.o.
\... (refl.: to become); to make s.t. (trans.: to s.o.)}{frequentative:
many subjects; many objects}{place where the action of the verb takes
place}{nominative: his;her;its (one thing, different person) }

2 maligaliurvia maligaliurvia
{mali:malik/1v}{ga:gaq/1vn}{li:li/3nv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{(1) to follow (trans. \[-mik\]: s.o. or s.t.) (2) to obey (trans.
\[-mik\]: s.o.)}{forms a noun with an inherently passive meaning:
someone/something that one \...}{to build, make something (trans.: for
s.o.); with certain words: find s.t.}{frequentative: many subjects; many
objects}{place where the action of the verb takes place}{nominative:
his;her;its (one thing, different person) }

2 maligaliurvia maligaliurvia
{mali:malik/1v}{ga:gaq/1vn}{li:lik/3nv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{(1) to follow (trans. \[-mik\]: s.o. or s.t.) (2) to obey (trans.
\[-mik\]: s.o.)}{forms a noun with an inherently passive meaning:
someone/something that one \...}{to give, to provide, to offer, to fetch
s.t. (trans.: to s.o.)}{frequentative: many subjects; many
objects}{place where the action of the verb takes place}{nominative:
his;her;its (one thing, different person) }

2 maligaliurvia maligaliurvia
{mali:malik/1v}{ga:gaq/1vn}{li:lik/2nv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{(1) to follow (trans. \[-mik\]: s.o. or s.t.) (2) to obey (trans.
\[-mik\]: s.o.)}{forms a noun with an inherently passive meaning:
someone/something that one \...}{to go to; to have gone to; to come to;
to find by chance}{frequentative: many subjects; many objects}{place
where the action of the verb takes place}{nominative: his;her;its (one
thing, different person) }

2 maligaliurvia maligaliurvia
{mali:malik/1v}{ga:gaq/1vn}{li:liq/3nv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{(1) to follow (trans. \[-mik\]: s.o. or s.t.) (2) to obey (trans.
\[-mik\]: s.o.)}{forms a noun with an inherently passive meaning:
someone/something that one \...}{to go to, toward}{frequentative: many
subjects; many objects}{place where the action of the verb takes
place}{nominative: his;her;its (one thing, different person) }

2 maligaliurvia maligaliurvia
{mali:malik/1v}{ga:gaq/2vv}{li:liq/1vv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{(1) to follow (trans. \[-mik\]: s.o. or s.t.) (2) to obey (trans.
\[-mik\]: s.o.)}{frequentative: several times}{on-going action; present
progressive tense}{frequentative: many subjects; many objects}{place
where the action of the verb takes place}{nominative: his;her;its (one
thing, different person) }

2 maligaliurvia maligaliurvia
{mali:malik/1v}{ga:gaq/1vn}{li:liq/2nv}{ur:uq/3vv}{vi:vik/3vn}{a:nga/tn-nom-s-4s}
{(1) to follow (trans. \[-mik\]: s.o. or s.t.) (2) to obey (trans.
\[-mik\]: s.o.)}{forms a noun with an inherently passive meaning:
someone/something that one \...}{to provide, supply; to put s.t.
(trans.: to, on s.o.)}{frequentative: many subjects; many objects}{place
where the action of the verb takes place}{nominative: his;her;its (one
thing, different person) }
