# Variation Query Parameters

!!! note "Current Beacon variation query parameters"

    The parameters currently implemented can be looked up in the Beacon v2
    default model'e [`genomicVariations/requestParameters`](https://github.com/ga4gh-beacon/beacon-v2/blob/main/models/src/beacon-v2-default-model/genomicVariations/requestParameters.yaml).

    Quoted text below reflects the v2 definitions, some of which might be subject
    toc change (e.g. as result of the scouts' process).

## Beacon v2 Variant Request Parameters

### `assemblyId`

In the original Beacon v2 specification `assemblyId` parameter refers to the

> genomic assembly accession and version as RefSqeq assembly accession (e.g. "GCF_000001405.39")
> or a versioned assembly name or synonym such as UCSC Genome Browser assembly (e.g. "hg38")
> or Genome Reference Consortium Human (e.g. GRCh38.p13") names.

#### Scouts TODO

* Revise / tighten these definitions since they are highly polymorphic; at least with
  a clearly documented preference?
* Abandon the parameter in lieu of versioned `referenceName` values? Currently both
  are allowed.


### `referenceName`

The `referenceName` parameter matches the 
    
> sequence id for genomic sequence (e.g. chromosome) in which variant coordinates
> (`start`, `end` ...) are given. Preferably a RefSeqId or alternatively common
> synonymus or aliases.

#### Examples

- refseq:NC_000009.12
- NC_000009.12
- Chr9
- 9
- NC_012920.1

#### Scouts TODO

* More stringent ID use?
* New explicit parameter?

### `mateName`

The parameter is used for a sequence id as in the `referenceName` definitions,
for use cases describing a fusion event (to a different or identical chromosome).
While the parameter had been defined in the Beacon v2 default model so far there
had been no good definition/documentation of use cases (though intuitively there
are many practical cases for translocation/fusion events).

#### Scouts TODO

* document use cases
* define query prototype(s)

### `start`

Precise or fuzzy start coordinate position(s) for a variation locus (0-based, inclusive).
The use depends on the query type:

> * `start` only:
> 	  - for single positions, e.g. the start of a specified sequence
> 	  alteration where the size is given through the specified `alternateBases`
> 	  - typical use are queries for SNV and small InDels
> 	  - the use of `start` without an `end` parameter requires the use of
> 	  `alternateBases`
> * `start` and `end`:
> 	  - for searching any variant falling fully or partially within the range
> 	  between `start` and `end` (a.k.a. "range query")
> 	  - additional use of `variantType` OR `alternateBases` can limit the
> 	  scope of the query
> 	  - by convention, partial overlaps of variants with the indicated genomic
> 	  range are accepted; for specific overlap requirements the 4-parameter
> 	  "Bracket Queries" should be employed
> * 2 values in both `start` and `end` for constructing a "Bracket Query":
> 	  - can be used to match any contiguous genomic interval, e.g. for querying
> 	  imprecise positions
> 	  - identifies all structural variants starting between `start[0]` and `start[1]`,
> 	  and ending between `end[0]` <-> `end[1]`
> 	  - single or double sided precise matches can be achieved by setting
> 	  `start[1]=start[0]+1` and `end[1]=end[0]+1`

#### Scouts TODO

* de-convolute documentation, _i.e._ move specifics to the query type definitions

### `end`

Precise or fuzzy end coordinate position(s) for a variation locus (0-based, inclusive).
This is commonly used for variations w/o specified sequence (although e.g. a range
and a sequence motif could be combined).

#### Scouts TODO

* as above

### `alternateBases`

Sequence of bases for this variation (starting from `start`).

> * Accepted values: [ACGTN]
> * N is a wildcard, that denotes the position of any base and can be used as
> a standalone base of any type or within a partially known sequence. As example,
> a query of `ANNT` the Ns can take take any form of [ACGT] and will match
> `ANNT`, `ACNT`, `ACCT`, `ACGT` ... and so forth.
> * an _empty value_ is used in the case of deletions with the maximally
> trimmed, deleted sequence being indicated in `referenceBases`

#### Scouts TODO

* resolve ambiguity in schema where also the pattern: `^([ACGTUNRYSWKMBDHV\-\.]*)$`
  is given
* future use of `sequence` as in VRS?


### `referenceBases`
      
Sequence of bases which have been replaced by the variation (from `start`). The
use of characters is equivalent to the `alternateBases` parameter.


#### Scouts TODO

* determine if `referenceBases` should be abandoned ...

### `variantType`

The `variantType` is used to query variants which are not defined through a sequence
of one or more bases using the `alternateBases` parameter or through an alternative
query type using non-sequence parameters (e.g. `aminoacidChange`).

The Beacon v2 schema uses some "VCF-like" examples w/o being prescriptive:

> Examples here are e.g. structural variants:
>
> * DUP
>     - increased allelic count of material from the genomic region between
>   `start` and `end` positions
>     - no assumption about the placement of the additional sequences is being
>   made (i.e. no _in situ_ requirement as tandem duplications)
> * DEL: deletion of sequence following `start`
> * BND: breakend, i.e. termination of the allele at position `start` or in
> the `startMin` => `startMax` interval, or fusion of the sequence to distant
> partner
>
> Either `alternateBases` or `variantType` is required, with the exception
> of range queries (single `start` and `end` parameters).

#### Scouts TODO

* revise regarding the preferential use of CURIEs (_i.e._ EFO or SO classes), as
  has been [exemplified in the Beacon v2 documentation](http://docs.genomebeacons.org/variant-queries/#cnv-term-use-comparison-in-computational-fileschema-formats)
  for CNVs
* revise/delete notes about parameter combinations which should be moved to the
  query type definitions

### `variantMinLength`

* Minimum length in bases of a genomic variant
* This is an optional parameter without prescribed use. While a length is commonly
  available for structural variants such as copy number variations, it is recommended
  that length based queries should also be supported for variants with indicated 
  eferenceBases and alternateBases, to enable length-specific wildcard queries.

#### Scouts TODO

* check definition

### `variantMaxLength`

* Maximum length in bases of a genomic variant.
* otherwise as above

### `geneId`

* A gene identifier
* It is suggested to use a symbol following the HGNC (https://www.genenames.org)
  nomenclature.

#### Examples

* BRAF
* SCN5A

#### Scouts TODO

* check definition
* compare to VRS where [prefixed identifiers are required](https://vrs.ga4gh.org/en/latest/terms_and_model.html#gene) instead of gene symbols

### `aminoacidChange`

An aminoacid alteration in 1 letter format.

#### Examples

* V600E
* M734V

#### Scouts TODO

* check definition

### `genomicAlleleShortForm`

A genomic HGVSId descriptor.

#### Examples

* NM_004006.2:c.4375C>T

#### Scouts TODO

* expand definition and examples

