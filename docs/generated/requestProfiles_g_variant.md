# Beacon v2 Requests

This represents the generic collection of variant parameters allowed in Beacon v2 requests.

## g_variant Parameters

* `assemblyId`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/Assembly`    
* `referenceName`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/RefSeqId`    
* `referenceBases`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/ReferenceBases`    
* `alternateBases`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/AlternateBases`    
* `variantType`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/VariantType`    
* `start`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/Start`    
* `end`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/End`    
* `geneId`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/GeneId`    
* `aminoacidChange`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/AminoacidChange`    
* `genomicAlleleShortForm`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm`    
* `variantMinLength`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/VariantMinLength`    
* `variantMaxLength`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/VariantMaxLength`    


## Beacon v2 Request Examples



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


### Query for a deletion involving TP53
#### Solution `g_variant` with `geneId` (`BV2geneIdRequest`)
Query for a deletion involving TP53 by using the HUGO name to specify the gene. This request does not provide coordinates so on the server side matching has to be performed from annotated variants or by retrieving the gene's coordinates and creating internally a type of range request.
#### Request 
* `geneId`: `TP53`    
* `variantType`: `DEL`    


### Find insertion events in TP53
#### Solution using `g_variant` with `geneId` (`BV2geneIdRequest`)
Query for a deletion involving TP53 by using the HUGO name to specify the gene. This request does not provide coordinates so on the server side matching has to be performed from annotated variants or by retrieving the gene's coordinates and creating internally a type of range request.
The "insertion" type is here provided through the Sequence Ontology term `SO:0000667` (which has to be supported by the beacon server, either in the annotation or through mapping to the internal vocabulary).
#### Request 
* `geneId`: `TP53`    
* `variantType`: `SO:0000667`    
