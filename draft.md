# OntoLex-Morph definitions

(use this for drafting text fragments, the HTML template is under [index.html](index.html) -- but this is empty)

When given and unless marked otherwise, definitions follow the wording of [2019-12-19](https://docs.google.com/document/d/1wybx2_U0EcqmefRRiAABha-cFII6H2rZBtlgTcjLYjg/edit?usp=sharing), resp., the [eLex -2019 paper](https://elex.link/elex2019/wp-content/uploads/2019/09/eLex_2019_33.pdf)

Current diagram under [doc/diagrams](doc/diagrams).

## Acknowledgements

editors (= past and present telco moderators, alph.; please double-check):
- Christian Chiarcos (since 2022)
- Maxim Ionov (2018-2023)
- Bettina Klimek (2018-2022)

contributors (alph, **incomplete/please add yourself/people you remember to have contributed**):
- Julia Bosque-Gil (2018-2022)
- Christian Chiarcos (since 2018)
- Thierry Declerck
- Jesse De Does (2019-2020)
- Katrien Depuydt (2019-2020)
- Katerina Gkirtzou
- Maxim Ionov (since 2018)
- Fahad Khan
- Bettina Klimek (2018-2022)
- Penny Labropoulou
- John P. McCrae (since 2018)
- Matteo Pellegrini
- Stefania Racioppa
- James K. Tauber

## Contents
- [Purpose and Scope](#purpose-and-scope)
- [Morphological Segments](#morphological-segments)
  * [morph:Morph](#morph-morph)
  * [morph:GrammaticalMeaning](#morph-grammaticalmeaning)
  * [morph:morphophonologicalRelation](#morph-morphophonologicalrelation)
  * [morph:baseForm](#morph-baseform)
- [Morphological Rules](#morphological-rules)
  * [morph:example](#morph-example)
  * [morph:Replacement](#morph-replacement)
- [Inflection](#inflection)
  * [morph:Paradigm](#morph-paradigm)
  * [morph:InflectionType](#morph-inflectiontype)
  * [morph:InflectionRule](#morph-inflectionrule)
  * [morph:baseType](#morph-baseType)
- [Word Formation](#word-formation)
  * [morph:WordFormationRule](#morph-wordformationrule)
  * [morph:WordFormationRelation](#morph-wordformationrelation)

## Purpose and Scope

Morphology is a vital and, in many languages, very sophisticated part of language, and  
as such it has been an important part of the work of lexicographers. In the traditional  
print form, morphological information is provided in brief abbreviated terms that can  
only be deciphered with significant knowledge of the language, however with the  
transformation  of  the  dictionary  to  an  electronic  resource  a  re-imagining  of  the  
morphology information in a dictionary is certainly due.

The morphology module aims at fulfilling two modelling purposes:

1. Stating elements that are involved in the decomposition of lexical entries and forms.
	- Morphological decomposition on the lexical entry level.
	> scope: The kind of elements of which a lexical entry can consist should be as non-restrictive as possible. I.e. The decomposition of lexical entries encompass lexical entries, components, derivational affixes, inflectional affixes, stems, roots and zero morphs. However, a lexical entry can NEVER be composed of a form!

	- Morphological decomposition on the form level.

	> scope: Elements of which a form can consist include roots, stems, inflectional affixes and zero morphs. A form can NEVER be decomposed into lexical entries (including ontolex:Affix), components and forms.

MP: should this be rephrased? Now Morph is a subclass of ontolex:LexicalEntry, and Forms can actually be decomposed into Morphs, and also into Forms

2. Enabling the representation of building patterns that are involved in the formation of lexical entries and forms.
	- Representation of decompositional building patterns for lexical entries.
	- Representation of decompositional building patterns for forms.

A fine-grained description of phonological and morphophonological processes that are  involved in any kind of stem or word formation on the phoneme level is excluded and not representable with this Morphology Module. Only the elements  between the lexical entry and the morph levels will be covered. It is possible, however, that such information may be addressed in future OntoLex modules.

The OntoLex-Morph module aims to be adequate for both traditional dictionary content (which contains only abbreviated about morphological rules and paradigms, often organized in appendices) and structured computational data (morphological dictionaries) as used in Language Technology, with the goal of making resources from one community more accessible to the other.

## Overall structure

OntoLex-Morph is designed to account for

- morphological inflection, derivation and compounding,
- languages with fusional or agglutinating morphology,
- the morphological structure of any given form or lexeme (extensional morphology, morphological segments),
- morphemes, rules and selectional constraints associated with them 
- both the structural and the semantic aspects of morphemes and rules,
- various data sources, including, but not limited to lexical resources, inflection tables and computational morphologies

OntoLex-Morph was intended for (but is not limited to) the following primary use cases:

- formalize morphological rules to generate context-adequate labels for and human-language descriptions from ontologies and knowledge graphs
- provide a machine-readable view on morphological data (examples, rules) as found in grammars, text books and dictionaries
- formalize computational morphologies in an interoperable and standard way so that they can be more easily ported between different implementations
- represent morphological relations between lexical entries and forms as a knowledge graph
- complement static dictionaries with dynamic rules to generate possible surface forms
- more easily combine any of these resources with each other and other lexical datasets (as provided in OntoLex)

At its core, OntoLex-Morph operates with three main classes:

- *morph* formalizes the morphological segmentation of lexical entries and forms.
- *rule* formalizes the morphological rules that constitute lexical entries and forms from underlying base forms.
- *grammatical meaning* formalizes semantic and morphosyntactic features of and constraints on morphs and rules.

They are related with each other and with OntoLex in the following way:

- A morph is a lexical entry in the sense of OntoLex. It involves a set of lexical or base forms and a set of meanings (senses). For dependent morphs that can only be characterized by their grammatical meaning, the set of senses can be empty.
- A rule typically *involves* a morph whose application to a given base form is represented by the rule.
- A morph, a rule or the `ontolex:Form` that results from the application of these to a base form can have a *grammatical meaning*. 
- The grammatical meaning is understood as a feature bundle that describes morphosyntactic, morphological or semantic features of the resulting form. It can be elucidated by Lexinfo properties (for morphosyntactic features) or OntoLex lexical concepts (for semantic constraints), but this is not obligatory.
- A morph or a rule can specificy necessary conditions for their application to a particular base form as a *base constraint*. The base constraint is formalized as a grammatical meaning object. By comparing a base constraint with the grammatical meaning of a base, an implementing system should be able to validate the applicability of a rule or morph to that base.

Individual morphological processes (derivation, compounding, inflection) and their relation to lexical entries and forms are represented by designated subclasses of `ontolex:Rule` as described below.

> Limitations: OntoLex-Morph is designed with a focus on deep morphology. Morphophonological rules *can* be modelled with OntoLex-Morph to a certain extent, but we expect phenomena such as assimilation, dissimilation and morphological "Level-2" rules to be more adequately handled by a separate vocabulary specialized in surface generation (transcription, text-to-speech, morphophonology).

## Morphological Segments

### morph:Morph

> ------
> Class **morph:Morph** is a subclass of ontolex:LexicalEntry that represents a concrete primitive element of  
morphological analysis.
>
> -------

MP: morph:Morph can actually be not concrete - if used for an abstract morpheme, see below - and not primitive - if we use it for complex stems. Perhaps we can define it as "any element of morphological analysis below the word level"?

Notes:
- can carry `lexinfo:termElement` (for what?)
- can consist of other morphs
- the model is agnostic as to whether this represents a morpheme or one of its allomorphs, but as a lexical entry
(MP: it might be confusing to have a class called "Morph" that can be used also for morphemes?)
- grammaticalMeaning: glossing information associated with the morph
- baseConstraint: (for affixes) contraints on the elements that this morph can be applied to
- subclasses `ontolex:Affix`, RootMorph, StemMorph, TransfixMorph, SimulfixMorph, ZeroMorph

> ----
> DEPRECATED Class **morph:RootMorph** identifies morph:Morphs that constitute the  semantic nucleus  of a stem. A root morph cannot be further segmented and  is often not specified for a part of speech.
> subClassOf: morph:Morph
>
> ---

> ---
> DEPRECATED Class **morph:StemMorph** identifies  morph:Morphs to which inflectional  marking applies.
> subClassOf: morph:Morph
>
> ---

> Note: we do not define affix (a bound segmental morph), but instead, `ontolex:Affix` is defined as a subclass of `morph:Morph`.

>---
> DEPRECATED Class **morph:TransfixMorph** is a discontinous `ontolex:Affix`
> subClassOf: ontolex:Affix, morph:Morph
>  
>  ---
> ---
> DEPRECATED Class **morph:SimulfixMorph**: A simulfix is a bound morph that entails a   change or replacement of vowels or consonants  (usually vowels) which changes the meaning of   a word, e.g.  eat  in past tense becomes  ate.
> subClassOf: ontolex:Affix, morph:Morph
>  
>  ---

> ---
> DEPRECATED Class **morph:ZeroMorph**: A morph that that corresponds to no overt   form,  i.e.  orthographic  or  phonetic  representation
> subClassOf: ontolex:Affix, morph:Morph
>  
>  ---

April 2022: morph subclasses deprecated and moved to [LexInfo](https://github.com/ontolex/lexinfo/pull/29). Note that lexinfo does not yet reference `morph:Morph`, but only `ontolex:Affix` and `ontolex:LexicalEntry`, but that should be changed when publishing OntoLex-Morph. Also note that the LexInfo definitions should be consolidated with those in this document.

> ------
> Property **morph:consistsOf** states  into  which  Morph resources a Form resource can  be segmented.
> Domain: ontolex:Form, morph:Morph
> Range: ontolex:Form, morph:Morph
>
>-----

Note: this is the eLex-2019 definition, but now we have consists of between morphs and between forms, too

Note: we still have no way to encode the order of morphemes.  We can model forms and morphs as an aggregate (here: `rdf:List` ?).

MP: If morph is a primitive, why it can consist of other morphs? see note above on the definition of morph

### morph:GrammaticalMeaning

> ------
> Class **morph:GrammaticalMeaning**: a grammatical feature that is assigned to a form or morph and corresponds to the value this has with respect to a grammatical category (e.g., value 'nominative' for 'case', 'singular' for 'number', etc.); it can also be a set of features in the case of forms or morphs characterised by a combination of features (for fusional languages)
> MP: Class **morph:GrammaticalMeaning** can be used to represent (bundles of) values of different morpho-syntactic properties expressed by a form or morph
>
> -------

Notes:
- should use lexinfo resources or instances with `rdfs:label`
- can represent *either* an individual feature or a feature bundle

> ------
> property **morph:grammaticalMeaning** assigns a grammatical  meaning to a morph resource or a form or a rule
> domain: ontolex:Form or morph:Morph or morph:Rule
> range: morph:GrammaticalMeaning
> -------

Discussion/History:

- the extension to forms was introduced 2022-02-23 per request from Penny and Matteo for more conveniently providing re-usable and directly indexable "feature bundles".
- the eLex-2019 draft had `morph:meaning` in a comparable function, but with Morph being subclass of LexicalEntry, this role is taken over by `ontolex:sense`.
- in spring 2022, it was requested by Penny and Katerina to make this a property of `morph:InflectionRule` as a short-hand for `morph:involves/morph:grammaticalMeaning`.
- as of 2022-10-19, it was agreed to attach this property also to `morph:Rule`. For circumstances in which no explicit morph can be provided (but only a rule), e.g., because a resource comes without an explicit notion of morph(eme)s, there would not be a way to express the meaning or function of that morpheme, otherwise.
- question (CC, 2022-10-24): do we need this for `morph:InflectionType` ? This would be useful to express that a certain "slot" contains information of a particular kind, e.g., morphological gender or morphological number. Right now, this information is implicit (in the inflection rules assigned to a particular inflection type).

> ------
> property **morph:baseConstraint** defines the grammatical characteristics of the stem or base that a derivational or inflectional morpheme needs to comply in order to be used in ontolex:Rule
> domain: ontolex:Morph or ontolex:Rule
> -------

For example, an element for nominal inflection can only be applied to nouns, and derivational affixes can have similar constraints. Note that such information is not applicable to an `ontolex:Form` because this describes only the result of the application of a rule or the addition of a particular form.

Discussion/History:
- CC 2022-10-24: by analogy with morph:grammaticalMeaning, this property should also be applicable to rules to specify necessary preconditions.

### morph:baseForm
> ----
> Property **baseForm** is an `ontolex:lexicalForm` property that indicates the morphological base form of a lexical entry
> Domain: `ontolex:Word` (not lexical entry!)
>  (MP: why not lexical entry?)
> Range: `ontolex:Form`
>  
>  ---

> ----
> MP: Property **baseForm** is an `ontolex:lexicalForm` property that indicates the form (or morph? see below) that is taken as base by inflection or derivation rules to generate other forms.
>  
>  ---


This property is necessary in cases in which inflection or derivation relations do not take the canonical form as their basis, but a different one. One example is German verbal inflection (e.g., for `gehen` "to go"), where the canonical form (`gehen`, infinitive) is derived from the base form (`geh-`, stem) by means of a suffix (`-en`, infinitive marker), like other inflected forms (`geh`, `gehst`, `geht` "I/you go; he/she/it goes").

MP: given this usage example, shouldn't baseForm also have morph:Morph in its range? The German base geh- is a stem rather than a form

## Morphological Rules

> ------
> [deprecated] Class **morph:Rule**  contains necessary information to add one morpheme to a single word form. It must contain either morph:example or morph:replacement (or both). “Tabular” value of a morpheme must be stored in rdfs:label (e.g. “-s”@en for usual PL in English)
>
> -------

Note: This class was in the Dec 2019 draft, but before Feb 2022, this class had been abandoned from diagram for visual reasons, it is a superclass of `morph:WordFormationRule` and `morph:InflectionRule` and defined as the domain of the properties `morph:replacement` and `morph:example`. Its deletion is to be reassessed, as this was for visual reasons only. Anyway, any information about both kinds of rules should go into this section.

Note: This class was originally introduced as `morph:MorphologicalPattern`: The  morphological  pattern states  the  inflectional,  derivational  or  compositional   building pattern that applies to a lexical entry. (eLex-2019)

### morph:example

> ----
> property **morph:example**: A single generated form that was generated using this rule
> Domain: morph:WordFormationRule or morph:InflectionRule
> Range: string literal
>
> ----

### morph:Replacement

> ----
> property **morph:replacement** states the replacement pattern that is involved in a morphological rule for the generation of a word
> MP: property **morph:replacement** links an InflectionRule or WordFormationRule to the Replacement it consists of.
> Domain: morph:WordFormationRule or morph:InflectionRule
> Range: morph:Replacement
>
> ----

note:
- Until 2022-02-22, this was incorrectly shown in diagram as datatpe property

> ---
> class **morph:Replacement**: An operation involving a source string and the target string that replaces it in order to generate a word according to a word formation rule
> MP: class **morph:Replacement** represents the modification that is performed by an InflectionRule or WordFormationRule on the form it takes as base.
>
> ---

processing analogy: replacement operations with regular expressions as in Perl or Sed.

> ---
> MP: datatype property **morph:source** is used to express the string that is replaced by the target string in a morph:Replacement.
> domain: morph:Replacement
> range: string literal
>
> ----

> ---
> MP: datatype property **morph:target** is used to express the string that replaces the source string in a morph:Replacement.
> domain: morph:Replacement
> range: string literal
>
> ----

As an example, a simple replacement operation would be concatenation, i.e., retrieve the baseForm (or canonicalForm, if no baseForm provided), check that it has the same stem type as the rule (if applicable), then append an affix to the written representation of the baseForm.

> Note: Unless specified otherwise (in the documentation of a resource), implementations SHOULD provide NFD-normalized Unicode strings for `morph:source` and `morph:target`, so that diacritics are separated from the base character as combining characters. This is a best practice that simplifies the writing of rules in many cases, as diacritic and base character can be manipulated independently from each other.

## Inflection

### morph:Paradigm

> --------------------
> Class **morph:Paradigm** represents a theoretically motivated type of declension, e.g.
> -   “a” stem declension in Latin
> -   First declension in Russian
>
> May contain metadata information about this type of declension.
>
> -----------

MP: not only declension, also conjugation. My proposal for a definition would be "the inflection class to which a LexicalEntry belongs/is assigned". 
This raises the question of why this is not called morph:InflectionClass, if that's what it is. A "paradigm" is rather a set of inflected wordforms: but as stated in the note below, morph:Paradigm is NOT that anymore

Book analogy: a full paradigm table with possible allomorphy/alternative variants

Note: eLex-2019: `morph:InflectionalParadigm`: A structured set of inflected forms according  
to specific grammatical parameters. This is now not a set of inflected forms but a set of inflection types that are linked with the respective forms.

>--------
> property **morph:paradigm**: A link to the paradigm to which an inflection type belongs (or is part of)(eLex-2019: assigns a form to an inflectional paradigm) (eLex-2019: assigns a form to an inflectional paradigm)
> Domain: morph:InflectionType
> Range: morph:Paradigm
>
> ---

Note: the link between paradigm and lexical entries is not defined in OntoLex-Morph, but modelled using `ontolex:morphologicalPattern`.

### morph:InflectionType

> ----------
> Class **morph:InflectionType**  represents a single slot for all values of a grammatical category or, in the case of bundles of grammatical categories, for all combinations of values thereof
>
> --------
>
Book analogy: a column from a paradigm table without allomorphy/alternative variants for just a single morpheme

Note: for fusional languages, the inflection type may be associated, for instance, with a combination of gender, number and case, as in the example of Greek nouns, while for agglutinative languages, each inflection type is associated with a single grammatical category (e.g. all values of case)

> -----
> property **morph:inflectionType** assigns an inflectional  pattern of  a form as belonging to a  morphological pattern  of  a  lexical  entry [eLex-2019 definition for `belongsToMorphPattern`, to be updated]
> Domain: morph:Rule
> Range: morph:InflectionType
>
> -----


> ---
> property **morph:next** links two consecutive inflection types (“slots”), e.g. number and case in Finnish
> Domain: morph:InflectionType
> Range: morph:InflectionType
>
>---

### morph:InflectionRule

> ------
> MP: Class **morph:InflectionRule** represents the generation of a form of a LexicalEntry from another form of that LexicalEntry.
>
> -------

Note: originally, we had the class Rule which contains necessary information to add one morpheme to a single word form. It must contain either morph:example or morph:replacement (or both). “Tabular” value of a morpheme must be stored in rdfs:label (e.g. “-s”@en for usual PL in English)

> ---
> DEPRECATED property **morph:inflects**: Property to link an inflection rule with the (abstract representation of the) morph(s) involved in the application of this particular rule.

> Domain: morph:InflectionRule
> Range: ontolex:Morph
>
> ---

Note: this is deprecated in favor of merging it with the analoguous `morph:involves` for derivation morphemes as decided telco 2022-04-20.


### morph:baseType

> ----
> Datatype property **morph:baseType** is used for coindexing a base, an inflection rule and the forms generated by the rule from the respective base in cases in which the inflectional paradigm of a single lexical entry involves bases, e.g., stems. 
> Domain: ontolex:Form or ontolex:InflectionRule
> Range: literal
>
>---

MP: as it has been shown that also derivation can be based a form different than the canonical one (e.g. Latin deverbal conversions from the Third Stem, like capio (Third Stem capt-) > capt-o), I think this should hold also for DerivationRules

Note: For an inflection rule with `morph:baseType` defined: If the lexical entry to which it is applied features a(n object of) `morph:baseForm` or (if these are not defined) a `ontolex:canonicalForm` with identital `morph:baseType`, apply the rule to this form, only. For a (generated) form, `morph:baseType` can be used to indicate from which form or with which rule it was generated. `morph:baseType` can also be used to mark stem classes in reseources for which no explicit inflection rules are given.

Note: This was introduced for modelling stem alternations. In this definition, we assume that we have one lexical entry for each stem variant, so that an inflection rule whose baseType doesn't match of its lexical entry doesn't fire.

- telco 2022-02-23: moved from LexicalEntry to forms that are baseForm objects

- April 2022: renamed from stemType to baseType

## Word Formation


### morph:WordFormationRule

> ------
> Class **morph:WordFormationRule** describes the *general* pattern how words are being formed.
>
> -------

> ------
> MP: Class **morph:WordFormationRule** represents the generation of a target LexicalEntry from one (or more) source LexicalEntry.
>
> -------

MP: move rhe remark on the fact that they can be used to refer to general patterns here?

For the analysis of a *specific* compound or derivation, use `morph:WordFormationRelation`.

Note: originally, we had the class Rule which contains necessary information to add one morpheme to a single word form. It must contain either morph:example or morph:replacement (or both). “Tabular” value of a morpheme must be stored in rdfs:label (e.g. “-s”@en for usual PL in English)

> ---
> MP: Property **morph:involves** links an InflectionRule or a DerivationRule with the Morphs that are involved in the process.
> Domain: morph:WordFormationRule or morph:InflectionRule
> Range: morph:Morph
>
> ----

links a word formation rule or an inflection rule (see below) with one or multiple morphemes involved in the process. Note that this does not encode order. One possibility to approximate order for most cases would be to restore `morph:Suffix` and `morph:Prefix`.

Note: updated according to telco April 21, 2022.

> ---
> Property **morph:generates** *is to be defined*
> Domain: morph:WordFormationRule
> Range: ontolex:LexicalEntry
>
>> ----

MP: given the parallelism between the inflection and derivation subcomponents of the generation component, I would expect InflectionRule to generate something too -- namely, ontolex:Forms. Should we change the domain and range accordingly?

Note: updated according to draft from Feb 2022.

subclasses CompoundRule and DerivationRule. Normally, a derivation rule will involve one specific morpheme or one allomorphic variant. A compound rule can involve an interfix or another morphophonological process.

> ----
> Class **morph:DerivationRule**: Derivation is a lexical process that generates one lexical entry from another by means of a  derivational affix.
>  
>  ---

> ----
> MP: Class **morph:DerivationRule** refers to rules that take one LexicalEntry as input.
>  
>  ---

MP: I would rather not mention the presence of an affix so as to make the definition sufficiently general to cover conversion too (as happens in WFL data)

> ----
> MP: Class **morph:CompoundingRule** refers to rules that take more than one LexicalEntry as input.
>  
>  ---
### morph:WordFormationRelation

> ---
> class **morph:WordFormationRelation** is an `vartrans:LexicalRelation` that describes the way that a specific lexical entry is formed, with the `vartrans:target` representing the resulting lexical entry, and the `vartrans:source` representing the morphological base (in derivation) or head (in compounding).
>
> ----

CC: new; note that this definition covers derivation and `morph:CompoundHead` but *not* `morph:CompoundRelation`.
MP: can this be solved simply by specifying "head or other constituents"?

Note that word formation relations do not (= no longer) replicate the full typology of word formation processes. Also, a word formation does not provide a link with derivational affixes or interfixes in compounding involved in the compound.
Instead, this is modelled via `morph:WordFormationRule`:

>----
> property **morph:wordFormationRule** relates  two  lexical  entries  that  stand  in  some  word formation relation.
> Domain: morph:WordFormationRelation 
> Range: morph: WordFormationRule
>
>---

>----
> MP: property **morph:wordFormationRule** relates a word formation relation to the rule that is applied to the source lexical entry in order to obtain the target lexical entry.
> Domain: morph:WordFormationRelation
> Range: morph: WordFormationRule
>
>---

Accordingly, the morphological derivation of German *Schönheit* "beauty" can be encoded as:

	:schoenheit-entry a ontolex:LexicalEntry;
	             ontolex:canonicalForm [ ontolex:writtenRep "Schönheit"@de ].
	:schoen-entry a ontolex:LexicalEntry.
	             ontolex:canonicalForm [ ontolex:writtenRep "schön"@de ].
	:schoen_heit a morph:WordFormationRelation;
	             vartrans:source :schoen-entry;
	             vartrans:target :schoenheit-entry;
	             morph:wordFormationRule :_heit-rule.
	:_heit-rule a morph:WordFormationRule, morph:DerivationRule;
	            morph:involves :_heit-morph;
	            morph:generates :schoenheit-entry.
	:_heit-morph a morph:Morph, morph:Suffix;
	            ontolex:lexicalForm [ ontolex:writtenRep "-heit"@de ].

> ---
> class **morph:CompoundRelation** is a `morph:WordFormationRelation` that connects a (lexical entry representing a) morphological consituent of a compound with the (lexical entry representing the) compound. This is a reification of `decomp:subTerm`: A compound relation entails that the constituent is a subterm of the compound.
>
> ----

CC 2022-02-23 (offline): is that really necessary? why can't we just use `decomp` ? I guess this is for cases in which we don't know the head, but then, we can also just omit the source.

telco 2022-04-20: is to be redefined as a reification of `decomp:subTerm`.

> ---
> class **morph:CompoundHead** is a `morph:WordFormationRelation` that connects the (lexical entry representing the) morphological head of a compound with the (lexical entry representing the) compound.
>
> ----


## Open questions

These are questions we decided to postpone until finalization of the module. Don't use that for on-going discussions, that's what minutes are for.

- shouldn’t LexicalEntry (except as superclass of morph:Morph) be an ontolex:Word
	- MI: I think there was a discussion about this in the very beginning (about affixes). To check
	- CC: PRO: semantics: otherwise everything we define for lexical entry then also applies to `morph:Morph`, this could be abused in unforeseen ways
	- CC: CON: makes a more complicated diagram
	- JM: tbc whether there are inflected multi-word expressions (if so => CON)
	- JM: CON: in general, users should be clever enough to figure that out without putting it explicitly into the diagram
