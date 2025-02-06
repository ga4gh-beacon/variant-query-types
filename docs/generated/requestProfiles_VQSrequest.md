# Beacon VQS Request Examples

This represents the generic collection of variant parameters supported in Beacon v2+ requests.



### Query for a focal deletion involving TP53
#### Solution using `VQSgeneIdRequest` with `geneId`
Query for a deletion involving TP53 by using the HUGO name to specify the gene. This request does not provide coordinates so on the server side matching has to be performed from annotated variants or by retrieving the gene's coordinates and creating internally a type of range request. Here we're also  limiting the size of the CNV to a typical "focal deletion" with a lower minimum size of 1kb (to avoid noise and non-structural variants) and an upper limit of 3Mb (to avoid large chromosomal deletions).
#### Request 
* `requestType`: `VQSgeneIdRequest`    
* `geneId`: `TP53`    
* `copyChange`: `EFO:0030067`    
* `variantMinLength`: `1000`    
* `variantMaxLength`: `3000000`    
