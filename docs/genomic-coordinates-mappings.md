# Genomic Coordinates and Mappings

!!! Attention "GA4GH Beacon Genome Coordinate Use Recommendation[^1]"

    * Beacon recommends the use of a __"0-start, half-open"__ (interbase) coordinate
      system
    * __"1-start, fully-closed"__ should be used when displaying coordinates through
      a Beacon GUI

## Variant normalization

The Beacon v2 specification does not prescribe which style of variant normalization
_sequence defined queries_ are based on. In practice usually the VCF model is assumed
(parsimony with avoidance of empty alleles). However, the GA4GH VRS specification
argues against this practice and recommends a fully justified normalization[^2].

!!! bug "Beacon Scouts To Do"

	The Beacon Variant Scouts team will work on documenting a recommended variant
	normalization format which might deviate from current practices.




[^1]: Source: [@andrewyatz](https://github.com/@andrewyatz/) at [GenomeStandards](https://genomestandards.org/standards/genome-coordinates/)
[^2]: VRS normalization rules as design decision: [Alleles are Fully Justified](https://vrs.ga4gh.org/en/latest/appendices/design_decisions.html#alleles-are-fully-justified)
