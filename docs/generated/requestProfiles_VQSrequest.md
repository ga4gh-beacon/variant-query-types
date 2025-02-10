# Beacon VQS Requests

The `VQSrequest` type represents the generic collection of variant parameters supported in Beacon v2+ requests. These include parameters with close alignment to VRS v2 concepts and replacing some Beacon v1/v2 generics with tighter definitions (e.g. `referenceAccession` instead of `referenceName` and `accession` or `copyChange` for a specific subset of former `variantType` values) but also keep some conceptsm beyond VRS scope or specifically geared towards query applications (`geneId`, `sequenceLength`)


For the parameter definitions please see the [`requestParameterComponents` page.](../requestParameterComponents/)

## VQSrequest Parameters

* `requestProfileId`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/RequestProfileId`    
* `referenceAccession`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/RefgetAccession`    
* `start`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/SequenceStart`    
* `end`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/SequenceEnd`    
* `sequence`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/Sequence`    
* `copyChange`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/CopyChange`    
* `adjacencyAccession`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/AdjacencyAccession`    
* `adjacencyStart`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/AdjacencyStart`    
* `adjacencyEnd`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/AdjacencyEnd`    
* `repeatSubunitCount`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/RepeatSubunitCount`    
* `repeatSubunitLength`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/RepeatSubunitLength`    
* `geneId`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/GeneId`    
* `aminoacidChange`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/AminoacidChange`    
* `genomicAlleleShortForm`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm`    
* `sequenceLength`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/SequenceLength`    
* `vrsType`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/VRStype`    


## Beacon v2+/VQS "VRSified" Request Examples



### Copy number gains involving the _whole_ locus _chr2:54,700,000-63,900,000_
#### Solution for `VQSrequest` using `start` and `end` ranges (`VQScopyChangeRequest`)
The query has to indicate the involved genomic region by positions as well as the type of change. Here, matched duplication events start 5\` of the region and end 3\` of it. For capturing any event upt to the complete chromosome duplication this requires knowledge about the maximum value (_i.e._ chromosome base length; using a random very large number might fail depending on the implementation).
The example uses `"copyChange": "EFO:0030070"` for `copy number gain` as specified in the [VRS definitions](https://vrs.ga4gh.org/en/latest/terms_and_model.html#systemic-variation).
#### Request 
    
* `requestProfileId`: `VQScopyChangeRequest`    
    
* `referenceAccession`: `refseq:NC_000002.12`    
    
* `start`:     
    - `0`    
    - `54700000`        
    
* `end`:     
    - `63900000`    
    - `242193529`        
    
* `copyChange`: `EFO:0030070`    
    
* `vrsType`: `CopyNumberCount`    

##### GET query string
```requestProfileId=VQScopyChangeRequest&referenceAccession=refseq:NC_000002.12&start=0,54700000&end=63900000,242193529&copyChange=EFO:0030070&vrsType=CopyNumberCount```

##### POST query component 
```{
    "copyChange": "EFO:0030070",
    "end": [
        63900000,
        242193529
    ],
    "referenceAccession": "refseq:NC_000002.12",
    "requestProfileId": "VQScopyChangeRequest",
    "start": [
        0,
        54700000
    ],
    "vrsType": "CopyNumberCount"
}```


### Focal high-level deletion involving the _CDKN2A_ locus
#### Solution for `VQSrequest` using `start` and `end` ranges (`VQScopyChangeRequest`)
To match deletion variants overlapping the CDKN2A gene's coding region (CDR) with at least a single base, but limited to "focal" hits (here i.e. <= ~2Mbp in size) a bracket query is constructed where the `start` range goes  from ~1Mb 5\' of the CDKN2A CDR until the end of the CDR and the `end` range goes from the start of the CDR to ~1Mb 3\' of the gene. 
The query uses `"copyChange": "EFO:0020073"` for `high-level copy number loss` as specified in the [VRS definitions](https://vrs.ga4gh.org/en/latest/terms_and_model.html#systemic-variation). With hierarchical expansion of this term explicit complete genomic deletions (`EFO:0030069`) should be retrieved too.
#### Request 
    
* `requestProfileId`: `VQScopyChangeRequest`    
    
* `referenceAccession`: `refseq:NC_000002.12`    
    
* `start`:     
    - `21000001`    
    - `21975098`        
    
* `end`:     
    - `21967753`    
    - `23000000`        
    
* `copyChange`: `EFO:0020073`    
    
* `vrsType`: `CopyNumberCount`    

##### GET query string
```requestProfileId=VQScopyChangeRequest&referenceAccession=refseq:NC_000002.12&start=21000001,21975098&end=21967753,23000000&copyChange=EFO:0020073&vrsType=CopyNumberCount```

##### POST query component 
```{
    "copyChange": "EFO:0020073",
    "end": [
        21967753,
        23000000
    ],
    "referenceAccession": "refseq:NC_000002.12",
    "requestProfileId": "VQScopyChangeRequest",
    "start": [
        21000001,
        21975098
    ],
    "vrsType": "CopyNumberCount"
}```


### Find variants overlapping an approximate sequence location
#### Solution `g_variant` with range indicated by single `start` and `end` positions (`BV2rangeRequest`) and `variantType`
Here sequence variants at a specifiied region on chromosome 2 are matched by using single start and end positions to indicate the genomic *range*.
CAVE: Since no variant type is indicated such a query can potentially match a large number of variants, depending on the beacon's content and query interpretation (e.g. "any" overlap of a CNV could be matched unless the variant type is required for CNV queries).
#### Request 
    
* `assemblyId`: `GRCh38`    
    
* `referenceName`: `17`    
    
* `start`:     
    - `345675`        
    
* `end`:     
    - `345681`        

##### GET query string
```assemblyId=GRCh38&referenceName=17&start=345675&end=345681```

##### POST query component 
```{
    "assemblyId": "GRCh38",
    "end": [
        345681
    ],
    "referenceName": "17",
    "start": [
        345675
    ]
}```


### Query for a deletion involving TP53
#### Solution using `g_variant` with position range
Query for a deletion involving TP53 using the maximum extent of the gene's coding region (known from somewhere...). The deletion to be found are expected to have an overlap with the queried range; however, the extent of the overlap is not pre-defined (most endpoints woul respond to a **recommended** "any" overlap but this is not a strict requirement imposed by the schema). Here positions refer to chromosome 17 on GRCh38 as indicated by the referenceName RefSeq ID.
*Recommendation* Implementers should provide a mechanism to match any "deletion" `variantType` (`EFO:0030067`, `DEL`, `SO:0001743`) independent of size since operational definitions of `CNV` vs. `INDEL` vary, and use explicit `variantMinLength`, `variantMaxLength` parameters if needed.
#### Request 
    
* `referenceName`: `refseq:NC_0000017.11`    
    
* `start`:     
    - `7669608`        
    
* `end`:     
    - `7676593`        
    
* `variantType`: `DEL`    

##### GET query string
```referenceName=refseq:NC_0000017.11&start=7669608&end=7676593&variantType=DEL```

##### POST query component 
```{
    "end": [
        7676593
    ],
    "referenceName": "refseq:NC_0000017.11",
    "start": [
        7669608
    ],
    "variantType": "DEL"
}```


### Find insertion events in TP53 or in close proximity (±~5000bp)
#### Solution using `g_variant` with position range (`BV2rangeRequest`)
For this query the mapping position of TP53 (17:7669607-7676593) has to be known. Usually this knowledge would be provided by a front end helper and the aditional padding added manually or w/ a helper field (if frequent scenario) and the beacon itself would just receive the positional range request.
The "insertion" type is here provided through the Sequence Ontology term `SO:0000667` and for the chromosome the full, prefixed RefSeq term is being used.
#### Request 
    
* `referenceName`: `refseq:NC_0000017.11`    
    
* `start`:     
    - `7664000`        
    
* `end`:     
    - `7682000`        
    
* `variantType`: `SO:0000667`    

##### GET query string
```referenceName=refseq:NC_0000017.11&start=7664000&end=7682000&variantType=SO:0000667```

##### POST query component 
```{
    "end": [
        7682000
    ],
    "referenceName": "refseq:NC_0000017.11",
    "start": [
        7664000
    ],
    "variantType": "SO:0000667"
}```


### Find  t(8;14)(q24;q32) translocations
#### Solution for `VQSrequest` using genomic ranges (`VQSadjacencyRequest`)
This is a query for translocations between the MYC and IgH loci, where the breakpoints are loosely defined through there well known cytogenetic bands. The query here follows the VRS adjacency model. In contrast to the VRS representational model, here:    

- VRS uses an array of 2 genomic locations while Beacon names the location
  parameters individually (using "adjacency..." for the second partner)    
- VRS explicitely encodes directionality by using either `start` or `end`
  position parameters (integers or ranges) while this query example creates
  non-directional ranges on both sides since directionality might not be known,
  the storage system might not encode this or all options could be of interest    
#### Request 
    
* `requestProfileId`: `VQSadjacencyRequest`    
    
* `referenceAccession`: `refseq:NC_000008.11`    
    
* `start`: `116700000`    
    
* `end`: `145138636`    
    
* `adjacencyAccession`: `refseq:NC_000014.9`    
    
* `adjacencyStart`: `89300000`    
    
* `adjacencyEnd`: `107043718`    
    
* `vrsType`: `Adjacency`    

##### GET query string
```requestProfileId=VQSadjacencyRequest&referenceAccession=refseq:NC_000008.11&start=116700000&end=145138636&adjacencyAccession=refseq:NC_000014.9&adjacencyStart=89300000&adjacencyEnd=107043718&vrsType=Adjacency```

##### POST query component 
```{
    "adjacencyAccession": "refseq:NC_000014.9",
    "adjacencyEnd": 107043718,
    "adjacencyStart": 89300000,
    "end": 145138636,
    "referenceAccession": "refseq:NC_000008.11",
    "requestProfileId": "VQSadjacencyRequest",
    "start": 116700000,
    "vrsType": "Adjacency"
}```


### `CAG` repeat in the first exon of the huntingtin gene (HTT)
The gene HTT is located at position 4p16.3. In individuals without Huntington's disease, this CAG segment is typically repeated 10 to 35 times. Expansions beyond 35 copys are associated with the development of Huntington's disease.
Examples for query parameters are:
* GeneId: HTT * referenceAccession: refseq:NC_000004.12 * start: 3074681 * end: 3243960 * RepeatSubunitLength: 3 (CAG) * RepeatSubunitCount: [36, 250] (not yet defined in VRS or Beacon) * SequenceLength:  [105, 750]
See also the [genome browser material](https://genome.ucsc.edu/training/education/cag.html).
#### Solution using `VQSsequenceRepeatRequest` with locus and `sequenceLength`
This example uses the HTT genome position and a range of (extended) sequence lengths to match against a `ReferenceLengthExpression` since the VRS v2 model does not contain a "repeat count" concept but only the overall length and unit length (as well as the sequence).
TODO: Limit location to first exon?
#### Request 
    
* `requestProfileId`: `VQSsequenceRepeatRequest`    
    
* `referenceAccession`: `refseq:NC_000004.12`    
    
* `start`: `3074681`    
    
* `end`: `3243960`    
    
* `repeatSubunitLength`: `3`    
    
* `sequenceLength`:     
    - `105`    
    - `750`        
    
* `vrsType`: `ReferenceLengthExpression`    

##### GET query string
```requestProfileId=VQSsequenceRepeatRequest&referenceAccession=refseq:NC_000004.12&start=3074681&end=3243960&repeatSubunitLength=3&sequenceLength=105,750&vrsType=ReferenceLengthExpression```

##### POST query component 
```{
    "end": 3243960,
    "referenceAccession": "refseq:NC_000004.12",
    "repeatSubunitLength": 3,
    "requestProfileId": "VQSsequenceRepeatRequest",
    "sequenceLength": [
        105,
        750
    ],
    "start": 3074681,
    "vrsType": "ReferenceLengthExpression"
}```


### `CAG` repeat in the first exon of the huntingtin gene (HTT)
For details see above. 
#### Solution using `VQSsequenceRepeatRequest` with `geneId` and `sequenceLength`
Here instead of the position simply the gene symbol is being used.
#### Request 
    
* `requestProfileId`: `VQSsequenceRepeatRequest`    
    
* `geneId`: `HTT`    
    
* `repeatSubunitLength`: `3`    
    
* `sequenceLength`:     
    - `105`    
    - `750`        
    
* `vrsType`: `ReferenceLengthExpression`    

##### GET query string
```requestProfileId=VQSsequenceRepeatRequest&geneId=HTT&repeatSubunitLength=3&sequenceLength=105,750&vrsType=ReferenceLengthExpression```

##### POST query component 
```{
    "geneId": "HTT",
    "repeatSubunitLength": 3,
    "requestProfileId": "VQSsequenceRepeatRequest",
    "sequenceLength": [
        105,
        750
    ],
    "vrsType": "ReferenceLengthExpression"
}```


### `CGG` trinucleotide repeat expansion in the FMR1 gene
A `CGG` trinucleotide repeat expansion in the FMR1 gene on the X chromosome (Xq27.3) is known to cause Fragile X Syndrome (FXS). CGG repeating less than 44 times are stable across generations.
#### Solution using `VQSsequenceRepeatRequest` with `geneId` and `sequenceLength`
Similarly to the `HTT` example here a `geneId` is used to specify the gene and a range of sequence lengths is used to match against a `ReferenceLengthExpression`.
#### Request 
    
* `requestProfileId`: `VQSsequenceRepeatRequest`    
    
* `geneId`: `FMR1`    
    
* `repeatSubunitLength`: `3`    
    
* `sequenceLength`:     
    - `130`    
    - `600`        
    
* `vrsType`: `ReferenceLengthExpression`    

##### GET query string
```requestProfileId=VQSsequenceRepeatRequest&geneId=FMR1&repeatSubunitLength=3&sequenceLength=130,600&vrsType=ReferenceLengthExpression```

##### POST query component 
```{
    "geneId": "FMR1",
    "repeatSubunitLength": 3,
    "requestProfileId": "VQSsequenceRepeatRequest",
    "sequenceLength": [
        130,
        600
    ],
    "vrsType": "ReferenceLengthExpression"
}```


### Query for a focal deletion involving TP53
#### Solution using `VQSgeneIdRequest` with `geneId`
Query for a deletion involving TP53 by using the HUGO name to specify the gene. This request does not provide coordinates so on the server side matching has to be performed from annotated variants or by retrieving the gene's coordinates and creating internally a type of range request. Here we're also  limiting the size of the CNV to a typical "focal deletion" with a lower minimum size of 1kb (to avoid noise and non-structural variants) and an upper limit of 3Mb (to avoid large chromosomal deletions).
#### Request 
    
* `requestType`: `VQSgeneIdRequest`    
    
* `geneId`: `TP53`    
    
* `copyChange`: `EFO:0030067`    
    
* `sequenceLength`:     
    - `1000`    
    - `3000000`        
    
* `vrsType`: `CopyNumberCount`    

##### GET query string
```requestType=VQSgeneIdRequest&geneId=TP53&copyChange=EFO:0030067&sequenceLength=1000,3000000&vrsType=CopyNumberCount```

##### POST query component 
```{
    "copyChange": "EFO:0030067",
    "geneId": "TP53",
    "requestType": "VQSgeneIdRequest",
    "sequenceLength": [
        1000,
        3000000
    ],
    "vrsType": "CopyNumberCount"
}```
