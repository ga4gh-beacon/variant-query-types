# Beacon VQS Requests

This represents the generic collection of variant parameters supported in Beacon v2+ requests.

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
* `requestProfileId`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/RequestProfileId`    
* `referenceAccession`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/RefgetAccession`    
* `start`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/SequenceStart`    
* `end`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/SequenceEnd`    
* `sequence`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/Sequence`    
* `copyChange`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/CopyChange`    
* `adjacencyAccession`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/AdjacencyAccession`    
* `adjacencyStart`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/AdjacencyStart`    
* `adjacencyEnd`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/AdjacencyEnd`    
* `repeatSubunitLength`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/RepeatSubunitLength`    
* `geneId`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/GeneId`    
* `aminoacidChange`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/AminoacidChange`    
* `genomicAlleleShortForm`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm`    
* `sequenceLength`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/SequenceLength`    
* `variantMinLength`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/VariantMinLength`    
* `variantMaxLength`:    
    - `$ref`: `./common/requestParameterComponents.yaml#/$defs/VariantMaxLength`    


## Beacon v2+/VQS "VRSified" Request Examples



### Query for a focal deletion involving TP53
#### Solution using `VQSgeneIdRequest` with `geneId`
Query for a deletion involving TP53 by using the HUGO name to specify the gene. This request does not provide coordinates so on the server side matching has to be performed from annotated variants or by retrieving the gene's coordinates and creating internally a type of range request. Here we're also  limiting the size of the CNV to a typical "focal deletion" with a lower minimum size of 1kb (to avoid noise and non-structural variants) and an upper limit of 3Mb (to avoid large chromosomal deletions).
#### Request 
* `requestType`: `VQSgeneIdRequest`    
* `geneId`: `TP53`    
* `copyChange`: `EFO:0030067`    
* `variantMinLength`: `1000`    
* `variantMaxLength`: `3000000`    
