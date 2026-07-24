Comments by Sander Stolk
========================

## Ontology morph.ttl

- It's missing an owl:Ontology resource, which should have a label and owl:imports ontolex. (Perhaps reference Linked Open Vocabularies for suitable metadata.)
- There's a unionOf with ontolex:Morph as one of the components, which should surely be morph:Morph
- Would it make sense to have a statement in this model that "ontolex:Affix rdfs:subClassOf morph:Morph" ? Or is it only so in analyses and therefore we would not consider all affixes to be morphs necessarily?
- The documentation states that:
- "This representation does not give the order of the morphs within the word, which is enough for some cases (and even useful when the order may be considered ambiguous, e.g. with infixation). However, for many applications, it is necessary to provide this information. To do so, the morphs can be modelled as an rdf:Seq by means of the rdf:_1, rdf:_2, etc. properties."
- These statements suggests that the model would benefit from adding "morph:consistsOf rdfs:subPropertyOf rdfs:member". After all, the use of rdf:_1 etc would automatically infer rdfs:member, which is pretty much what should also be present when one would not have captured any order.
- The ontology tends to use rdfs:domain for properties for things that are likely better captured as owl:Restriction's on the classes. By having used rdfs:domain, the property morph:example for instance cannot be used with smth such as instances of morph:Replacement without entailing those must be instances of morph:Rule too. The properties morph:source and morph:target also can not be reused for anything other than RegexReplacement instances without indicating they must be RegexReplacements too. I doubt such inferences are intended, but that they serve more as tips for the classes: "please use this property with this class". That would be best captured with owl:Restriction instead, imo. (Or SHACL shapes, but preferably shapes should be served separately from the ontology they work on.)



## Morph documentation

### GENERAL

- No list of prefixes & namespaces ?
- No list of references?

### SECTION "1. Introduction"

- "the decomposition of lexical entries encompasses lexical entries, components, [..]"
- > Components are always part of a decomposition, so I assume here a specific kind of component is meant. Specificity would help here. Additionally, is the list of possible components here complete? If not, then consider replacing "and" before the last item with a comma.
- "However, a lexical entry can NEVER be composed of a form!"
- > Perhaps best to rephrase (i.e., any number of forms), and mention how forms are related to LexicalEntry instead, perhaps between brackets?
- "The morphology module aims at fulfilling two modelling purposes: Stating elements that are involved in the decomposition of lexical entries and forms."
- > It would be great to have explicitly mention that 'lexical entry' and 'form' come from Ontolex core, possibly with links to the definitions, so that readers can quickly grasp that these terms were already established/defined elsewhere and here the focus is on expanding on those terms. On a minor, stylistic note: the unnumbered bullets here do not appear indented to me, even though they should be.
- Figure 1
- > The grey used to distinguish Ontolex core terminology from that of Morph could be quite a lot darker. Imo it is hardly visible as it is. Additionally, it would be good to mention the legend (e.g. stating it follows UML + what the grey means) either as part of the caption or in the paragraph just below the figure.

### SECTION "2. Morphological Segments"

- "A free morph may be a single concept such as “tea” or “pot” in “teapots”, while the plural suffix “-s” is a bound morph."
- > Perhaps shuffle around to have the same pattern in both clauses of free/bound vs example (e.g., ".., while a bound morph may be the plural suffix -s")
- Example 3
- > Introduces boxes with "n_dfb1" and "n_dfb2", which are rather cryptic. From the Turtle I see these are blank nodes, but the Turtle doesn't show those labels (somewhat understandably). I'd encourage either literally leaving the boxes blank in the figure, to represent blank nodes, or finding a better naming (e.g., "bnode1", "bnode2") and possibly adding those names as comments to their corresponding Turtle lines (i.e.,

    morph:grammaticalMeaning [ #bnode1
        lexinfo:number lexinfo:plural ;
    ] ;")
    
"Typically, the bundles will be expressed as blank nodes."  and later  "In practice, it might be better to define instances for common morphological meanings and reuse these objects."
- > So which is it? Isn't reuse always the better option, or is it expected that most morphological meanings are not that reusable?

### SECTION "3. Morphological Rules."

- "The target can use backreferences (\1) to refer to the captured groups in the source string."
- > Please do use dollar sign here (e.g., '$1'), for compatibility with SPARQL. Backslash does not work. See example queries below:
        https://yasgui.triply.cc/#query=SELECT%20*%20WHERE%20%7B%0A%20%20BIND%20(%22laufen%22%20AS%20%3Fword)%20.%0A%20%20BIND%20(%22%5E(.*)en%24%22%20AS%20%3Fsource)%20.%0A%20%20BIND%20(%22ge%5C%5C1t%22%20AS%20%3Ftarget)%20.%0A%20%20BIND%20(REPLACE(%3Fword%2C%20%3Fsource%2C%20%3Ftarget)%20AS%20%3FwordPerfect)%20.%0A%7D&endpoint=https%3A%2F%2Fdbpedia.org%2Fsparql&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table
        https://yasgui.triply.cc/#query=SELECT%20*%20WHERE%20%7B%0A%20%20BIND%20(%22laufen%22%20AS%20%3Fword)%20.%0A%20%20BIND%20(%22%5E(.*)en%24%22%20AS%20%3Fsource)%20.%0A%20%20BIND%20(%22ge%241t%22%20AS%20%3Ftarget)%20.%0A%20%20BIND%20(REPLACE(%3Fword%2C%20%3Fsource%2C%20%3Ftarget)%20AS%20%3FwordPerfect)%20.%0A%7D&endpoint=https%3A%2F%2Fdbpedia.org%2Fsparql&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table

- "We recommend adding this property to generated items".
- > The property morph:involves currently goes from Rules to Morphs, though. Is that desired or is it best to revert the direction?  I assume the Rule is not generated in e.g. Example 10, but the :ge there is. Only at Example 12 do I see that that it's meant differently and that the phrasing in the documentation was rather misleading. I recommend rephrasing slightly, e.g. from the above quoted line (and lines like it!), to "We recommend adding this property to items that the Rule would generate when used/applied."


Ilan Kernerman Comments
=======================

Add “irregular”:
- In traditional print dictionaries, irregular morphological information is provided in abbreviated terms ... language;

Add “of”:
- The kind of elements of which a lexical entry can consist of should

Add “inflected”:
- NEVER be composed of an inflected form!

John McCrae Comments
====================

- The figure and example numbers are not synced.
- The figures are drawn with GraphViz and look a bit ugly, it would be better to use Mermaid to draw them instead.
- The base type property is a datatype property, but refers to a fixed taxonomy of objects. It would make much more sense for this to be an object property and an inventory of possible values stored in LexInfo.

Matteo Pelligrini Comments
==========================


## Section 1

"The RDF file with the OntoLex lemon lexicography module can be found at http://www.w3.org/ns/lemon/morph."
> lemon morphology module

"Morphological decomposition on the lexical entry level.
The kind of elements of which a lexical entry can consist should be as non-restrictive as possible, i.e., the decomposition of lexical entries encompasses lexical entries, components, derivational affixes, inflectional affixes, stems, roots and zero morphs. However, a lexical entry can NEVER be composed of a form!": While this is in principle completely reasonable, I find it contradictory with the fact that the domain of morph:consistsOf is currently stated to be ontolex:Form (see below) - so instances LexicalyEntrie do not technically consist of anything in terms of our modelling. I agree with the modelling choice, because lexical entries are more abstract entities that are not directly segmentable, but then I think it would be better to rephrase this section to avoid confusion.

## Section 2

"Elements of which a form can consist of roots, stems, inflectional affixes and zero morphs." > Forms can also consist of derivational affixes and non-zero morphs, so I would drop the "inflectional" and "zero".

"Morphs are the basic building blocks within the module that represent a single indivisible unit of meaning or grammatical function." I would drop "indivisible" to match the definition (and at least stems are often divisible, indeed)

"The property, ‘consists of’, relates": drop commas and single quotes? (same in many other places, check throughout)

"The class grammatical meaning is used to gloss information associated with the morph" > "The class grammatical meaning is used to gloss information associated with the morph, form or rule" (for consistency with what we state later)

Example 5/Figure 6: why is there "Synset" in the figure (it is not in the underlying .ttl)

## Section 3

"“Tabular” value of a morpheme must be stored in a RDFS label" > Not fully clear what is meant by "tabular". Perhaps reformulate?

naming of the property morph:example: since in Ontolex 2.0 there will also be the property ontolex:example, is it worth distinguishing this in the naming, e.g. morph:ruleExample? Or perhaps we might consider dropping the restriction on the domain of ontolex:example and just use ontolex:example for rules too?

"A source is a string which is used as a basis for the substitution." > "A source is a string pattern which is used as a basis for the substitution." (for consistency with the definition below)

## Section 4

"An inflection class is a group of lexemes that share the same pattern of inflected forms." > "An inflection class is a group of lexemes that share the same pattern of inflectional behaviour."

"In this definition, we assume that we have one lexical entry for each stem variant so that an inflection rule whose base type doesn’t match will not fire if its lexical entry doesn’t fire.": this is unclear to me, why would we have one *lexical entry* for each stem variant?

## Section 5

"As a consequence, vartrans properties are also used to link lexical entries to the relations holding between them: specifically, each word formation relation is linked through source to its base(s) and through target to the derivative." : Correct links: they currently point to morph:source and morph:target, but here we are referring to vartrans:source and vartrans:target. Same in the definition below.

Language tags are often missing in the string patterns of morph:target in many examples; check and correct throughout.

"E.g., for the verb meaning ‘to write’, we have: - citation form of the verb: scribo (displaying present stem scrib-) - supine: scriptum (displaying third stem script-) - agent and action nouns: script-or, script-io.": fix .md formatting of bullet point list

I would also like to add a comment on John's observation that 

>>>The base type property is a datatype property, but refers to a fixed taxonomy of objects. It would make much more sense for this to be an object property and an inventory of possible values stored in LexInfo.

I don' think this can be reduced to a set of predefined closed values. While in the Latin example provided there is a correspondence with meaning classes, in many other cases ths will just be an index to group forms that share the same stem in a given language, and those sets are often completely arbitrary and not reusable across languages.
