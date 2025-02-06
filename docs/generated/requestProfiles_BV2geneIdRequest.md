# Request Profile: `BV2geneIdRequest`

A typical Beacon v2.n request for gene queries, e.g. for the retrieval of all variants in a gene or variants restricted by additional parameters such `variantType` or length of the affected sequence. TODO: Evaluate to split into more basic `GeneIdRequest` and specialized
      requests requiring an effect component.

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
