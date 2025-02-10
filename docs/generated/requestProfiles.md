# Request Profile Definitions

## `g_variant` 

#### Description
This represents the generic collection of variant parameters allowed in Beacon v2 requests.    

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
* `examples`:    
    - `$ref`: `../examples/g_variant.yaml#/examples`    

## `VQSrequest` 

#### Description
The `VQSrequest` type represents the generic collection of variant parameters supported in Beacon v2+ requests. These include parameters with close alignment to VRS v2 concepts and replacing some Beacon v1/v2 generics with tighter definitions (e.g. `referenceAccession` instead of `referenceName` and `accession` or `copyChange` for a specific subset of former `variantType` values) but also keep some conceptsm beyond VRS scope or specifically geared towards query applications (`geneId`, `sequenceLength`)    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'$ref': './requestParameterComponents.yaml#/$defs/RequestProfileId'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefgetAccession'`      
    - `start`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceStart'`      
    - `end`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceEnd'`      
    - `sequence`: `'$ref': './requestParameterComponents.yaml#/$defs/Sequence'`      
    - `copyChange`: `'$ref': './requestParameterComponents.yaml#/$defs/CopyChange'`      
    - `adjacencyAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/AdjacencyAccession'`      
    - `adjacencyStart`: `'$ref': './requestParameterComponents.yaml#/$defs/AdjacencyStart'`      
    - `adjacencyEnd`: `'$ref': './requestParameterComponents.yaml#/$defs/AdjacencyEnd'`      
    - `repeatSubunitCount`: `'$ref': './requestParameterComponents.yaml#/$defs/RepeatSubunitCount'`      
    - `repeatSubunitLength`: `'$ref': './requestParameterComponents.yaml#/$defs/RepeatSubunitLength'`      
    - `geneId`: `'$ref': './requestParameterComponents.yaml#/$defs/GeneId'`      
    - `aminoacidChange`: `'$ref': './requestParameterComponents.yaml#/$defs/AminoacidChange'`      
    - `genomicAlleleShortForm`: `'$ref': './requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm'`      
    - `sequenceLength`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceLength'`      
    - `vrsType`: `'$ref': './requestParameterComponents.yaml#/$defs/VRStype'`    

## `BV2alleleRequest` 
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'description': 'Note: The `requestProfile` parameter had not been defined for Beacon v2.0 and therefore in _senso stricto_ is not part of requests only relying on v2 parameters.', 'const': 'BV2alleleRequest'`      
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
A typical Beacon v2 request for matching variations where start and end fall in a genomic range. Here, the approximate or varying positions for variation start and end are queried through brackets, _i.e._ by using 2 values for `start` and `end` each. This is a typical scenario in querying for CNVs where the `variantType` parameter indicates the relative change in genomic copy number through either VCF derived string parameters or, preferably, EFO terms (pls. refer to the class definition.) Since a bracket request is a positional query for varying sequence extend no `sequence` parameter should be used.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'BV2bracketRequest'`      
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
Beacon Range Queries are supposed to return matches of any variant with at least partial overlap of the sequence range specified by `referenceName`, `start` and end `parameters`. Additional qualifiers such as `variantType` or length of the affected sequence can be used to further restrict the returned results. For this request type `start` and `end` with a single position are used, _i.e._ a subset of the `start` and `end` specifications.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'BV2rangeRequest'`      
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

## `BV2variantIdRequest` 

#### Description
A typical Beacon v2 request for matching variations by their `variantId`. This request is used to retrieve a specific variant by its identifier.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'BV2variantIdRequest'`      
    - `variantId`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantId'`    

## `BV2aminoacidChangeRequest` 

#### Description
A Beacon v2 request for amino acid change queries, e.g. for the retrieval of all variants leading to specific amino acid change. The request may be restricted by additionally providing the gene ID.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'BV2aminoacidChangeRequest'`      
    - `aminoacidChange`: `'$ref': './requestParameterComponents.yaml#/$defs/AminoacidChange'`      
    - `geneId`: `'$ref': './requestParameterComponents.yaml#/$defs/GeneId'`    
    
* `required`:     
    - `aminoacidChange`        

## `BV2genomicAlleleShortFormRequest` 
    
* `type`: `object`    
* `properties`:    
    - `genomicAlleleShortForm`: `'$ref': './requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm'`    

## `BV2geneIdRequest` 

#### Description
A typical Beacon v2.n request for gene queries, e.g. for the retrieval of all variants in a gene or variants restricted by additional parameters such `variantType` or length of the affected sequence. TODO: Evaluate to split into more basic `GeneIdRequest` and specialized
      requests requiring an effect component.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'BV2geneIdRequest'`      
    - `geneId`: `'$ref': './requestParameterComponents.yaml#/$defs/GeneId'`      
    - `variantType`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantType'`      
    - `variantMinLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMinLength'`      
    - `variantMaxLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMaxLength'`    
    
* `required`:     
    - `geneId`        

## `VQSalleleRequest` 

#### Description
A Beacon v2+ sequence query. It is in its scope similar to the Beacon v1/v2 allele requests but replaces the original parameters with VRS v2 concepts.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'VQSalleleRequest'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefgetAccession'`      
    - `start`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceStart'`      
    - `end`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceEnd'`      
    - `sequence`: `'$ref': './requestParameterComponents.yaml#/$defs/Sequence'`      
    - `vrsType`: `'const': 'Allele'`    
    
* `required`:     
    - `referenceAccession`    
    - `start`    
    - `sequence`        

## `VQScopyChangeRequest` 

#### Description
A typical Beacon v2.n request for copy number variations (CNVs) queries approximate positions for CNV start and end regions through use of the `Range` type. The `copyChange` parameter indicates the relative change in genomic copy number (pls. refer to the class definition.)    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'VQScopyChangeRequest'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefgetAccession'`      
    - `start`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceStart'`      
    - `end`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceEnd'`      
    - `copyChange`: `'$ref': './requestParameterComponents.yaml#/$defs/CopyChange'`      
    - `variantMinLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMinLength'`      
    - `variantMaxLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMaxLength'`      
    - `vrsType`: `'const': 'CopyNumberChange'`    
    
* `required`:     
    - `referenceAccession`    
    - `start`    
    - `end`    
    - `copyChange`        

## `VQSrangeRequest` 

#### Description
Beacon Range Queries are supposed to return matches of any variant with at least partial overlap of the sequence range specified by `referenceAccession`, `start` and `end` parameters. Additional qualifiers such as `copyChange` or length of the affected sequence can be used to further restrict the returned results. For this request type usually `start` and `end` with a single position are used, _i.e._ a subset of the `start` and `end` specifications. However, 

##### TODO
    
* Evaluate to split into more basic `RangeRequest` and specialized
  requests requiring an effect component
    
* Review current VRS v2 and upcoming versions for optoions to express
  types of variants beyond the `copyChange` parameter    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'VQSrangeRequest'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefSeqId'`      
    - `start`: `'type': 'integer'`      
    - `end`: `'type': 'integer'`      
    - `variantMinLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMinLength'`      
    - `variantMaxLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMaxLength'`      
    - `vrsType`: `'$ref': './requestParameterComponents.yaml#/$defs/VRStype'`    
    
* `required`:     
    - `referenceAccession`    
    - `start`    
    - `end`    
    - `vrsType`        

## `VQSadjacencyRequest` 

#### Description
A typical Beacon v2.n request for sequence adjacency queries, e.g. for the retrieval of chromosomal translocation events or sequence fusions. TODO: In VRS v2 there is an implicit sequence directionality from the use of either start or end parameters for either side of the adjacency. This might be problematic on the query side where in many instances just the approximate position of the (fused) breakpoints maight be of interest. This needs additional clarification (e.g. use of integer `start` and `end`, `adjacencyStart` and  `adjecencyEnd` parameters to indicate direction independent matching).    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'VQSadjacencyRequest'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefgetAccession'`      
    - `start`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceStart'`      
    - `end`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceEnd'`      
    - `adjacencyAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/AdjacencyAccession'`      
    - `adjacencyStart`: `'$ref': './requestParameterComponents.yaml#/$defs/AdjacencyStart'`      
    - `adjacencyEnd`: `'$ref': './requestParameterComponents.yaml#/$defs/AdjacencyEnd'`      
    - `vrsType`: `'const': 'Adjacency'`    

## `VQSsequenceRepeatRequest` 

#### Description
A Beacon v2.n request for sequence repeat queries, e.g. for the retrieval of tandem repeat expansions or other sequence repeat events.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'VQSsequenceRepeatRequest'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefgetAccession'`      
    - `start`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceStart'`      
    - `end`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceEnd'`      
    - `repeatSubunitLength`: `'$ref': './requestParameterComponents.yaml#/$defs/RepeatSubunitLength'`      
    - `repeatSubunitCount`: `'$ref': './requestParameterComponents.yaml#/$defs/RepeatSubunitCount'`      
    - `vrsType`: `'const': 'SequenceRepeat'`    

## `VQSgeneIdRequest` 

#### Description
A typical Beacon v2.n request for gene queries, e.g. for the retrieval of all variants in a gene or variants restricted by additional parameters such as CNV type (`copyChange`) or length of the affected sequence. TODO: Evaluate to split into more basic `GeneIdRequest` and specialized
      requests requiring an effect component.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'VQSgeneIdRequest'`      
    - `geneId`: `'$ref': './requestParameterComponents.yaml#/$defs/GeneId'`      
    - `copyChange`: `'$ref': './requestParameterComponents.yaml#/$defs/CopyChange'`      
    - `variantMinLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMinLength'`      
    - `variantMaxLength`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantMaxLength'`      
    - `molecularEffect`: `'$ref': './requestParameterComponents.yaml#/$defs/molecularEffect'`      
    - `clinicalRelevance`: `'$ref': './requestParameterComponents.yaml#/$defs/clinicalRelevance'`      
    - `vrsType`: `'$ref': './requestParameterComponents.yaml#/$defs/VRStype'`    
    
* `required`:     
    - `geneId`        

## `BV2multivarsRequest` 

#### Description
This multi variant query is a collection of individual variant queries based on the Beacon v2 parameters (`g_variant`). Status: Proposed for evaluation for Beacon v2.n or v3.0 (but potentially
        skipped in favor of the `VQSmultivarRequest` queries).    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'BV2multivarsRequest'`      
    - `variantLogic`: `'description': 'The logic to apply to the set of variants in the query. The default is to apply the AND logic, meaning that all **samples** (i.e. biosamples, individuals or analyses) must fulfil the query criteria: * with a (default) AND logic and "biosamples" as requested entity \n  `biosample_id` values from the individual variant query responses\n  will be intersected\n* with an OR logic and "analyses" as requested entity `analysis_id`\n  values from the individual variant query responses will be concatenated\nNote: The `variantLogic` parameter is not defined in the current\n      `requestParameterComponents.yaml` file yet due to the very experimental\n      and tentative nature of this proposal.', 'type': 'string', 'enum': ['AND', 'OR'], 'default': 'AND'`      
    - `queries`: `'type': 'array', 'items': '$ref': '#/$defs/g_variant'`    

## `VQSmultivarRequest` 

#### Description
This multi variant query is a collection of individual variant queries based on the Beacon v2+ "VQS" query patterns. Status: Proposed for evaluation for Beacon v2.n or v3.0    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfileId`: `'const': 'VQSmultivarRequest'`      
    - `variantLogic`: `'type': 'string', 'enum': ['AND', 'OR'], 'default': 'AND'`      
    - `queries`: `'type': 'array', 'items': 'anyOf': ['$ref': '#/$defs/VQSalleleRequest', '$ref': '#/$defs/VQScopyChangeRequest', '$ref': '#/$defs/VQSadjacencyRequest', '$ref': '#/$defs/VQSgeneIdRequest', '$ref': '#/$defs/BV2variantIdRequest', '$ref': '#/$defs/BV2aminoacidChangeRequest', '$ref': '#/$defs/BV2genomicAlleleShortFormRequest']`    
