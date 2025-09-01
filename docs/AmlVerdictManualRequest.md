# AmlVerdictManualRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verdict** | **str** | The AML verdict to set for the transaction | 
**tx_id** | **str** | The transaction ID to set the verdict for | 

## Example

```python
from fireblocks.models.aml_verdict_manual_request import AmlVerdictManualRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AmlVerdictManualRequest from a JSON string
aml_verdict_manual_request_instance = AmlVerdictManualRequest.from_json(json)
# print the JSON string representation of the object
print(AmlVerdictManualRequest.to_json())

# convert the object into a dict
aml_verdict_manual_request_dict = aml_verdict_manual_request_instance.to_dict()
# create an instance of AmlVerdictManualRequest from a dict
aml_verdict_manual_request_from_dict = AmlVerdictManualRequest.from_dict(aml_verdict_manual_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


