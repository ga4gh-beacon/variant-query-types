# Recommended Ternminologies and Example Values

Beyond single beacons or managed beacon networks the use of common, widely supported
and standardized query values is of special importance to empower federated queries.
The main examples relevant to variation queries here are `referenceName` and
`variantType`. 

!!! info "Value Definitions in the Beacon Schemas"

	In most of its schemas the Beacon v2 specification is not prescriptive in the
	specific values permitted for individual parameters and provides a number of
	legacy values as examples in its inline documentation. This was thought
	to promote flexibility (e.g. non-human use cases) and simple adoption (e.g. reusing
	VCF terms).

!!! bug "Beacon Scouts To Do"

	We will add and document recommended termionologies and use case examples during
	the _2024/2025 Beacon Variation Scouts_ process.

## VRSification and value definitions

Due to the adoption of VRS concepts already recommendations for some values can be provided.

### `referenceName` (v1/v2) and `referenceSequence` (v2+)

Reference names (`referenceName`) in Beacon v1/v2 allow versioned and unversioned
formats and use an `assemblyId` to specify the reference genome.

#### Recommendation

1. use of un-prefixed chromosome names (e.g. `1`, `17`, `X`) for human genomes
  together with an `assemblyId` (e.g. `GRCh38`), OR
2. use of prefixed Refseq chromosome names (e.g. `refseq:NC_000001.11`)

From experience with current practices the use of option 1 seems more widespread
and - while implementations should be able to disambiguate and remap - recommended
over option 2.

```
?referenceName=17&assemblyId=GRCh38
```

Moving forward the Beacon v2+ specification will adopt the VRS `referenceSequence`
which uses the Refget definitions and include the prefixed Refseq chromosome id
use as option.

```
?referenceSequence=refseq:NC_000017.11
```

### `variantType` (v1/v2) and `copyChange` (v2+)

In Beacon v1/v2 the `variantType` parameter is a free text field and can be used
to scope queries for specific types of genomic variations. It is very permissive
and ambigouos, with frequent use of VCF terms but also other such as from `SO` and `EFO`.

With the current move of the Beacon v2+ specification towards the use of the VRS
concepts the future of a general `variantType` equivalent for variation queries
has yet to be determined. However, VRS v2 provides a dedicated `copyChange` parameter
as well as a dedicated vocabulary derived from EFO terminology.

#### Recommendation

* for CNV queries use the EFO terms for relative copy number changes for either
  `copyChange` or `variantType` parameters, depending on the Beacon version
* for other types of variations `variantType` according to query documentation and
  emerging examples
* `variantType` might be replaced during future development


