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
