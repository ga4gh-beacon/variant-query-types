# Query Types

Genomic variation queries can be implemented through combinations of different parameters,
as available through the given data model. Beacon v2's variation query parameters
are defined in the `genomicVariations` default model's
[requestParameters schema](https://github.com/ga4gh-beacon/beacon-v2/blob/main/models/src/beacon-v2-default-model/genomicVariations/requestParameters.yaml).
As part of the 2024 Beacon Variant Scouts we work on a revison and potential
extension of the available parameters, as well as on the definition of canonical
_Query Types_ tailored to the retrieval of defined [_Variant Types_](../variant-types).

## Beacon v2 Default Model Queries

### _Sequence Queries_: `VariantSequenceRequest`[^1]

_Sequence Queries_ query for the existence of a specified sequence at a given genomic
position. Such queries roughly correspond to Beacon v1 queries and are used to match
short, precisely defined genomic variants such as SNVs, MNVs and INDELs.

### _Range Queries_: `VariantRangeRequest`[^1]

Beacon _Range Queries_ are supposed to return matches of any variant with at least
partial overlap of the sequence range specified by `referenceName`, `start` and `end`
parameters.

* Documentation: [VariantRangeRequest](VariantRangeRequest.md)
* Schema: [`VariantRangeRequest.yaml`]({{config.repo_url}}{{config.schemas_path}}VariantRangeRequest.yaml)


### _Bracket Queries_ ("CNV queries"): `VariantBracketRequest`[^1]

_Bracket Queries_ allow the specification of sequence ranges for both start and end
positions of a genomic variation. The typical example here is the query for similar
structural variants - particularly CNVs - affecting a genomic region but potentially
differing in their exact extents.

* Documentation: [VariantBracketRequest](VariantBracketRequest.md)
* Schema: [`VariantBracketRequest.yaml`]({{config.repo_url}}{{config.schemas_path}}VariantBracketRequest.yaml)


### _GeneId Queries_: `GeneRequest`[^1]

_GeneId Queries_ are in essence a variation of _Range Queries_ in which the coordinates
are replaced by the [HGNC](https://www.genenames.org) gene symbol. It is left to the
implementation if the matching is done on variants annotated for the gene symbol or if
a positional translation is being applied.

### _Aminoacid Change Queries_: `AminoacidRequest`[^1]

Annotated variants can potentiallyqueried using the single amino acid replacement
format. The `aminoacidChange` parameter may (must?[^2]) be combined with e.g. a `geneId` to increase
specificity


## Query Type Proposals

==TBD==





[^1]: The names of the request type schemas should be considered "malleable".
[^2]: One of the *conventions* which so far haven't been settled (TBD).




