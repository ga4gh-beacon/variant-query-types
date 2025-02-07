# Beacon VQS Requests

This represents the generic collection of variant parameters supported in Beacon v2+ requests.


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
* `variantMinLength`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/VariantMinLength`    
* `variantMaxLength`:    
    - `$ref`: `./requestParameterComponents.yaml#/$defs/VariantMaxLength`    
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
    
* `vrsType`: `copyChange`    

##### GET query string
```requestProfileId=VQScopyChangeRequest&referenceAccession=refseq:NC_000002.12&start=0,54700000&end=63900000,242193529&copyChange=EFO:0030070&vrsType=copyChange```

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
    "vrsType": "copyChange"
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
    
* `vrsType`: `copyChange`    

##### GET query string
```requestProfileId=VQScopyChangeRequest&referenceAccession=refseq:NC_000002.12&start=21000001,21975098&end=21967753,23000000&copyChange=EFO:0020073&vrsType=copyChange```

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
    "vrsType": "copyChange"
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


### Query for a focal deletion involving TP53
#### Solution using `VQSgeneIdRequest` with `geneId`
Query for a deletion involving TP53 by using the HUGO name to specify the gene. This request does not provide coordinates so on the server side matching has to be performed from annotated variants or by retrieving the gene's coordinates and creating internally a type of range request. Here we're also  limiting the size of the CNV to a typical "focal deletion" with a lower minimum size of 1kb (to avoid noise and non-structural variants) and an upper limit of 3Mb (to avoid large chromosomal deletions).
#### Request 
    
* `requestType`: `VQSgeneIdRequest`    
    
* `geneId`: `TP53`    
    
* `copyChange`: `EFO:0030067`    
    
* `variantMinLength`: `1000`    
    
* `variantMaxLength`: `3000000`    
    
* `vrsType`: `copyChange`    

##### GET query string
```requestType=VQSgeneIdRequest&geneId=TP53&copyChange=EFO:0030067&variantMinLength=1000&variantMaxLength=3000000&vrsType=copyChange```

##### POST query component 
```{
    "copyChange": "EFO:0030067",
    "geneId": "TP53",
    "requestType": "VQSgeneIdRequest",
    "variantMaxLength": 3000000,
    "variantMinLength": 1000,
    "vrsType": "copyChange"
}```
