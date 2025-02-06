# Beacon Variant Scouts

**Variant Query Types and Components**

The Beacon protocol has demonstrated the general feasibility of federated queries and aggregated responses for genomic sequence variations, over distributed and disparate resources when supporting a common protocol. The final Beacon v1 standard added the option to query some for some types of structural variations - notably CNVs; and during the design of the Beacon v2 standard a "Variant Scouts" group documented an extended set of supported query patterns, while the development team implemented the necessary parameters (such as aminoacidAlteration, variantMaxLength, geneId…)  into the Beacon default data model. However, several aspects had to be left open or have arisen since the original definitions - frequently not concerning necessary query parameter extensions but rather definition of standardized vocabularies and usage practices.

The Beacon Varians Scouts work will focus on:

* Establishing an extended set of use case driven variant query needs and document how to express them through current Beacon parameters
* Suggesting extensions to the current specification where use cases, after triage against borderline scenarios and with a conservative view towards extending the vocabulary
* Document recommended vocabularies and standards (e.g. for `variantType` or `referenceName`)
* Develop use cases into typed queries (e.g. deletion, fusion, translocation request) implemented through schema documents, following the previous points
* Evaluate solutions for scenarios requiring identification of compound variants

The outcome of this scout would be a document summarising points 1-3, and building on the previous Genomic variants document. It could, for example, take the form of a submitted article. Importantly, we envision that the group - in coordination with other standards groups from GA4GH and beyond - will provide solid "variant query standard blocks" - not necessarily limited to Beacon implementations; thereby providing an overarching harmonization of federated variant discovery tools and implementations.

## VRSification

From ongoing Beacon Scouts work and coordination with the Genomic Knowledge Standards
work stream we have come to the overall agreement that future Beacon variant standards
and queries will adopt the VRS v2+ standard to the largest extent possible. In reality
this (probably) translates into 

* Beacon v2+ inlining or referencing VRS schemas
* variant queries using VRS terms and structures or referring to them (since query
  parameters might require different structures from definition parameters)

We've started to refer to the developing VRSified query options as "*VQS*" (*V*ariation
*Q*uery *S*tandard).

## Material & References

* Beacon v2 [Variant Queries documentation](http://docs.genomebeacons.org/variant-queries/#genomic-variant-queries)
* Previous [Beacon Scouts: Genomic Variants Use Cases & Examples](https://docs.google.com/document/d/1cwwRQ2PtlN1dBffCugdkbSHWCPmLgLkADd-5mu-rVAw/edit)
* [VRS data model](https://vrs.ga4gh.org/en/latest/terms_and_model.html)

* ELIXIR hCNV [CNV type comparison matrix](https://cnvar.org/resources/CNV-annotation-standards/)
* Experimental Factor Ontology [CNVs](https://www.ebi.ac.uk/ols4/ontologies/efo/classes/http%253A%252F%252Fwww.ebi.ac.uk%252Fefo%252FEFO_0030066?lang=en)
* Sequence Ontology [sequence_variant](http://sequenceontology.org/browser/current_release/term/SO:0001060)