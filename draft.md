# OntoLex-Morph definitions

(use this for drafting text fragments, the HTML template is under [index.html](index.html) -- but this is empty)

Definitions as of [2019-12-19](https://docs.google.com/document/d/1wybx2_U0EcqmefRRiAABha-cFII6H2rZBtlgTcjLYjg/edit?usp=sharing)

## Contents
  * [Morphological segments](#morphological-segments)
  * [Morphological rules](#morphological-rules)
    + [morph:example](#morph-example)
    + [morph:replacement](#morph-replacement)
  * [Inflection](#inflection)
    + [morph:Paradigm](#morph-paradigm)
    + [morph:paradigm](#morph-paradigm)
    + [morph:InflectionType](#morph-inflectiontype)
    + [morph:next](#morph-next)
    + [morph:inflects](#morph-inflects)
    + [morph:inflectionType](#morph-inflectiontype)
    + [morph:InflectionRule](#morph-inflectionrule)
  * [Word Formation](#word-formation)
    + [morph:WordFormationRule](#morph-wordformationrule)
    + [morph:generates](#morph-generates)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Morphological segments

## Morphological rules

> ------
> Class **morph:Rule**  contains necessary information to add one morpheme to a single word form. It must contain either morph:example or morph:replacement (or both). “Tabular” value of a morpheme must be stored in rdfs:label (e.g. “-s”@en for usual PL in English)
>
> -------

Note: This class was in the Dec 2019 draft, but before Feb 2022, this class had been abandoned from diagram for visual reasons, it is a superclass of `morph:WordFormationRule` and `morph:InflectionRule` and defined as the domain of the properties `morph:replacement` and `morph:example`. Its deletion is to be reassessed, as this was for visual reasons only. Anyway, any information about both kinds of rules should go into this section. 

### morph:example

> ----
> property **morph:example**: A single generated form that was generated using this rule
> Domain: morph:Rule
> Range: string literal
>
> ----

### morph:replacement

> ----
> Domain: morph:Rule
> Range: [morph:source, morph:target, both are string literals]
> 
> ----

note: 
- Until 2022-02-22, this was incorrectly shown in diagram as datatpe property

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

### morph:paradigm

>--------
> property **morph:paradigm**: A link to the paradigm for the inflection type
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


### morph:next

> ---
> property **morph:next** links two consecutive inflection types (“slots”), e.g. number and case in Finnish
> Domain: morph:InflectionType
> Range: morph:InflectionType
>
>---

### morph:inflects

> ---
> property **morph:inflects**: A link to the first “slot” (inflection type), e.g. an inflection type for number for English nouns
> Domain: ontolex:Word
> Range: morph:InflectionType
>
> ---

### morph:inflectionType

> -----
> Domain: morph:Rule
> Range: morph:InflectionType
>
> -----

### morph:InflectionRule

> ------
> Class **morph:InflectionRule** 
>
> -------

Note: originally, we had the class Rule which contains necessary information to add one morpheme to a single word form. It must contain either morph:example or morph:replacement (or both). “Tabular” value of a morpheme must be stored in rdfs:label (e.g. “-s”@en for usual PL in English)

## Word Formation


### morph:WordFormationRule

> ------
> Class **morph:WordFormationRule** 
>
> -------

Note: originally, we had the class Rule which contains necessary information to add one morpheme to a single word form. It must contain either morph:example or morph:replacement (or both). “Tabular” value of a morpheme must be stored in rdfs:label (e.g. “-s”@en for usual PL in English)


### morph:generates

> ---
> Domain: morph:Rule
> Range: unrestricted?
>
>> ----

note: 
BK: currently missing in draft image, does the inflection rule generate the ontolex:Form resources? yes
