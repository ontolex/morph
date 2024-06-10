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
  >  scope: The kind of elements of which a lexical entry can consist should be as non-restrictive as possible. I.e. The decomposition of lexical entries encompass lexical entries, components, derivational affixes, inflectional affixes, stems, roots and zero morphs. However, a lexical entry can NEVER be composed of a form!

  - Morphological decomposition on the form level.

  > scope: Elements of which a form can consist include roots, stems, inflectional affixes and zero morphs. 

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
> Class **morph:Morph** is a subclass of ontolex:LexicalEntry that represents any element of morphological analysis below the word level.

> -------

Notes:
- can carry `lexinfo:termElement` (for what?)
- can consist of other morphs [MP: not in the last version of the diagram; is that intended?]
- the model is agnostic as to whether this represents a morpheme or one of its allomorphs, but as a lexical entry
- grammaticalMeaning: glossing information associated with the morph
- baseConstraint: (for affixes) contraints on the elements that this morph can be applied to
- `ontolex:Affix` is defined as a subclass of `morph:Morph`.
- other types of morph (roots, stems, transfix, etc.) are not defined in the module, but should be defined in Lexinfo

> ------
> Property **morph:consistsOf** states  into  which  Morph resources a Form resource can  be segmented.
> Domain: ontolex:Form
> Range: morph:Morph
>
>-----

Note: we still have no way to encode the order of morphemes.  We can model forms and morphs as an aggregate (here: `rdf:List` ?).


### morph:GrammaticalMeaning

> ------
> Class **morph:GrammaticalMeaning** can be used to represent (bundles of) values of different morpho-syntactic features expressed by a form, morph or rule (e.g., value 'nominative' for feature 'case', value 'singular' for feature 'number', etc.; or the feature bundle composed by the latter two values, in a fusional language where they are expressed cumulatively, e.g. Latin)

> -------

Notes:
- should use lexinfo resources or instances with `rdfs:label`
- can represent *either* an individual feature or a feature bundle

> ------
> property **morph:grammaticalMeaning** assigns a grammatical meaning to a morph, form, or rule
> domain: ontolex:Form or morph:Morph or morph:Rule
> range: morph:GrammaticalMeaning

> -------


For instance, the segmentation into morphs of the english plural form *cats*, and the assignment of grammatical meaning to the form and the corresponding plural morph,  can be expressed in this way.

    :cats a ontolex:Form ;
        ontolex:writtenRep "cats"@en ;
        morph:grammaticalMeaning lexinfo:plural ;
        morph:consistsOf :cat , :-s .

    :cat a morph:Morph .

    :-s a ontolex:Affix ;
        morph:grammaticalMeaning lexinfo:plural .

Since plural number is the only morphosyntactic feature value conveyed by this form and morph, in this case the grammatical meaning simply corresponds to the individual for that feature value in Lexinfo.

On the other hand, in the Latin form *lupus*, nominative case and singular number are expressed cumulatively by the affix *-us*. Therefore, an instance of morph:GrammaticalMeaning is introduced for that feature bundle, and the individual feature values included therein can be expressed using the property :composedOf in the Paralex ontology.

    :lupus a ontolex:Form
        ontolex:writtenRep "lupus"@la ;
        morph:grammaticalMeaning :nom.sg ;
        morph:consistsOf :lup , :-us .

    :lup a morph:Morph .

    :-us a ontolex:Affix ;
        morph:grammaticalMeaning :nom.sg .

    :nom.sg a morph:GrammaticalMeaning ;
        paralex:composedOf lexinfo:nominativeCase , lexinfo:singular .

Discussion/History:

- the extension to forms was introduced 2022-02-23 per request from Penny and Matteo for more conveniently providing re-usable and directly indexable "feature bundles".
- the eLex-2019 draft had `morph:meaning` in a comparable function, but with Morph being subclass of LexicalEntry, this role is taken over by `ontolex:sense`.
- in spring 2022, it was requested by Penny and Katerina to make this a property of `morph:InflectionRule` as a short-hand for `morph:involves/morph:grammaticalMeaning`.
- as of 2022-10-19, it was agreed to attach this property also to `morph:Rule`. For circumstances in which no explicit morph can be provided (but only a rule), e.g., because a resource comes without an explicit notion of morph(eme)s, there would not be a way to express the meaning or function of that morpheme, otherwise.
- question (CC, 2022-10-24): do we need this for `morph:InflectionType` ? This would be useful to express that a certain "slot" contains information of a particular kind, e.g., morphological gender or morphological number. Right now, this information is implicit (in the inflection rules assigned to a particular inflection type).

> ------
> property **morph:baseConstraint** defines the grammatical characteristics of the stem or base that a derivational or inflectional morpheme can be combined with
> domain: ontolex:Morph or ontolex:Rule

> -------

For example, an element for nominal inflection can only be applied to nouns, and derivational affixes can have similar constraints. Note that such information is not applicable to an `ontolex:Form` because this describes only the result of the application of a rule or the addition of a particular form.

Discussion/History:
- CC 2022-10-24: by analogy with morph:grammaticalMeaning, this property should also be applicable to rules to specify necessary preconditions.

### morph:baseForm

> ----
> MP: Property **baseForm** is a subproperty of `ontolex:lexicalForm` that indicates the form that is taken as base for the application of inflection or derivation rules to generate other forms.
> Domain: `ontolex:Word` (not lexical entry!)
> Range: `ontolex:Form`

>  ---


This property is necessary in cases in which inflection or derivation relations do not take the canonical form as their basis, but a different one. One example is German verbal inflection (e.g., for `gehen` "to go"), where the canonical form (`gehen`, infinitive) is derived from the base form (`geh-`, stem) by means of a suffix (`-en`, infinitive marker), like other inflected forms (`geh`, `gehst`, `geht` "I/you go; he/she/it goes").

## Morphological Rules

> ------
> Class **morph:Rule** represents the formal operation applied to a base form to obtain another form (inflectionally or derivationally related to it).
> It must contain either morph:example or morph:replacement (or both). “Tabular” value of a morpheme must be stored in rdfs:label (e.g. “-s”@en for usual PL in English)

> -------

### morph:example

> ----
> property **morph:example**: A single generated form that was generated using this rule
> Domain: morph:Rule
> Range: string literal

> ----

### morph:replacement

> ----
> property **morph:replacement** states the replacement pattern that is involved in a morphological rule for the generation of a form
> Domain: morph:Rule
> Range: any URI, cf. in doc/wrapup/minutes-2025-06-64

processing analogy: replacement operations with regular expressions as in Perl or Sed.

As an example, a simple replacement operation would be concatenation, i.e., retrieve the baseForm (or canonicalForm, if no baseForm provided), check that it has the same stem type as the rule (if applicable), then append an affix to the written representation of the baseForm.

> Note: Unless specified otherwise (in the documentation of a resource), implementations SHOULD provide NFD-normalized Unicode strings for `morph:source` and `morph:target`, so that diacritics are separated from the base character as combining characters. This is a best practice that simplifies the writing of rules in many cases, as diacritic and base character can be manipulated independently from each other.

### morph:involves

> Property **morph:involves** links a Rule with the Morphs that are involved in the process.
> Domain: morph:Rule
> Range: morph:Morph

Note that this does not encode order. 

## Inflection

### morph:InflectionClass

> --------------------
> Class **morph:InflectionClass** represents the inflection class to which a LexicalEntry belongs/is assigned -- e.g., the declension of a noun, or the conjugation of a verb.

> -----------

It may contain metadata information about this type of declension.

Note: the link between inflection classes and lexical entries is not defined in OntoLex-Morph, but modelled using `ontolex:morphologicalPattern`.

> --------------------
> Property **morph:inflectionClass** links an inflection rule to the inflection class it pertains to.
> Domain: morph:InflectionRule
> Range: morph:InflectionClass

> --------------------

### morph:InflectionSlot

> ----------
> Class **morph:InflectionSlot**  represents a single slot for all values of a grammatical category or, in the case of bundles of grammatical categories, for all combinations of values thereof
>
> --------
>
Book analogy: a column from a paradigm table without allomorphy/alternative variants for just a single morpheme

Note: for fusional languages, the inflection slot may be associated, for instance, with a combination of gender, number and case, as in the example of Greek nouns, while for agglutinative languages, each inflection type is associated with a single grammatical category (e.g. all values of case)

> -----
> property **morph:inflectionSlot** links an inflection rule to the slot it pertains to
> Domain: morph:InflectionRule
> Range: morph:InflectionSlot

> -----


> ---
> property **morph:next** links two consecutive inflection types (“slots”), e.g. number and case in Finnish
> Domain: morph:InflectionType
> Range: morph:InflectionType

>---

### morph:InflectionRule

> ------
> Class **morph:InflectionRule** represents the formal operation applied to a base form of a LexicalEntry to obtain another inflected form of that LexicalEntry.
>
> -------

The example below illustrates the modelling of inflection classes and rules for the generation of the genitive singular of *lupus* in Latin.

    lupus a ontolex:LexicalEntry ;
        ontolex:canonicalForm :lupus_form ;
        ontolex:morphologicalPattern :firstDeclension .

    gen_sg_rule a morph_InflectionRule ;
        morph:example "lupi" ;
        morph:replacement ? ;
        morph:inflectionClass :firstDeclension ;
        morph:grammaticalMeaning :gen.sg ;
        morph:involves :-i .

    :-i a ontolex:Affix ;
        morph:grammaticalMeaning :gen.sg .

In a fusional language like Latin, there is no need to have different inflection slots: a single inflection rule (specific for the inflection class to which the lexical entry is assigned) allows for the generation of the genitive singular form as follows:

    :lupi a ontolex:Form ;
        ontolex writtenRep "lupi"@la ;
        morph:grammaticalMeaning :gen.sg ;
        morph:consistsOf :lup , :-i .

On the other hand, in an agglutinative language like Turkish, it is useful to define separate inflection slots for each morphosyntactic feature, and separate inflection rules for each inflection slot, as illustrated in the example below. 

    adam a ontolex:LexicalEntry ;
        ontolex:canonicalForm adam_form ;
        ontolex:morphologicalPattern :noun_infl_vowelHarmony1 .

    pl_rule a morph:InflectionRule ;
        morph:example "adamlar" ;
        morph:replacement ? ;
        morph:inflectionClass :noun_infl_vowelHarmony1 ;
        morph:grammaticalMeaning lexinfo:plural ;
        morph:involves :-lar ;
        morph:inflectionSlot number_slot . 

    acc_rule a morph:InflectionRule ;
        morph:example "adami" ;
        morph:replacement ? ;
        morph:inflectionClass :noun_infl_vowelHarmony1 ;
        morph:grammaticalMeaning lexinfo:accusativeCase ;
        morph:involves :-i ;
        morph:inflectionSlot case_slot .

    number_slot a morph:InflectionSlot ;
        rdfs:comment "slot for number in Turkish nominal inflection" ;
        morph:next case_slot .

    case_slot a morph:InflectionSlot ;
        rdfs:comment "slot for case in Turkish nominal inflection" .

The successive application of the two appropriate rules for accusative and plural formation -- in the order established by the use of the morph:next property -- allows for the generation of the accusative plural form as follows:

    :adamlari a ontolex:Form ;
      ontolex writtenRep "adamlari"@tur ;
      morph:grammaticalMeaning [lexinfo:accusative , lexinfo:plural ] ;
      morph:consistsOf :adam , :-lar , :-i .

### morph:baseType

> ----
> Datatype property **morph:baseType** is used for coindexing a base form, an inflection rule and the forms generated by the rule from the respective base in cases in which the inflectional paradigm of a single lexical entry involves different bases, e.g., stems. 
> Domain: ontolex:Form or ontolex:InflectionRule (or ontolex:Rule? MP)
> Range: literal

>---

MP: as it has been shown that also derivation can be based a form different than the canonical one (e.g. Latin deverbal conversions from the Third Stem, like capio (Third Stem capt-) > capt-o), shouldn't this hold also for WordFormationRule?

Note: For an inflection rule with `morph:baseType` defined: If the lexical entry to which it is applied features a(n object of) `morph:baseForm` or (if these are not defined) a `ontolex:canonicalForm` with identital `morph:baseType`, apply the rule to this form, only. For a (generated) form, `morph:baseType` can be used to indicate from which form or with which rule it was generated. `morph:baseType` can also be used to mark stem classes in reseources for which no explicit inflection rules are given.

Note: This was introduced for modelling stem alternations. In this definition, we assume that we have one lexical entry for each stem variant, so that an inflection rule whose baseType doesn't match of its lexical entry doesn't fire.

## Word Formation


### morph:WordFormationRule

> Class **morph:WordFormationRule** represents the formal operation applied to a base form of a source LexicalEntry to obtain another, target LexicalEntry form (inflectionally or derivationally related to it).

Note: It describes the *general* pattern how words are being formed.For the analysis of a *specific* compound or derivation, use `morph:WordFormationRelation`.



Note: updated according to telco April 21, 2022.

> ---
> Property **morph:generates** *is to be defined*
> Domain: morph:WordFormationRule
> Range: ontolex:LexicalEntry
>
>> ----

MP: given the parallelism between the inflection and derivation subcomponents of the generation component, I would expect InflectionRule to generate something too -- namely, ontolex:Forms. Should we change the domain and range accordingly?

subclasses CompoundRule and DerivationRule. Normally, a derivation rule will involve one specific morpheme or one allomorphic variant. A compound rule can involve an interfix or another morphophonological process.

> ----
> Class **morph:DerivationRule** refers to rules that take one LexicalEntry as input and generate another LexicalEntry as output through the addition of a derivational affix.

>  ---

> Class **morph:CompoundingRule** refers to rules that take more than one LexicalEntry as input to generate the output Lexical.

>  ---
### morph:WordFormationRelation

> ---
> class **morph:WordFormationRelation** is a subclass of `vartrans:LexicalRelation` that describes the way in which a specific lexical entry is formed, with the `vartrans:target` representing the resulting lexical entry, and the `vartrans:source` representing the morphological base (in derivation) or head (in compounding).
>
> ----

> ---
> class **morph:WordFormationRelation** is a subclass of `vartrans:LexicalRelation` that relates two lexical entries that are derivationally related, with the `vartrans:target` representing the resulting lexical entry, and the `vartrans:source` representing the morphological base (in derivation) or head and other constituents (in compounding).

> ----

>----
> property **morph:wordFormationRule** relates a word formation relation to the word formation rule that is applied to the source lexical entry in order to obtain the target lexical entry.
> Domain: morph:WordFormationRelation
> Range: morph: WordFormationRule

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

> ----

> ---
> class **morph:CompoundHead** is a `morph:WordFormationRelation` that connects the (lexical entry representing the) morphological head of a compound with the (lexical entry representing the) compound.

> ----

## Open questions

These are questions we decided to postpone until finalization of the module. Don't use that for on-going discussions, that's what minutes are for.

- shouldn’t LexicalEntry (except as superclass of morph:Morph) be an ontolex:Word
  - MI: I think there was a discussion about this in the very beginning (about affixes). To check
  - CC: PRO: semantics: otherwise everything we define for lexical entry then also applies to `morph:Morph`, this could be abused in unforeseen ways
  - CC: CON: makes a more complicated diagram
  - JM: tbc whether there are inflected multi-word expressions (if so => CON)
  - JM: CON: in general, users should be clever enough to figure that out without putting it explicitly into the diagram
