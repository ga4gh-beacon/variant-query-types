# Request Profile: `BV2rangeRequest`

Beacon Range Queries are supposed to return matches of any variant with at least partial overlap of the sequence range specified by `referenceName`, `start` and end `parameters`. Additional qualifiers such as `variantType` or length of the affected sequence can be used to further restrict the returned results. For this request type `start` and `end` with a single position are used, _i.e._ a subset of the `start` and `end` specifications.

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


### Query for a deletion involving TP53
#### Solution using `g_variant` with position range
Query for a deletion involving TP53 using the maximum extent of the gene's coding region (known from somewhere...). The deletion to be found are expected to have an overlap with the queried range; however, the extent of the overlap is not pre-defined (most endpoints woul respond to a **recommended** "any" overlap but this is not a strict requirement imposed by the schema). Here positions refer to chromosome 17 on GRCh38 as indicated by the referenceName RefSeq ID.
#### Request 
* `referenceName`: `refseq:NC_0000017.11`    
* `start`:     
    - `7669608`        
* `end`:     
    - `7676593`        
* `variantType`: `DEL`    


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
