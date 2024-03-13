# Use Case Examples

<!--
TODO:
* more examples
* GET vs. POST examples
-->

## Any deletion(s) involving the TP53 gene locus

### `VariantRangeRequest`

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

### `GeneRequest`

For the interpretation of the "deletion" parameter see above.

```
?geneId=TP53&variantType=EFO:0030067
```

--------------------------------------------------------------------------------

## Copy number gains involving the whole locus (chr2:54,700,000-63,900,000)

The query has to indicate the involved genomic region by positions as well as the
type of change. Here, matched duplication events start 5\` of the region and end 3\`
of it.

Besides the positions, this requires knowledge about the maximum value of the
reference base (or use of  a very large one exceeding chromosome size; this example
here uses an "2nd end position equal to chr2 + 1" value).

While the example uses `SO:0001742` for `copy_number_gain` the EFO term use
(`EFO:0030070`: `copy number gain`) should be preferred since the EFO terms provide
a more granular expressivity and are referenced in the [VRS definitions](https://vrs.ga4gh.org/en/latest/terms_and_model.html#systemic-variation).

```
?referenceName=refseq:NC_000002.12&start=0,54700000&end=63900000,242193529&variantType=SO:0001742
```

--------------------------------------------------------------------------------
==TBD==