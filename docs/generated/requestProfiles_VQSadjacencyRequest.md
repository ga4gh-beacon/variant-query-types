# Request Profile: `VQSadjacencyRequest`

A typical Beacon v2.n request for sequence adjacency queries, e.g. for the retrieval of chromosomal translocation events or sequence fusions. TODO: In VRS v2 there is an implicit sequence directionality from the use of either start or end parameters for either side of the adjacency. This might be problematic on the query side where in many instances just the approximate position of the (fused) breakpoints maight be of interest. This needs additional clarification (e.g. use of integer `start` and `end`, `adjacencyStart` and  `adjecencyEnd` parameters to indicate direction independent matching).

### Find  t(8;14)(q24;q32) translocations
#### Solution for `VQSrequest` using genomic ranges (`VQSadjacencyRequest`)
This is a query for translocations between the MYC and IgH loci, where the breakpoints are loosely defined through there well known cytogenetic bands. The query here follows the VRS adjacency model. In contrast to the VRS representational model, here:    

- VRS uses an array of 2 genomic locations while Beacon names the location
  parameters individually (using "adjacency..." for the second partner)    
- VRS explicitely encodes directionality by using either `start` or `end`
  position parameters (integers or ranges) while this query example creates
  non-directional ranges on both sides since directionality might not be known,
  the storage system might not encode this or all options could be of interest    
#### Request 
    
* `requestProfileId`: `VQSadjacencyRequest`    
    
* `referenceAccession`: `refseq:NC_000008.11`    
    
* `start`: `116700000`    
    
* `end`: `145138636`    
    
* `adjacencyAccession`: `refseq:NC_000014.9`    
    
* `adjacencyStart`: `89300000`    
    
* `adjacencyEnd`: `107043718`    
    
* `vrsType`: `Adjacency`    

##### GET query string
```requestProfileId=VQSadjacencyRequest&referenceAccession=refseq:NC_000008.11&start=116700000&end=145138636&adjacencyAccession=refseq:NC_000014.9&adjacencyStart=89300000&adjacencyEnd=107043718&vrsType=Adjacency```

##### POST query component 
```{
    "adjacencyAccession": "refseq:NC_000014.9",
    "adjacencyEnd": 107043718,
    "adjacencyStart": 89300000,
    "end": 145138636,
    "referenceAccession": "refseq:NC_000008.11",
    "requestProfileId": "VQSadjacencyRequest",
    "start": 116700000,
    "vrsType": "Adjacency"
}```
