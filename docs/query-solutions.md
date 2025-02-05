# Use Case Examples

!!! bug "Auto-generated Examples"

	We are moving to a system where examples are auto-generated from the YAML
	example files in the source tree instead of maintaining separate descriptions.
	The examples below (though correct) will be replaced with the new system soon.

	The current version of query examples for the Beacon v2 parameters (_i.e._ not
	using additional parameters beyond the specification) can be found in 
	**[Beacon v2 Examples](../generated/requestProfiles_g_variant)**.


## Mature, working examples

### Any deletion(s) involving the TP53 gene locus

??? tip "Using `VariantRangeRequest`"

	The query can be created by using the maximum extent of the TP53 coding region
	(optionally extended for functionally relevent elements, e.g. promotor), and a
	`variantType` parameter supported by the implementation. The interpretation of
	"any deletion" is not straightforward; this would potentially include small
	INDELS specified as sequence alterations as well as copy number deletions.

	*Recommendation* Implementers should provide a mechanism to match any "deletion" `variantType`
	(`EFO:0030067`, `DEL`, `SO:0001743`) independent of size since operational definitions
	of `CNV` vs. `INDEL` vary, and use explicit `variantMinLength`, `variantMaxLength`
	parameters if needed.

	```
	?referenceName=NC_0000017.11&start=7669608&end=7676593&variantType=EFO:0030067
	```

??? tip "Using `GeneRequest`"

	For the interpretation of the "deletion" parameter see above.

	```
	?geneId=TP53&variantType=EFO:0030067
	```


### Insertion event in gene TP53 (17:7669607-7676593) or in close proximity (±~5000bp)

??? tip "Using `VariantRangeRequest`"

	For this query the mapping position of TP53 (17:7669607-7676593) has to be
	known. Usually this knowledge would be provided by a front end helper and
	the aditional padding added manually or w/ a helper field (if frequent scenario)
	and the beacon itself would just receive the positional range request.

	The "insertion" type is here provided through the Sequence Ontology term
	`SO:0000667` and for the chromosome the full, prefixed RefSeq term is being used.

	```
	?referenceName=refseq:NC_000017.11&start=7664000&end=7682000&variantType=SO:0000667
	```

### Copy number gains involving the _whole_ locus _chr2:54,700,000-63,900,000_

??? tip "Using `VariantBracketRequest`"

	The query has to indicate the involved genomic region by positions as well as the
	type of change. Here, matched duplication events start 5\` of the region and end 3\`
	of it. For capturing any event upt to the complete chromosome duplication this
	requires knowledge about the maximum value (_i.e._ chromosome base length; using a
	random very large number might fail depending on the implementation).

	The example uses `EFO:0030070` for `copy number gain` instead of the alternative
	`SO:0001742` `copy_number_gain` as the preferred since the EFO terms
	provide a more granular expressivity and are referenced in the
	[VRS definitions](https://vrs.ga4gh.org/en/latest/terms_and_model.html#systemic-variation).

	```
	?referenceName=refseq:NC_000002.12&start=0,54700000&end=63900000,242193529&variantType=SO:0001742
	```


## Work in Progress
