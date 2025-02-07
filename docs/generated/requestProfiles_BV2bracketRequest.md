# Request Profile: `BV2bracketRequest`

A typical Beacon v2 request for matching variations where start and end fall in a genomic range. Here, the approximate or varying positions for variation start and end are queried through brackets, _i.e._ by using 2 values for `start` and `end` each. This is a typical scenario in querying for CNVs where the `variantType` parameter indicates the relative change in genomic copy number through either VCF derived string parameters or, preferably, EFO terms (pls. refer to the class definition.) Since a bracket request is a positional query for varying sequence extend no `sequence` parameter should be used.

### Find small, _variable_ sequence insertions/deletions at an approximate position
#### Solution `g_variant` with `start` and `end` ranges (`BV2bracketRequest`) and `variantType`
Here sequence variants (insertions or deletions) involving a specific region on chromosome 17 but of varying length are matched by using "fuzzy" start  and end ranges ("brackets"). The variant type is identified as an INDEL although the interpretation is left to the implementation; e.g. an insertion which is stored as sequence change `17:43045708:A>AAACAAAC` would fulfill the request but might not be indicated as `INDEL` type.
#### Request 
    
* `assemblyId`: `GRCh38`    
    
* `referenceName`: `17`    
    
* `start`:     
    - `43045703`    
    - `43045709`        
    
* `end`:     
    - `43045715`    
    - `43045720`        
    
* `variantType`: `INDEL`    

##### GET query string
```assemblyId=GRCh38&referenceName=17&start=43045703,43045709&end=43045715,43045720&variantType=INDEL```

##### POST query component 
```{
    "assemblyId": "GRCh38",
    "end": [
        43045715,
        43045720
    ],
    "referenceName": 17,
    "start": [
        43045703,
        43045709
    ],
    "variantType": "INDEL"
}```


### Copy number gains involving the _whole_ locus _chr2:54,700,000-63,900,000_
#### Solution for `g_variant` using `start` and `end` ranges (`BV2bracketRequest`)
The query has to indicate the involved genomic region by positions as well as the type of change. Here, matched duplication events start 5\` of the region and end 3\` of it. For capturing any event upt to the complete chromosome duplication this requires knowledge about the maximum value (_i.e._ chromosome base length; using a random very large number might fail depending on the implementation).
The example uses `EFO:0030070` for `copy number gain` instead of the alternative `SO:0001742` `copy_number_gain` or the VCF `DUP` as the preferred since the EFO terms provide a more granular expressivity and are referenced in the [VRS definitions](https://vrs.ga4gh.org/en/latest/terms_and_model.html#systemic-variation).
#### Request 
    
* `assemblyId`: `GRCh38`    
    
* `referenceName`: `refseq:NC_000002.12`    
    
* `start`:     
    - `0`    
    - `54700000`        
    
* `end`:     
    - `63900000`    
    - `242193529`        
    
* `variantType`: `EFO:0030070`    

##### GET query string
```assemblyId=GRCh38&referenceName=refseq:NC_000002.12&start=0,54700000&end=63900000,242193529&variantType=EFO:0030070```

##### POST query component 
```{
    "assemblyId": "GRCh38",
    "end": [
        63900000,
        242193529
    ],
    "referenceName": "refseq:NC_000002.12",
    "start": [
        0,
        54700000
    ],
    "variantType": "EFO:0030070"
}```
