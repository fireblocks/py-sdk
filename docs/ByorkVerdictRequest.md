# ByorkVerdictRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** | Transaction ID to set the verdict for | 
**verdict** | [**ByorkSetVerdictEnum**](ByorkSetVerdictEnum.md) |  | 

## Example

```python
from fireblocks.models.byork_verdict_request import ByorkVerdictRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ByorkVerdictRequest from a JSON string
byork_verdict_request_instance = ByorkVerdictRequest.from_json(json)
# print the JSON string representation of the object
print(ByorkVerdictRequest.to_json())

# convert the object into a dict
byork_verdict_request_dict = byork_verdict_request_instance.to_dict()
# create an instance of ByorkVerdictRequest from a dict
byork_verdict_request_from_dict = ByorkVerdictRequest.from_dict(byork_verdict_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


