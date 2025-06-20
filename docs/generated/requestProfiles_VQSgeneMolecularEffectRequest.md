# Request Profile: `VQSgeneMolecularEffectRequest`

A request for the variation consequence, e.g. for the _molecular_ changes
caused by the variant.

##### TODO

* Define a clear structure for how request types are constructed with a
  primacy of *where* the variant is located or *what* happens. 

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
