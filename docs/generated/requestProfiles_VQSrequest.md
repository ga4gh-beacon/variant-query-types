# Beacon VQS Requests

The `VQSrequest` type represents the generic collection of variant parameters
supported in Beacon v2+ requests. These include parameters with close alignment
to VRS v2 concepts and replacing some Beacon v1/v2 generics with tighter
definitions (e.g. `referenceAccession` instead of `referenceName` and `accession`
or `copyChange` for a specific subset of former `variantType` values) but also
keep some conceptsm beyond VRS scope or specifically geared towards query
applications (`geneId`, `sequenceLength`)


For the parameter definitions please see the [`requestParameterComponents` page.](../requestParameterComponents/)

## VQSrequest Parameters

    

#### `requestProfile`: [./requestParameterComponents.yaml#/$defs/RequestProfileId](../requestParameterComponents#requestprofileid)    
    

#### `referenceAccession`: [./requestParameterComponents.yaml#/$defs/RefgetAccession](../requestParameterComponents#refgetaccession)    
    

#### `startPos`: [./requestParameterComponents.yaml#/$defs/SequenceStart](../requestParameterComponents#sequencestart)    
    

#### `endPos`: [./requestParameterComponents.yaml#/$defs/SequenceEnd](../requestParameterComponents#sequenceend)    
    

#### `startRange`: [./requestParameterComponents.yaml#/$defs/Range](../requestParameterComponents#range)    
    

#### `endRange`: [./requestParameterComponents.yaml#/$defs/Range](../requestParameterComponents#range)    
    

#### `sequence`: [./requestParameterComponents.yaml#/$defs/Sequence](../requestParameterComponents#sequence)    
    

#### `copyChange`: [./requestParameterComponents.yaml#/$defs/CopyChange](../requestParameterComponents#copychange)    
    

#### `adjacencyAccession`: [./requestParameterComponents.yaml#/$defs/AdjacencyAccession](../requestParameterComponents#adjacencyaccession)    
    

#### `adjacencyRange`: [./requestParameterComponents.yaml#/$defs/Range](../requestParameterComponents#range)    
    

#### `repeatSubunitCount`: [./requestParameterComponents.yaml#/$defs/RepeatSubunitCount](../requestParameterComponents#repeatsubunitcount)    
    

#### `repeatSubunitLength`: [./requestParameterComponents.yaml#/$defs/RepeatSubunitLength](../requestParameterComponents#repeatsubunitlength)    
    

#### `geneId`: [./requestParameterComponents.yaml#/$defs/GeneId](../requestParameterComponents#geneid)    
    

#### `aminoacidChange`: [./requestParameterComponents.yaml#/$defs/AminoacidChange](../requestParameterComponents#aminoacidchange)    
    

#### `genomicAlleleShortForm`: [./requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm](../requestParameterComponents#genomicalleleshortform)    
    

#### `sequenceLength`: [./requestParameterComponents.yaml#/$defs/SequenceLength](../requestParameterComponents#sequencelength)    
    

#### `vrsType`: [./requestParameterComponents.yaml#/$defs/VRStype](../requestParameterComponents#vrstype)    
    

#### `genomicFeature`: [./requestParameterComponents.yaml#/$defs/GenomicFeature](../requestParameterComponents#genomicfeature)    
    

#### `molecularEffect`: [./requestParameterComponents.yaml#/$defs/MolecularEffect](../requestParameterComponents#moleculareffect)    
    

#### `phenoClinicEffect`: [./requestParameterComponents.yaml#/$defs/PhenoClinicEffect](../requestParameterComponents#phenocliniceffect)    

## Beacon v2+/VQS "VRSified" Request Examples



### Copy number gains involving the _whole_ locus _chr2:54,700,000-63,900,000_

#### Solution for `VQSrequest` using `start` and `end` ranges (`VQScopyChangeRequest`)

The query has to indicate the involved genomic region by positions as well as the
type of change. Here, matched duplication events start 5\` of the region and end 3\`
of it. For capturing any event upt to the complete chromosome duplication this
requires knowledge about the maximum value (_i.e._ chromosome base length; using a
random very large number might fail depending on the implementation).

The example uses `"copyChange": "EFO:0030070"` for `copy number gain` as specified in the
[VRS definitions](https://vrs.ga4gh.org/en/latest/terms_and_model.html#systemic-variation).
#### Request 

    
* `requestProfile`: `VQScopyChangeRequest`    


    
* `referenceAccession`: `refseq:NC_000002.12`    


    
* `start`:     
    - `0`    
    - `54700000`        


    
* `end`:     
    - `63900000`    
    - `242193529`        


    
* `copyChange`: `EFO:0030070`    


    
* `vrsType`: `CopyNumberChange`    




##### GET query string
```
?requestProfile=VQScopyChangeRequest&referenceAccession=refseq:NC_000002.12&start=0,54700000&end=63900000,242193529&copyChange=EFO:0030070&vrsType=CopyNumberChange
```



##### POST query component 
```json
{
    "copyChange": "EFO:0030070",
    "end": [
        63900000,
        242193529
    ],
    "referenceAccession": "refseq:NC_000002.12",
    "requestProfile": "VQScopyChangeRequest",
    "start": [
        0,
        54700000
    ],
    "vrsType": "CopyNumberChange"
}
```


### Focal high-level deletion involving the _CDKN2A_ locus

#### Solution for `VQSrequest` using `start` and `end` ranges (`VQScopyChangeRequest`)

To match deletion variants overlapping the CDKN2A gene's coding region (CDR) with
at least a single base, but limited to "focal" hits (here i.e. <= ~2Mbp in size)
a bracket query is constructed where the `start` range goes  from ~1Mb 5\'
of the CDKN2A CDR until the end of the CDR and the `end` range goes from the
start of the CDR to ~1Mb 3\' of the gene. 

The query uses `"copyChange": "EFO:0020073"` for `high-level copy number loss`
as specified in the [VRS definitions](https://vrs.ga4gh.org/en/latest/terms_and_model.html#systemic-variation).
With hierarchical expansion of this term explicit complete genomic deletions
(`EFO:0030069`) should be retrieved too.
#### Request 

    
* `requestProfile`: `VQScopyChangeRequest`    


    
* `referenceAccession`: `refseq:NC_000002.12`    


    
* `start`:     
    - `21000001`    
    - `21975098`        


    
* `end`:     
    - `21967753`    
    - `23000000`        


    
* `copyChange`: `EFO:0020073`    


    
* `vrsType`: `CopyNumberChange`    




##### GET query string
```
?requestProfile=VQScopyChangeRequest&referenceAccession=refseq:NC_000002.12&start=21000001,21975098&end=21967753,23000000&copyChange=EFO:0020073&vrsType=CopyNumberChange
```



##### POST query component 
```json
{
    "copyChange": "EFO:0020073",
    "end": [
        21967753,
        23000000
    ],
    "referenceAccession": "refseq:NC_000002.12",
    "requestProfile": "VQScopyChangeRequest",
    "start": [
        21000001,
        21975098
    ],
    "vrsType": "CopyNumberChange"
}
```


### Query for a missense variant in DMD

#### Using `VQSgeneMolecularEffectRequest` with `geneId` and `molecularEffect`

Query for a missense mutation involving TP53 by using the HUGO name to specify the
gene and the Sequence Ontology id to match missense mutations. This request
requires that the server has indexed variants with molecular effects.
#### Request 

    
* `requestType`: `VQSgeneMolecularEffectRequest`    


    
* `geneId`: `DMD`    


    
* `molecularEffect`: `SO:0001583`    




##### GET query string
```
?requestType=VQSgeneMolecularEffectRequest&geneId=DMD&molecularEffect=SO:0001583
```



##### POST query component 
```json
{
    "geneId": "DMD",
    "molecularEffect": "SO:0001583",
    "requestType": "VQSgeneMolecularEffectRequest"
}
```


### Find  t(8;14)(q24;q32) translocations

#### Solution for `VQSrequest` using genomic ranges (`VQSadjacencyRequest`)

This is a query for translocations between the MYC and IgH loci, where the
breakpoints are loosely defined through there well known cytogenetic bands.
The query here follows the VRS adjacency model. In contrast to the VRS
representational model, here:    


- VRS uses an array of 2 genomic locations while Beacon names the location
  parameters individually (using "adjacency..." for the second partner)    
- VRS explicitely encodes directionality by using either `start` or `end`
  position parameters (integers or ranges) while this query example creates
  non-directional ranges on both sides since directionality might not be known,
  the storage system might not encode this or all options could be of interest    
#### Request 

    
* `requestProfile`: `VQSadjacencyRequest`    


    
* `referenceAccession`: `refseq:NC_000008.11`    


    
* `start`: `116700000`    


    
* `end`: `145138636`    


    
* `adjacencyAccession`: `refseq:NC_000014.9`    


    
* `adjacencyStart`: `89300000`    


    
* `adjacencyEnd`: `107043718`    


    
* `vrsType`: `Adjacency`    




##### GET query string
```
?requestProfile=VQSadjacencyRequest&referenceAccession=refseq:NC_000008.11&start=116700000&end=145138636&adjacencyAccession=refseq:NC_000014.9&adjacencyStart=89300000&adjacencyEnd=107043718&vrsType=Adjacency
```



##### POST query component 
```json
{
    "adjacencyAccession": "refseq:NC_000014.9",
    "adjacencyEnd": 107043718,
    "adjacencyStart": 89300000,
    "end": 145138636,
    "referenceAccession": "refseq:NC_000008.11",
    "requestProfile": "VQSadjacencyRequest",
    "start": 116700000,
    "vrsType": "Adjacency"
}
```


### `CAG` repeat in the first exon of the huntingtin gene (HTT)

The gene HTT is located at position 4p16.3. In individuals without Huntington's
disease, this CAG segment is typically repeated 10 to 35 times. Expansions
beyond 35 copys are associated with the development of Huntington's disease.

Examples for query parameters are:    


* GeneId: HTT   
* referenceAccession: refseq:NC_000004.12   
* start: 3074681    
* end: 3243960    
* RepeatSubunitLength: 3 (CAG)    
* RepeatSubunitCount: [36, 250] (not yet defined in VRS or Beacon)    
* SequenceLength:  [105, 750]    

See also the [genome browser material](https://genome.ucsc.edu/training/education/cag.html).

#### Solution using `VQSsequenceRepeatRequest` with locus and `sequenceLength`

This example uses the HTT genome position and a range of (extended) sequence
lengths to match against a `ReferenceLengthExpression` since the VRS v2 model
does not contain a "repeat count" concept but only the overall length and
unit length (as well as the sequence).

TODO: Limit location to first exon?
#### Request 

    
* `requestProfile`: `VQSsequenceRepeatRequest`    


    
* `referenceAccession`: `refseq:NC_000004.12`    


    
* `start`: `3074681`    


    
* `end`: `3243960`    


    
* `repeatSubunitLength`: `3`    


    
* `sequenceLength`:     
    - `105`    
    - `750`        


    
* `vrsType`: `ReferenceLengthExpression`    




##### GET query string
```
?requestProfile=VQSsequenceRepeatRequest&referenceAccession=refseq:NC_000004.12&start=3074681&end=3243960&repeatSubunitLength=3&sequenceLength=105,750&vrsType=ReferenceLengthExpression
```



##### POST query component 
```json
{
    "end": 3243960,
    "referenceAccession": "refseq:NC_000004.12",
    "repeatSubunitLength": 3,
    "requestProfile": "VQSsequenceRepeatRequest",
    "sequenceLength": [
        105,
        750
    ],
    "start": 3074681,
    "vrsType": "ReferenceLengthExpression"
}
```


### `CAG` repeat in the first exon of the huntingtin gene (HTT)

For details see above. 

#### Solution using `VQSsequenceRepeatRequest` with `geneId` and `sequenceLength`

Here instead of the position simply the gene symbol is being used.
#### Request 

    
* `requestProfile`: `VQSsequenceRepeatRequest`    


    
* `geneId`: `HTT`    


    
* `repeatSubunitLength`: `3`    


    
* `sequenceLength`:     
    - `105`    
    - `750`        


    
* `vrsType`: `ReferenceLengthExpression`    




##### GET query string
```
?requestProfile=VQSsequenceRepeatRequest&geneId=HTT&repeatSubunitLength=3&sequenceLength=105,750&vrsType=ReferenceLengthExpression
```



##### POST query component 
```json
{
    "geneId": "HTT",
    "repeatSubunitLength": 3,
    "requestProfile": "VQSsequenceRepeatRequest",
    "sequenceLength": [
        105,
        750
    ],
    "vrsType": "ReferenceLengthExpression"
}
```


### `CGG` trinucleotide repeat expansion in the FMR1 gene

A `CGG` trinucleotide repeat expansion in the FMR1 gene on the X chromosome
(Xq27.3) is known to cause Fragile X Syndrome (FXS). CGG repeating less than
44 times are stable across generations.

#### Solution using `VQSsequenceRepeatRequest` with `geneId` and `sequenceLength`

Similarly to the `HTT` example here a `geneId` is used to specify the gene
and a range of sequence lengths is used to match against a `ReferenceLengthExpression`.
#### Request 

    
* `requestProfile`: `VQSsequenceRepeatRequest`    


    
* `geneId`: `FMR1`    


    
* `repeatSubunitLength`: `3`    


    
* `sequenceLength`:     
    - `130`    
    - `600`        


    
* `vrsType`: `ReferenceLengthExpression`    




##### GET query string
```
?requestProfile=VQSsequenceRepeatRequest&geneId=FMR1&repeatSubunitLength=3&sequenceLength=130,600&vrsType=ReferenceLengthExpression
```



##### POST query component 
```json
{
    "geneId": "FMR1",
    "repeatSubunitLength": 3,
    "requestProfile": "VQSsequenceRepeatRequest",
    "sequenceLength": [
        130,
        600
    ],
    "vrsType": "ReferenceLengthExpression"
}
```


### Query for a focal deletion involving TP53

#### Solution using `VQSgeneIdRequest` with `geneId`

Query for a deletion involving TP53 by using the HUGO name to specify the
gene. This request does not provide coordinates so on the server side matching
has to be performed from annotated variants or by retrieving the gene's
coordinates and creating internally a type of range request. Here we're also 
limiting the size of the CNV to a typical "focal deletion" with a lower minimum
size of 1kb (to avoid noise and non-structural variants) and an upper limit
of 3Mb (to avoid large chromosomal deletions).
#### Request 

    
* `requestType`: `VQSgeneIdRequest`    


    
* `geneId`: `TP53`    


    
* `copyChange`: `EFO:0030067`    


    
* `sequenceLength`:     
    - `1000`    
    - `3000000`        


    
* `vrsType`: `CopyNumberChange`    




##### GET query string
```
?requestType=VQSgeneIdRequest&geneId=TP53&copyChange=EFO:0030067&sequenceLength=1000,3000000&vrsType=CopyNumberChange
```



##### POST query component 
```json
{
    "copyChange": "EFO:0030067",
    "geneId": "TP53",
    "requestType": "VQSgeneIdRequest",
    "sequenceLength": [
        1000,
        3000000
    ],
    "vrsType": "CopyNumberChange"
}
```
