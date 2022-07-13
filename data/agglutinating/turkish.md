# Modelling inflection type for agglutinating languages, taking Turkish as an example

examples and quotes from 

Gerjan van Schaaik (2020), The Oxford Turkish Grammar, Oxford University Press, ISBN 9780198851509, Published to Oxford Scholarship Online, DOI: 10.1093/oso/9780198851509.001.0001

https://oxford-universitypressscholarship-com.wikipedialibrary.idm.oclc.org/view/10.1093/oso/9780198851509.001.0001/oso-9780198851509-chapter-6

## slots and suffixes

> Turkish is a so-called *agglutinative* language, which means that a whole series of suffices may follow a word stem. Tentatively, these suffixes can be grouped as suffixes for *number*, *possession*, and *case marking*. (p.46)

> In the first slot in the suffix sequence the suffix for plural can be put; the second slot is reserved for suffixes expressing possession, and in the third slot any of the six case markers can be placed. Schematically, this gives:
> 	stem + (plural suffix) + (possessive suffix) + (case marker) [p.47]

> The order of the suffixes is strict but not every slot needs to be filled. ... One or more slots may remain empty ... [p.47]

- *ev* 'house'
- *ev-im* 'my house' (*-(I)m* '1.sg.poss')
- *ev-de* 'in the house' (*-TE* 'loc.')
- *ev-im-de* 'in my house'

> The plural is formed by attaching the suffix *-lEr* (glossed as 'plur'). Words in which the final vowel is a front vowel take *-ler* and words with a back vowel receive *-lar* [p.47]

- *ev-ler* 'my houses'
- *ev-ler-de* 'in the houses'
- *ev-ler-im-de* 'in my houses'
- *kitap-lar* 'books' (*kitap* 'book')

> The second slot in the suffix model ... can be filled by possessive suffixes. There are two variants: one for words ending in a vowel and one for words that end in a consonant. In their abbreviated form these possessive suffixes can best be interpreted as: *-(I)m* (etc.) [p.49]

- *araba-m* 'my car' (*araba* 'car')
- *ev-im* 'my house'

Focusing on 1.sg gives a slightly simplified picture, other morphemes involve optional phonemes that are used in specific contexts, e.g., *-(s)I(n)* (3.sg.poss.)

> The *nominative* ... is the uninflected form of a noun as it is listed in a dictionary. [p.50]

> The *genitive* case marker [is] *-(n)In* ... After vowels the form is *-nIn*, (...) [a]nd after consonants *-In* [p.51]

- *araba-nın* 'of the car'
- *ev-in* 'of the house'

## Morphophonology (assimilation rules)

### vowel harmony

in many suffixes, the vowel quality depends on the quality of the preceding vowel, i.e., alternation between

- front vowels: e i ö ü
- back vowels: a ı o u

> Twofold vowel harmony applies when a suffix comes in two forms. The vowel in that suffix is realized as an *e* if the preceding vowel is a front vowel, and as an *a* if preceded by a back vowel. The *plural* form of nouns, for instance, is either *-ler* or *-lar* ... [p.29] The pkural suffix can hence be represented by *-lEr*. [p.30]

> Fourfold vowel harmony works in principle in the same way ... The (predictable) vowel variation *ı*, *i*, *u*, *ü* will be represented ... by the capital letter *I* ... [p.30]

### Consonants

> In Turkish there are five suffixes that start with a t or a d and the choice of one depends on whether the preceding word ends in a voiceless or a voiced consonant. ... [For *-TE*, a] word ending in a vowel or a *voiced* consonant takes (...) [p.36] *-de* or *-da* (...) and otherwise (...) *-te* or *-ta*. [p.37]

- *ev-de* 'in the house'
- *kitap-ta* 'in the book'

## Modelling

> In the first slot in the suffix sequence the suffix for plural can be put; the second slot is reserved for suffixes expressing possession, and in the third slot any of the six case markers can be placed. Schematically, this gives:
> 	stem + (plural suffix) + (possessive suffix) + (case marker) [p.47]

> The order of the suffixes is strict but not every slot needs to be filled. ... One or more slots may remain empty ... [p.47]

	# *ev* 'house'
	:ev_le a ontolex:LexicalEntry; 
		lexinfo:partOfSpeech lexinfo:commonNoun;
		ontolex:sense [ skos:definition "house" ];
		ontolex:canonicalForm :ev_lf.
	:ev_lf a ontolex:Form;
		ontolex:writtenRep "ev"@tr .

### *ev-im* 'my house' (*-(I)m* '1.sg.poss'), descriptive
	:Im_m a ontolex:Affix;
		morph:grammaticalMeaning [ :tag "1.sg.poss" ];
		morph:baseForm [ ontolex:writtenRep "-(I)m"@tr ];
		ontolex:lexicalForm :Im_m_m_f, :Im_m_ım_f, :Im_m_im_f, :Im_m_um_f, :Im_m_üm_f.

> In many suffixes, the vowel quality depends on the quality of the preceding vowel, i.e., alternation between

- front vowels: e i ö ü
- back vowels: a ı o u

> The (predictable) vowel variation *ı*, *i*, *u*, *ü* will be represented ... by the capital letter *I* ... [p.30]

	:Im_m_im_f a ontolex:Form;
		ontolex:writtenRep "-im"@tr;
		morph:grammaticalMeaning [ :phon :ending_in_consonant, :front_vowel, :not_rounded, :not_unvoiced ] ;
		morph:baseConstraint [ :phon :ending_in_consonant, :front_vowel, :not_rounded ]. 
		# note: so far, this was on morph, only, but this would be a way to implement vowel harmony

For this to work, we also need to add phonological features (grammatical meaning) to the canonical form

	:ev_lf morph:grammaticalMeaning [ :phon :ending_in_consonant, :front_vowel, :not_rounded, :not_unvoiced ].

	:ev_le ontolex:lexicalForm :evim_lf.
	:evim_lf a ontolex:Form;
		ontolex:writtenRep "evim"@tr;
		morph:consistsOf :ev_le, :Im_m; # not necessary because of the following
		rdf:_1 :ev_le;
		rdf:_2 :Im_m.

### *ev-im-de* 'in my house'

	:TE_m a ontolex:Affix;
		morph:grammaticalMeaning [ :tag "loc" ];
		morph:baseForm [ ontolex:writtenRep "-TE"@tr ];
		ontolex:lexicalForm :TE_m_da_f, :TE_m_de_f, :TE_m_ta_f, :TE_m_te_f.

	:TE_m_de_f a ontolex:Form;
		ontolex:writtenRep "-de"@tr;
		morph:grammaticalMeaning [ :phon :front_vowel, :ending_in_vowel, :not_rounded ];
		morph:baseConstraint [ :phon :not_unvoiced, :front_vowel, :not_rounded ].

> In Turkish there are five suffixes that start with a t or a d and the choice of one depends on whether the preceding word ends in a voiceless or a voiced consonant. ... [For *-TE*, a] word ending in a vowel or a *voiced* consonant takes (...) [p.36] *-de* or *-da* (...) and otherwise (...) *-te* or *-ta*. [p.37]

	:ev_le ontolex:lexicalForm :evimde_lf.
	:evimde_lf a ontolex:Form;
		ontolex:writtenRep "evimde"@tr;
		morph:consistsOf :ev_le, :Im_m, :TE_m;
		rdf:_1 :ev_le;
		rdf:_2 :Im_m;
		rdf:_3 :TE_m.

> note that alternatively, we can model each allomorph as an independent morph with one canonical form
> then, baseConstraints on forms would not be necessary
> to be discussed: do we want this? this would lead to more consistent modelling, but it would rob data providers of
> some degree of flexibility that may be necessary for different data sources (i.e. those that do not properly distinguish
> morphemes and allomorphs)

## modelling inflection types

For further modelling, we ignore allomorphy (for the moment) and operate over morphs, only.

Idea was to use inflection types to model slots:

	> stem + (plural suffix) + (possessive suffix) + (case marker) [p.47]

### alternative 0: keep current model, one inflection type per paradigm and rule

	Form -inflectionType-> InflectionType
	Paradigm <-paradigm- InflectionType
	InflectionType -inflectionRule-> InflectionRule
	InflectionType -next-> InflectionType

	:ev_le ontolex:morphologicalPattern :nominal_paradigm.
	:nominal_paradigm a morph:Paradigm.

	:ev_lf morph:inflectionType :number_slot_zero, :poss_slot_zero, :case_slot_zero.
	:number_slot_zero a morph:InflectionType;
		morph:inflectionRule :zero_rule;
		morph:paradigm :nominal_paradigm.
	:poss_slot_zero a morph:InflectionType;
		morph:inflectionRule :zero_rule;
		morph:paradigm :nominal_paradigm.
	:case_slot_zero a morph:InflectionType;
		morph:inflectionRule :zero_rule;
		morph:paradigm :nominal_paradigm .

	:zero_rule a morph:InflectionRule.
	# note: we don't say anything about this rule, by default, we don't model nothing explicitly ;)

	:evim_lf morph:inflectionType :number_slot_zero, :poss_slot_Im, :case_slot_zero.
	:evimde_lf morph:inflectionType :number_slot_zero, :poss_slot_Im, :case_slot_TE.
	# etc. for other 

	:poss_slot_Im a morph:InflectionType;
		morph:inflectionRule :Im_rule;
		morph:paradigm :nominal_paradigm.
	:case_slot_TE a morph:InflectionType;
		morph:inflectionRule :TE_rule;
		morph:paradigm :nominal_paradigm.

	:Im_rule a morph:InflectionRule;
		morph:involves :Im_m;
		morph:replacement [ morph:source "$"; morph:target "(I)m" ].
	:TE_rule a morph:InflectionRule;
		morph:involves :TE_m;
		morph:replacement [ morph:source "$"; morph:target "TE"].

We only generate the "deep" form, for resolving allomorphs, we need to model each allomorph as a separate morph

> I guess this is what we should do -- or, we should link inflection rules to grammatical meaning
> so that the same mechanism for resolving allomoprhy constraints can apply (as also suggested by our Greek colleagues ;)
> and then have one inflection rule per allomorphic variant


As inflection types do not correspond to slots, but combinations of rules and paradigms, we need to express order for all individual inflection types:

	:number_slot_zero morph:next :poss_slot_zero, :poss_slot_Im. # etc.
	:poss_slot_zero morph:next :case_slot_zero, :case_slot_TE. # etc.
	:poss_slot_Im morph:next :case_slot_zero, :case_slot_TE. # etc.

We don't compile all variants out, but model exactly the same data for the alternatives.

43 triples

### alternative 1: detach InflectionType

	Form -inflectionRule-> InflectionRule
	Paradigm <-paradigm- InflectionRule
	InflectionRule -inflectionType-> InflectionType
	InflectionType -next-> InflectionType

	:ev_le ontolex:morphologicalPattern :nominal_paradigm.
	:nominal_paradigm a morph:Paradigm.

if we go from forms to inflection rules, we need to create one rule per morph, i.e., multiple zero rules

	:ev_lf morph:inflectionRule :number_zero_rule, :poss_zero_rule, :case_zero_rule.
	:number_zero_rule a morph:InflectionRule
		morph:paradigm :nominal_paradigm;
		morph:inflectionType :number_slot.
	:poss_zero_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:inflectionType :poss_slot.
	:case_zero_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:inflectionType :case_slot.

inflection types for encoding order

	:number_slot a morph:InflectionType;
		morph:next :poss_slot.
	:poss_slot a morph:InflectionType;
		morph:next :case_slot.

Note that this modelling is *somewhat* incomplete as we don't mark beginning and end explicitly.

	:evim_lf morph:inflectionType :number_zero_rule, :poss_Im_rule, :case_zero_rule.
	:evimde_lf morph:inflectionType :number_zero_rule, :poss_Im_rule, :case_TE_rule.
	# etc. for other 

	:poss_Im_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:involves :Im_m;
		morph:replacement [ morph:source "$"; morph:target "(I)m" ].

	:case_TE_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:involves :TE_m;
		morph:replacement [ morph:source "$"; morph:target "TE"].

36 triples

### alternative 2: replace InflectionType by GrammaticalMeaning 

	Form -inflectionRule-> InflectionRule
	Paradigm <-paradigm- InflectionRule
	InflectionRule -grammaticalMeaning-> GrammaticalMeaning
	GrammaticalMeaning -next-> GrammaticalMeaning


	:ev_le ontolex:morphologicalPattern :nominal_paradigm.
	:nominal_paradigm a morph:Paradigm.

if we go from forms to inflection rules, we need to create one rule per morph, i.e., multiple zero rules

	:ev_lf morph:inflectionRule :number_zero_rule, :poss_zero_rule, :case_zero_rule.
	:number_zero_rule a morph:InflectionRule
		morph:paradigm :nominal_paradigm;
		morph:grammaticalMeaning :number_slot.
	:poss_zero_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:grammaticalMeaning :poss_slot.
	:case_zero_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:grammaticalMeaning :case_slot.

inflection types for encoding order

	:number_slot a morph:GrammaticalMeaning;
		morph:next :poss_slot.
	:poss_slot a morph:GrammaticalMeaning;
		morph:next :case_slot.

Note that this modelling is *somewhat* incomplete as we don't mark beginning and end explicitly.

	:evim_lf morph:inflectionRule :number_zero_rule, :poss_Im_rule, :case_zero_rule.
	:evimde_lf morph:inflectionRule :number_zero_rule, :poss_Im_rule, :case_TE_rule.
	# etc. for other 

	:poss_Im_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:involves :Im_m;
		morph:replacement [ morph:source "$"; morph:target "(I)m" ].

	:case_TE_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:involves :TE_m;
		morph:replacement [ morph:source "$"; morph:target "TE"].

36 triples

### alternative 3: merge InflectionType with InflectionRule
	
	Form -inflectionRule-> InflectionRule
	Paradigm <-paradigm- InflectionRule
	InflectionRule -grammaticalMeaning-> GrammaticalMeaning
	InflectionRule -next-> InflectionRule

	:ev_le ontolex:morphologicalPattern :nominal_paradigm.
	:nominal_paradigm a morph:Paradigm.

if we go from forms to inflection rules, we need to create one rule per morph, i.e., multiple zero rules

	:ev_lf morph:inflectionRule :number_zero_rule, :poss_zero_rule, :case_zero_rule.
	:number_zero_rule a morph:InflectionRule
		morph:paradigm :nominal_paradigm;
		morph:grammaticalMeaning :number_slot.
	:poss_zero_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:grammaticalMeaning :poss_slot.
	:case_zero_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:grammaticalMeaning :case_slot.

Note that this modelling is *somewhat* incomplete as we don't mark beginning and end explicitly.

	:evim_lf morph:inflectionRule :number_zero_rule, :poss_Im_rule, :case_zero_rule.
	:evimde_lf morph:inflectionRule :number_zero_rule, :poss_Im_rule, :case_TE_rule.
	# etc. for other 

	:poss_Im_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:involves :Im_m;
		morph:replacement [ morph:source "$"; morph:target "(I)m" ].

	:case_TE_rule a morph:InflectionRule;
		morph:paradigm :nominal_paradigm;
		morph:involves :TE_m;
		morph:replacement [ morph:source "$"; morph:target "TE"].

slot order operates over inflection rules, here

	:number_zero_rule morph:next :poss_zero_rule, :poss_Im_rule. # etc.
	:poss_zero_rule morph:next :case_zero_rule, :case_TE_rule. # etc.
	:poss_Im_rule morph:next :case_zero_rule, :case_TE_rule. # etc.
	
38 triples

### evaluation

alternative 1 and alternative 2 have the same number of triples (36), note that these avoid the combinatorial explosion necessary for current modelling and next over rules, so that is a significant gain.

The difference is just whether inflection type is considered to be something different from grammatical meaning.
Terminologically, this makes sense.
In terms of verbosity, we might want to link inflection types and grammatical meaning, and then, more triples would be required.

suggested compromise: create a designated subclass "Slot" of grammatical meaning. For computational applications, yet another subclass could be "State", in either case, the difference is terminological only, not in terms of definitions.