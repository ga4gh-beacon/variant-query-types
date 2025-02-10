# Request Profile: `VQSgeneIdRequest`

A typical Beacon v2.n request for gene queries, e.g. for the retrieval of all variants in a gene or variants restricted by additional parameters such as CNV type (`copyChange`) or length of the affected sequence. TODO: Evaluate to split into more basic `GeneIdRequest` and specialized
      requests requiring an effect component.

### Query for a focal deletion involving TP53
#### Solution using `VQSgeneIdRequest` with `geneId`
Query for a deletion involving TP53 by using the HUGO name to specify the gene. This request does not provide coordinates so on the server side matching has to be performed from annotated variants or by retrieving the gene's coordinates and creating internally a type of range request. Here we're also  limiting the size of the CNV to a typical "focal deletion" with a lower minimum size of 1kb (to avoid noise and non-structural variants) and an upper limit of 3Mb (to avoid large chromosomal deletions).
#### Request 
    
* `requestType`: `VQSgeneIdRequest`    
    
* `geneId`: `TP53`    
    
* `copyChange`: `EFO:0030067`    
    
* `variantMinLength`: `1000`    
    
* `variantMaxLength`: `3000000`    
    
* `vrsType`: `CopyNumberCount`    

##### GET query string
```requestType=VQSgeneIdRequest&geneId=TP53&copyChange=EFO:0030067&variantMinLength=1000&variantMaxLength=3000000&vrsType=CopyNumberCount```

##### POST query component 
```{
    "copyChange": "EFO:0030067",
    "geneId": "TP53",
    "requestType": "VQSgeneIdRequest",
    "variantMaxLength": 3000000,
    "variantMinLength": 1000,
    "vrsType": "CopyNumberCount"
}```
