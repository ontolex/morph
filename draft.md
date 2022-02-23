
# OntoLex-Morph definitions

(use this for drafting text fragments, the HTML template is under [index.html](index.html) -- but this is empty)
When
When given and unless marked otherwise, definitions follow the wording of [2019-12-19](https://docs.google.com/document/d/1wybx2_U0EcqmefRRiAABha-cFII6H2rZBtlgTcjLYjg/edit?usp=sharing), resp., the [eLex -2019 paper](https://elex.link/elex2019/wp-content/uploads/2019/09/eLex_2019_33.pdf)

## Acknowledgements

editors (= past and present telco moderators, alph.; please double-check):
- Christian Chiarcos (since 2022)
- Maxim Ionov (since 2018)
- Bettina Klimek (2018-2022)

contributors (alph, **incomplete/please add yourself/people you know**):
- Julia Bosque-Gil (2018-2022)
- Christian Chiarcos (since 2018)
-  Jesse De Does (2019-2020)
- Katrien Depuydt (2019-2020)
- Maxim Ionov (since 2018)
- Bettina Klimek (2018-2022)
- John P. McCrae (since 2018)
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
  * [morph:stemType](#morph-stemtype)
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

2. Enabling the representation of building patterns that are involved in the formation of lexical entries and forms.
	- Representation of decompositional building patterns for lexical entries.
	- Representation of decompositional building patterns for forms.

A fine-grained description of phonological and morphophonological processes that are  involved in any kind of stem or word formation on the phoneme level is excluded and not representable with this Morphology Module. Only the elements  between the lexical entry and the morph levels will be covered. It is possible, however, that such information may be addressed in future OntoLex modules.

The OntoLex-Morph module aims to be adequate for both traditional dictionary content (which contains only abbreviated about morphological rules and paradigms, often organized in appendices) and structured computational data (morphological dictionaries) as used in Language Technology, with the goal of making resources from one community more accessible to the other.

## Morphological Segments

### morph:Morph

> ------
> Class **morph:Morph** is a subclass of ontolex:LexicalEntry that represents a concrete primitive element of  
morphological analysis.
>
> -------

Notes:
- can carry `lexinfo:termElement` (for what?)
- can consist of other morphs
- the model is agnostic as to whether this represents a morpheme or one of its allomorphs, but as a lexical entry
- grammaticalMeaning: glossing information associated with the morph
- baseConstraint: (for affixes) contraints on the elements that this morph can be applied to
- subclasses `ontolex:Affix`, RootMorph, StemMorph, TransfixMorph, SimulfixMorph, ZeroMorph

> ----
> Class **morph:RootMorph** identifies morph:Morphs that constitute the  semantic nucleus  of a stem. A root morph cannot be further segmented and  is often not specified for a part of speech.
> subClassOf: morph:Morph
> 
> ---

> ---
> Class **morph:StemMorph** identifies  morph:Morphs to which inflectional  marking applies.
> subClassOf: morph:Morph
> 
> ---

> Note: we do not define affix (a bound segmental morph), but instead, `ontolex:Affix` is defined as a subclass of `morph:Morph`.

>---
> Class **morph:TransfixMorph** is a discontinous `ontolex:Affix`
> subClassOf: ontolex:Affix, morph:Morph
>  
>  ---
> ---
> Class **morph:SimulfixMorph**: A simulfix is a bound morph that entails a   change or replacement of vowels or consonants  (usually vowels) which changes the meaning of   a word, e.g.  eat  in past tense becomes  ate.
> subClassOf: ontolex:Affix, morph:Morph
>  
>  ---

> ---
> Class **morph:ZeroMorph**: A morph that that corresponds to no overt   form,  i.e.  orthographic  or  phonetic  representation
> subClassOf: ontolex:Affix, morph:Morph
>  
>  ---


> ------
> Property **morph:consistsOf** states  into  which  Morph resources a Form resource can  be segmented.
> Domain: ontolex:Form, morph:Morph
> Range: ontolex:Form, morph:Morph
>
>-----

Note: this is the eLex-2019 definition, but now we have consists of between morphs and between forms, too

Note: we still have no way to encode the order of morphemes.  We can model forms and morphs as an aggregate (here: `rdf:List` ?).


### morph:GrammaticalMeaning

> ------
> Class **morph:GrammaticalMeaning** *is to be defined*
>
> -------

Notes: should use lexinfo resources por instances with `rdfs:label`

> ------
> property **morph:grammaticalMeaning** assigns a grammatical  meaning to a morph resource
>
> -------

Note: the eLex-2019 draft also had `morph:meaning`, but with Morph being subclass of LexicalEntry, this role is taken over by `ontolex:sense`.

> ------
> property **morph:baseConstraint** *is to be defined*
>
> ------

### morph:morphophonologicalRelation

> ----
> Datatype **morph:morphophonologicalRelation** is *to be defined*
> Domain: `ontolex:LexicalEntry` or `ontolex:Form`
> 
> ----

### morph:baseForm
> ----
> Property **baseForm** is an `ontolex:lexicalForm` property that indicates the morphological base form of a lexical entry
> Domain: `ontolex:Word` (not lexical entry!)
> Range: `ontolex:Form`
>  
>  ---

This property is necessary in cases in which inflection or derivation relations do not take the canonical form as their basis, but a different one. One example is German verbal inflection (e.g., for `gehen` "to go"), where the canonical form (`gehen`, infinitive) is derived from the base form (`geh-`, stem) by means of a suffix (`-en`, infinitive marker), like other inflected forms (`geh`, `gehst`, `geht` "I/you go; he/she/it goes").

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
> property **morph:replacement** *is to be defined* 
> Domain: morph:WordFormationRule or morph:InflectionRule
> Range: morph:Replacement 
> 
> ----

note: 
- Until 2022-02-22, this was incorrectly shown in diagram as datatpe property

> ---
> class **morph:Replacement** *is to be defined*
> 
> ---

processing analogy: replacement operations with regular expressions as in Perl or Sed

> ---
> datatype property **morph:source** *is to be defined*
> domain: morph:Replacement
> range: string literal
> 
> ----

> ---
> datatype property **morph:target** *is to be defined*
> domain: morph:Replacement
> range: string literal
> 
> ----

## Inflection

### morph:Paradigm

> --------------------
> Class **morph:Paradigm** represents a theoretically motivated type of declination, e.g.
> -   “a” stem declension in Latin
> -   First declension in Russian
>
> May contain metadata information about this type of declination.
>
> -----------
Book analogy: a full paradigm table with possible allomorphy/alternative variants

Note: eLex-2019: `morph:InflectionalParadigm`: A structured set of inflected forms according  
to specific grammatical parameters. This is now not a set of inflected forms but a set of inflection types that are linked with the respective forms.

>--------
> property **morph:paradigm**: A link to the paradigm for the inflection type (eLex-2019: assigns a form to an  
inflectional paradigm)
> Domain: morph:InflectionType
> Range: morph:Paradigm
> 
> ---


### morph:InflectionType

> ----------
> Class **morph:InflectionType**  represents a single slot for a single grammatical category for all its possible values (e.g. all the cases)
>
> --------
> 
Book analogy: a column from a paradigm table without allomorphy/alternative variants for just a single morpheme


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
> Class **morph:InflectionRule** *is to be defined*
>
> -------

Note: originally, we had the class Rule which contains necessary information to add one morpheme to a single word form. It must contain either morph:example or morph:replacement (or both). “Tabular” value of a morpheme must be stored in rdfs:label (e.g. “-s”@en for usual PL in English)

> ---
> property **morph:inflects**: A link to the first “slot” (inflection type), e.g. an inflection type for number for English nouns
> Domain: morph:InflectionType
> Range: ontolex:Word
>
> ---


### morph:stemType

> ----
> Datatype property **morph:stemType** is used for coindexing a stem and an inflection rule in cases in which a single lexical entry can have multiple stem classes, in which a type of inflection rules operates with one stem class
> Domain: ontolex:LexicalEntry or ontolex:InflectionRule
> Range: literal
>
>---

Note: This was introduced for modelling stem alternations. In this definition, we assume that we have one lexical entry for each stem variant, so that an inflection rule whose stemType doesn't match of its lexical entry doesn't fire.

Question (CC, 2022-02-23, offline): wouldn't it make more sense to model stemType at a (base) form rather than at the level of lexical entries?


## Word Formation


### morph:WordFormationRule

> ------
> Class **morph:WordFormationRule** describes the *general* pattern how words are being formed.
>
> -------

For the analysis of a *specific* compound or derivation, use `morph:WordFormationRelation`.

Note: originally, we had the class Rule which contains necessary information to add one morpheme to a single word form. It must contain either morph:example or morph:replacement (or both). “Tabular” value of a morpheme must be stored in rdfs:label (e.g. “-s”@en for usual PL in English)

> ---
> Property **morph:involves** *is to be defined*
> Domain: morph:WordFormationRule
> Range: morph:Morph
> 
> ----

links a word formation rule with one or multiple morphemes involved in the process. Note that this does not encode order. One possibility to approximate order for most cases would be to restore `morph:Suffix` and `morph:Prefix`.

question: this corresponds to `morph:inflects` for inflection rules. Can we generalize over both? (If so, we probably need to re-instatiate `morph:Rule`.

> ---
> Property **morph:generates** *is to be defined* 
> Domain: morph:WordFormationRule
> Range: ontolex:LexicalEntry
>
>> ----

Note: updated according to draft from Feb 2022.

subclasses CompoundRule and DerivationRule. Normally, a derivation rule will involve one specific morpheme or one allomorphic variant. A compound rule can involve an interfix or another morphophonological process.

> ----
> Class **morph:DerivationRule**: Derivation is a lexical process that generates one lexical entry from another by means of a  derivational affix.
>  
>  ---


### morph:WordFormationRelation

> ---
> class **morph:WordFormationRelation** is an `vartrans:LexicoSemanticRelation` that describes the way that a specific lexical entry is formed, with the `vartrans:target` representing the resulting lexical entry, and the `vartrans:source` representing the morphological base (in derivation) or head (in compounding).
> 
> ----

CC: new; note that this definition covers derivation and `morph:CompoundHead` but not `morph:CompoundRelation`.

Note that word formation relations do not (= no longer) replicate the full typology of word formation processes. Also, a word formation does not provide a link with derivational affixes or interfixes in compounding involved in the compound. 
Instead, this is modelled via `morph:WordFormationRule`:

>----
> property **morph:wordFormationRule** relates  two  lexical  entries  that  stand  in  some  word formation relation.
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
> class **morph:CompoundRelation** is a `morph:WordFormationRelation` that connects a (lexical entry representing a) morphological consituent of a compound with the (lexical entry representing the) compound. 
> 
> ----

CC 2022-02-23 (offline): is that really necessary? why can't we just use `decomp` ? I guess this is for cases in which we don't know the head, but then, we can also just omit the source.

> ---
> class **morph:CompoundHead** is a `morph:WordFormationRelation` that connects the (lexical entry representing the) morphological head of a compound with the (lexical entry representing the) compound. 
> 
> ----


