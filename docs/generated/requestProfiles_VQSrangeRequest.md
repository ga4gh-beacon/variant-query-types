# Request Profile: `VQSrangeRequest`

Beacon Range Queries are supposed to return matches of any variant with at least partial overlap of the sequence range specified by `referenceAccession`, `start` and `end` parameters. Additional qualifiers such as `copyChange` or length of the affected sequence can be used to further restrict the returned results. For this request type usually `start` and `end` with a single position are used, _i.e._ a subset of the `start` and `end` specifications. However, 
##### TODO
* Evaluate to split into more basic `RangeRequest` and specialized
  requests requiring an effect component
* Review current VRS v2 and upcoming versions for optoions to express
  types of variants beyond the `copyChange` parameter