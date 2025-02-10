# Request Profile: `VQSsequenceRepeatRequest`

A Beacon v2.n request for sequence repeat queries, e.g. for the retrieval of tandem repeat expansions or other sequence repeat events.

### `CAG` repeat in the first exon of the huntingtin gene (HTT)
The gene HTT is located at position 4p16.3. In individuals without Huntington's disease, this CAG segment is typically repeated 10 to 35 times. Expansions beyond 35 copys are associated with the development of Huntington's disease.
Examples for query parameters are:
* GeneId: HTT * referenceAccession: refseq:NC_000004.12 * start: 3074681 * end: 3243960 * RepeatSubunitLength: 3 (CAG) * RepeatSubunitCount: [36, 250] (not yet defined in VRS or Beacon) * SequenceLength:  [105, 750]
See also the [genome browser material](https://genome.ucsc.edu/training/education/cag.html).
#### Solution using `VQSsequenceRepeatRequest` with locus and `sequenceLength`
This example uses the HTT genome position and a range of (extended) sequence lengths to match against a `ReferenceLengthExpression` since the VRS v2 model does not contain a "repeat count" concept but only the overall length and unit length (as well as the sequence).
TODO: Limit location to first exon?
#### Request 
    
* `requestProfileId`: `VQSsequenceRepeatRequest`    
    
* `referenceAccession`: `refseq:NC_000004.12`    
    
* `start`: `3074681`    
    
* `end`: `3243960`    
    
* `repeatSubunitLength`: `3`    
    
* `sequenceLength`:     
    - `105`    
    - `750`        
    
* `vrsType`: `ReferenceLengthExpression`    

##### GET query string
```requestProfileId=VQSsequenceRepeatRequest&referenceAccession=refseq:NC_000004.12&start=3074681&end=3243960&repeatSubunitLength=3&sequenceLength=105,750&vrsType=ReferenceLengthExpression```

##### POST query component 
```{
    "end": 3243960,
    "referenceAccession": "refseq:NC_000004.12",
    "repeatSubunitLength": 3,
    "requestProfileId": "VQSsequenceRepeatRequest",
    "sequenceLength": [
        105,
        750
    ],
    "start": 3074681,
    "vrsType": "ReferenceLengthExpression"
}```


### `CAG` repeat in the first exon of the huntingtin gene (HTT)
For details see above. 
#### Solution using `VQSsequenceRepeatRequest` with `geneId` and `sequenceLength`
Here instead of the position simply the gene symbol is being used.
#### Request 
    
* `requestProfileId`: `VQSsequenceRepeatRequest`    
    
* `geneId`: `HTT`    
    
* `repeatSubunitLength`: `3`    
    
* `sequenceLength`:     
    - `105`    
    - `750`        
    
* `vrsType`: `ReferenceLengthExpression`    

##### GET query string
```requestProfileId=VQSsequenceRepeatRequest&geneId=HTT&repeatSubunitLength=3&sequenceLength=105,750&vrsType=ReferenceLengthExpression```

##### POST query component 
```{
    "geneId": "HTT",
    "repeatSubunitLength": 3,
    "requestProfileId": "VQSsequenceRepeatRequest",
    "sequenceLength": [
        105,
        750
    ],
    "vrsType": "ReferenceLengthExpression"
}```


### `CGG` trinucleotide repeat expansion in the FMR1 gene
A `CGG` trinucleotide repeat expansion in the FMR1 gene on the X chromosome (Xq27.3) is known to cause Fragile X Syndrome (FXS). CGG repeating less than 44 times are stable across generations.
#### Solution using `VQSsequenceRepeatRequest` with `geneId` and `sequenceLength`
Similarly to the `HTT` example here a `geneId` is used to specify the gene and a range of sequence lengths is used to match against a `ReferenceLengthExpression`.
#### Request 
    
* `requestProfileId`: `VQSsequenceRepeatRequest`    
    
* `geneId`: `FMR1`    
    
* `repeatSubunitLength`: `3`    
    
* `sequenceLength`:     
    - `130`    
    - `600`        
    
* `vrsType`: `ReferenceLengthExpression`    

##### GET query string
```requestProfileId=VQSsequenceRepeatRequest&geneId=FMR1&repeatSubunitLength=3&sequenceLength=130,600&vrsType=ReferenceLengthExpression```

##### POST query component 
```{
    "geneId": "FMR1",
    "repeatSubunitLength": 3,
    "requestProfileId": "VQSsequenceRepeatRequest",
    "sequenceLength": [
        130,
        600
    ],
    "vrsType": "ReferenceLengthExpression"
}```
