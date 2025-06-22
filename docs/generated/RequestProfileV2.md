# Request Profile Definitions

## `g_variant` 

#### Description
This represents the generic collection of variant parameters allowed in  
Beacon v2 requests.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `assemblyId`: `'$ref': './requestParameterComponents.yaml#/$defs/Assembly'`      
    - `referenceName`: `'$ref': './requestParameterComponents.yaml#/$defs/RefSeqId'`      
    - `referenceBases`: `'$ref': './requestParameterComponents.yaml#/$defs/ReferenceBases'`      
    - `alternateBases`: `'$ref': './requestParameterComponents.yaml#/$defs/AlternateBases'`      
    - `variantType`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantType'`      
    - `start`: `'$ref': './requestParameterComponents.yaml#/$defs/Start'`      
    - `end`: `'$ref': './requestParameterComponents.yaml#/$defs/End'`      
    - `geneId`: `'$ref': './requestParameterComponents.yaml#/$defs/GeneId'`      
    - `aminoacidChange`: `'$ref': './requestParameterComponents.yaml#/$defs/AminoacidChange'`      
    - `genomicAlleleShortForm`: `'$ref': './requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm'`      
    - `variantMinLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMinLength'`      
    - `variantMaxLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMaxLength'`    
    

#### `examples`: [../examples/g_variant.yaml#/examples](../examples/g_variant.yaml#/examples)    

## `VariantIdRequest` 

#### Description
A typical Beacon v2 request for matching variations by their `variantId`.  
This request is used to retrieve a specific variant by its identifier.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'BV2variantIdRequest'`      
    - `variantId`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantId'`    

## `AminoacidChangeRequest` 

#### Description
A Beacon v2 request for amino acid change queries, e.g. for the  
retrieval of all variants leading to specific amino acid change. The request  
may be restricted by additionally providing the gene ID.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'BV2aminoacidChangeRequest'`      
    - `aminoacidChange`: `'$ref': './requestParameterComponents.yaml#/$defs/AminoacidChange'`      
    - `geneId`: `'$ref': './requestParameterComponents.yaml#/$defs/GeneId'`    
    
* `required`:     
    - `aminoacidChange`        

## `GenomicAlleleShortFormRequest` 
    
* `type`: `object`    
* `properties`:    
    - `genomicAlleleShortForm`: `'$ref': './requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm'`    

## `GeneIdRequest` 

#### Description
A typical Beacon v2.n request for gene queries, e.g. for the retrieval of  
all variants in a gene or variants restricted by additional parameters  
such `variantType` or length of the affected sequence.  
TODO: Evaluate to split into more basic `GeneIdRequest` and specialized  
      requests requiring an effect component. There is already a type for  
      a `molecularEffectRequest` - see also notes there.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'geneIdRequest'`      
    - `geneId`: `'$ref': './requestParameterComponents.yaml#/$defs/GeneId'`      
    - `variantMinLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMinLength'`      
    - `variantMaxLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMaxLength'`    
    
* `required`:     
    - `geneId`        

## `BV2alleleRequest` 
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'description': 'Note: The `requestProfile` parameter had not been defined for Beacon v2.0\nand therefore in _senso stricto_ is not part of requests only relying\non v2 parameters.', 'const': 'BV2alleleRequest'`      
    - `assemblyId`: `'$ref': './requestParameterComponents.yaml#/$defs/Assembly'`      
    - `referenceName`: `'$ref': './requestParameterComponents.yaml#/$defs/RefSeqId'`      
    - `start`: `'$ref': './requestParameterComponents.yaml#/$defs/Start'`      
    - `referenceBases`: `'$ref': './requestParameterComponents.yaml#/$defs/ReferenceBases'`      
    - `alternateBases`: `'$ref': './requestParameterComponents.yaml#/$defs/AlternateBases'`    
    
* `required`:     
    - `referenceName`    
    - `start`    
    - `alternateBases`        

## `BV2bracketRequest` 

#### Description
A typical Beacon v2 request for matching variations where start and end  
fall in a genomic range. Here, the approximate or varying positions for  
variation start and end are queried through brackets, _i.e._ by using 2  
values for `start` and `end` each. This is a typical scenario in querying  
for CNVs where the `variantType` parameter indicates the relative change in  
genomic copy number through either VCF derived string parameters  
or, preferably, EFO terms (pls. refer to the class definition.)  
Since a bracket request is a positional query for varying sequence extend  
no `sequence` parameter should be used.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'BV2bracketRequest'`      
    - `assemblyId`: `'$ref': './requestParameterComponents.yaml#/$defs/Assembly'`      
    - `referenceName`: `'$ref': './requestParameterComponents.yaml#/$defs/RefSeqId'`      
    - `start`: `'$ref': './requestParameterComponents.yaml#/$defs/Start'`      
    - `end`: `'$ref': './requestParameterComponents.yaml#/$defs/End'`      
    - `variantType`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantType'`      
    - `variantMinLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMinLength'`      
    - `variantMaxLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMaxLength'`    
    
* `required`:     
    - `referenceName`    
    - `start`    
    - `end`    
    - `variantType`        

## `BV2rangeRequest` 

#### Description
Beacon Range Queries are supposed to return matches of any variant with at  
least partial overlap of the sequence range specified by `referenceName`,  
`start` and end `parameters`. Additional qualifiers such as `variantType`  
or length of the affected sequence can be used to further restrict the  
returned results.  
For this request type `start` and `end` with a single position are used,  
_i.e._ a subset of the `start` and `end` specifications.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'BV2rangeRequest'`      
    - `assemblyId`: `'$ref': './requestParameterComponents.yaml#/$defs/Assembly'`      
    - `referenceName`: `'$ref': './requestParameterComponents.yaml#/$defs/RefSeqId'`      
    - `start`: `'type': 'array', 'items': 'type': 'integer', 'minItems': 1, 'maxItems': 1`      
    - `end`: `'type': 'array', 'items': 'type': 'integer', 'minItems': 1, 'maxItems': 1`      
    - `variantType`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantType'`      
    - `variantMinLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMinLength'`      
    - `variantMaxLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMaxLength'`    
    
* `required`:     
    - `referenceName`    
    - `start`    
    - `end`        
