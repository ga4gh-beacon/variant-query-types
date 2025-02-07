# Request Profile: `VQScopyChangeRequest`

A typical Beacon v2.n request for copy number variations (CNVs) queries approximate positions for CNV start and end regions through use of the `Range` type. The `copyChange` parameter indicates the relative change in genomic copy number (pls. refer to the class definition.)

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
