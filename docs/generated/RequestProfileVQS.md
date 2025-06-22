# Request Profile Definitions
Request profile allow the definition of the structure of genomic variation
queries, the verification of the request structure by the beacons receiving the
request and the exposure of supported request types by beacons and Beacon
aggregators.

## `VQSrequest` 

#### Description
The `VQSrequest` type represents the generic collection of variant parameters  
supported in Beacon v2+ requests. These include parameters with close alignment  
to VRS v2 concepts and replacing some Beacon v1/v2 generics with tighter  
definitions (e.g. `referenceAccession` instead of `referenceName` and `accession`  
or `copyChange` for a specific subset of former `variantType` values) but also  
keep some conceptsm beyond VRS scope or specifically geared towards query  
applications (`geneId`, `sequenceLength`)    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'$ref': './requestParameterComponents.yaml#/$defs/RequestProfileId'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefgetAccession'`      
    - `startPos`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceStart'`      
    - `endPos`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceEnd'`      
    - `startRange`: `'$ref': './requestParameterComponents.yaml#/$defs/Range'`      
    - `endRange`: `'$ref': './requestParameterComponents.yaml#/$defs/Range'`      
    - `sequence`: `'$ref': './requestParameterComponents.yaml#/$defs/Sequence'`      
    - `copyChange`: `'$ref': './requestParameterComponents.yaml#/$defs/CopyChange'`      
    - `adjacencyAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/AdjacencyAccession'`      
    - `adjacencyRange`: `'$ref': './requestParameterComponents.yaml#/$defs/Range'`      
    - `repeatSubunitCount`: `'$ref': './requestParameterComponents.yaml#/$defs/RepeatSubunitCount'`      
    - `repeatSubunitLength`: `'$ref': './requestParameterComponents.yaml#/$defs/RepeatSubunitLength'`      
    - `geneId`: `'$ref': './requestParameterComponents.yaml#/$defs/GeneId'`      
    - `aminoacidChange`: `'$ref': './requestParameterComponents.yaml#/$defs/AminoacidChange'`      
    - `genomicAlleleShortForm`: `'$ref': './requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm'`      
    - `sequenceLength`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceLength'`      
    - `vrsType`: `'$ref': './requestParameterComponents.yaml#/$defs/VRStype'`      
    - `genomicFeature`: `'$ref': './requestParameterComponents.yaml#/$defs/GenomicFeature'`      
    - `molecularEffect`: `'$ref': './requestParameterComponents.yaml#/$defs/MolecularEffect'`      
    - `phenoClinicEffect`: `'$ref': './requestParameterComponents.yaml#/$defs/PhenoClinicEffect'`    

## `VQSvariantIdRequest` 

#### Description
A typical Beacon v2 request for matching variations by their `variantId`.  
This request is used to retrieve a specific variant by its identifier.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'BV2variantIdRequest'`      
    - `variantId`: `'$ref': './requestParameterComponents.yaml#/$defs/VariantId'`    

## `VQSaminoacidChangeRequest` 

#### Description
A Beacon request for amino acid change queries, e.g. for the  
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

## `VQSgenomicAlleleShortFormRequest` 
    
* `type`: `object`    
* `properties`:    
    - `genomicAlleleShortForm`: `'$ref': './requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm'`    

## `VQSgeneIdRequest` 

#### Description
A typical Beacon v2.n request for gene queries, e.g. for the retrieval of  
all variants in a gene or variants restricted by additional parameters  
such as CNV type (`copyChange`) or length of the affected sequence.  
TODO: Evaluate to split into more basic `GeneIdRequest` and specialized  
      requests requiring an effect component.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'VQSgeneIdRequest'`      
    - `geneId`: `'$ref': './requestParameterComponents.yaml#/$defs/GeneId'`      
    - `copyChange`: `'$ref': './requestParameterComponents.yaml#/$defs/CopyChange'`      
    - `sequenceLength`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceLength'`      
    - `molecularEffect`: `'$ref': './requestParameterComponents.yaml#/$defs/molecularEffect'`      
    - `clinicalRelevance`: `'$ref': './requestParameterComponents.yaml#/$defs/clinicalRelevance'`      
    - `vrsType`: `'$ref': './requestParameterComponents.yaml#/$defs/VRStype'`    
    
* `required`:     
    - `geneId`        

## `VQSalleleRequest` 

#### Description
A Beacon v2+ sequence query. It is in its scope similar to the Beacon v1/v2  
allele requests but replaces the original parameters with VRS v2 concepts.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'VQSalleleRequest'`      
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
A typical Beacon v2.n request for copy number variations (CNVs) queries  
approximate positions for CNV start and end regions through use of the  
`Range` type. The `copyChange` parameter indicates the relative change in  
genomic copy number (pls. refer to the class definition.)    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'VQScopyChangeRequest'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefgetAccession'`      
    - `startRange`: `'$ref': './requestParameterComponents.yaml#/$defs/Range'`      
    - `endRange`: `'$ref': './requestParameterComponents.yaml#/$defs/Range'`      
    - `copyChange`: `'$ref': './requestParameterComponents.yaml#/$defs/CopyChange'`      
    - `sequenceLength`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceLength'`      
    - `vrsType`: `'const': 'CopyNumberChange'`    
    
* `required`:     
    - `requestProfile`    
    - `referenceAccession`    
    - `startRange`    
    - `endRange`    
    - `copyChange`        

## `VQSgeneMolecularEffectRequest` 

#### Description
A request for the variation consequence, e.g. for the _molecular_ changes  
caused by the variant.  
  

##### TODO  
  
* Define a clear structure for how request types are constructed with a  
  primacy of *where* the variant is located or *what* happens.     

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'VQSgeneMolecularEffectRequest'`      
    - `molecularEffect`: `'$ref': './requestParameterComponents.yaml#/$defs/MolecularEffect'`      
    - `geneId`: `'$ref': './requestParameterComponents.yaml#/$defs/GeneId'`    
    
* `required`:     
    - `requestProfile`    
    - `molecularEffect`        

## `VQSlocationMolecularEffectRequest` 

#### Description
A request for the variation consequence, e.g. for the _molecular_ changes  
caused by the variant, at a genomic location defined through coordinates.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'VQSlocationMolecularEffectRequest'`      
    - `molecularEffect`: `'$ref': './requestParameterComponents.yaml#/$defs/MolecularEffect'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefSeqId'`      
    - `sequenceRange`: `'$ref': './requestParameterComponents.yaml#/$defs/Range'`    
    
* `required`:     
    - `requestProfile`    
    - `referenceAccession`        

## `VQSrangeRequest` 

#### Description
Beacon Range Queries are supposed to return matches of any variant with at  
least partial overlap of the sequence range specified by `referenceAccession`,  
`start` and `end` parameters. Additional qualifiers such as `copyChange`  
or length of the affected sequence can be used to further restrict the  
returned results.  
For this request type usually `start` and `end` with a single position are used,  
_i.e._ a subset of the `start` and `end` specifications. However,   
  

##### TODO  
  
* Evaluate to split into more basic `RangeRequest` and specialized  
  requests requiring an effect component  
* Review current VRS v2 and upcoming versions for optoions to express  
  types of variants beyond the `copyChange` parameter    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'VQSrangeRequest'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefSeqId'`      
    - `sequenceRange`: `'$ref': './requestParameterComponents.yaml#/$defs/Range'`      
    - `sequenceLength`: `'$ref': './requestParameterComponents.yaml#/$defs/SequenceLength'`      
    - `vrsType`: `'$ref': './requestParameterComponents.yaml#/$defs/VRStype'`    
    
* `required`:     
    - `requestProfile`    
    - `referenceAccession`    
    - `sequenceRange`        

## `VQSadjacencyRequest` 

#### Description
A typical Beacon v2.n request for sequence adjacency queries, e.g. for  
the retrieval of chromosomal translocation events or sequence fusions.  
  
TODO: In VRS v2 there is an implicit sequence directionality from the use  
of either start or end parameters for either side of the adjacency. This  
might be problematic on the query side where in many instances just the  
approximate position of the (fused) breakpoints maight be of interest.  
  
This might need additional clarification (e.g. use of `startRange` or  
`endRange`, `adjacencyStartRange` and `adjecencyEndRange` parameters to  
indicate direction dependent matching).    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'VQSadjacencyRequest'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefgetAccession'`      
    - `sequenceRange`: `'$ref': './requestParameterComponents.yaml#/$defs/Range'`      
    - `adjacencyAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/AdjacencyAccession'`      
    - `adjacencyRange`: `'$ref': './requestParameterComponents.yaml#/$defs/Range'`      
    - `vrsType`: `'const': 'Adjacency'`    
    
* `required`:     
    - `requestProfile`    
    - `referenceAccession`    
    - `sequenceRange`    
    - `adjacencyAccession`    
    - `adjacencyRange`    
    - `vrsType`        

## `VQSterminusRequest` 

#### Description
A Beacon v2.n request for a sequence terminus, _i.e._ the end of a sequence.  
An example would be the match of chromosomal breakpoints terminating the  
derived chromosome w/o resulting sequence fusion.  
  
TODO: As in adjacency requests one could use `startRange` or `endRange`  
to limit the side of the breakpoint.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'VQSterminusRequest'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefgetAccession'`      
    - `sequenceRange`: `'$ref': './requestParameterComponents.yaml#/$defs/Range'`      
    - `vrsType`: `'const': 'Terminus'`    
    
* `required`:     
    - `requestProfile`    
    - `referenceAccession`    
    - `sequenceRange`    
    - `vrsType`        

## `VQSsequenceRepeatRequest` 

#### Description
A Beacon v2.n request for sequence repeat queries, e.g. for the  
retrieval of tandem repeat expansions or other sequence repeat events.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'VQSsequenceRepeatRequest'`      
    - `referenceAccession`: `'$ref': './requestParameterComponents.yaml#/$defs/RefgetAccession'`      
    - `sequenceRange`: `'$ref': './requestParameterComponents.yaml#/$defs/Range'`      
    - `repeatSubunitLength`: `'$ref': './requestParameterComponents.yaml#/$defs/RepeatSubunitLength'`      
    - `repeatSubunitCount`: `'$ref': './requestParameterComponents.yaml#/$defs/RepeatSubunitCount'`      
    - `vrsType`: `'const': 'SequenceRepeat'`    
    
* `required`:     
    - `requestProfile`    
    - `referenceAccession`    
    - `sequenceRange`    
    - `vrsType`        

## `VQSmultivarRequest` 

#### Description
This multi variant query is a collection of individual variant queries  
based on the Beacon v2+ "VQS" query patterns.    

#### Definitions
    
* `type`: `object`    
* `properties`:    
    - `requestProfile`: `'const': 'VQSmultivarRequest'`      
    - `variantLogic`: `'description': 'The logic to apply to the set of variants in the query. The default is\nto apply the AND logic, meaning that all **samples** (i.e. biosamples,\nindividuals or analyses) must fulfil the query criteria:\n* with a (default) AND logic and "biosamples" as requested entity \n  `biosample_id` values from the individual variant query responses\n  will be intersected\n* with an OR logic and "analyses" as requested entity `analysis_id`\n  values from the individual variant query responses will be concatenated\n\n*TODO*: As with filters while there are potential use cases it has to be\nevaluated whether the logic is needed in practice, with view towards\nrequest complexity and stakeholder interest.', 'type': 'string', 'enum': ['AND', 'OR'], 'default': 'AND'`      
    - `queries`: `'type': 'array', 'items': 'anyOf': ['$ref': '#/$defs/VQSrequest', '$ref': '#/$defs/VQSvariantIdRequest', '$ref': '#/$defs/VQSaminoacidChangeRequest', '$ref': '#/$defs/VQSgenomicAlleleShortFormRequest', '$ref': '#/$defs/VQSgeneIdRequest', '$ref': '#/$defs/VQSalleleRequest', '$ref': '#/$defs/VQScopyChangeRequest', '$ref': '#/$defs/VQSgeneMolecularEffectRequest', '$ref': '#/$defs/VQSlocationMolecularEffectRequest', '$ref': '#/$defs/VQSrangeRequest', '$ref': '#/$defs/VQSadjacencyRequest', '$ref': '#/$defs/VQSterminusRequest', '$ref': '#/$defs/VQSsequenceRepeatRequest']`    
