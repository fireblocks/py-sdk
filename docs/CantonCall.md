# CantonCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Which call to make. Selects the shape of &#x60;payload&#x60;. | 
**payload** | [**TransferWithdrawPayload**](TransferWithdrawPayload.md) |  | 

## Example

```python
from fireblocks.models.canton_call import CantonCall

# TODO update the JSON string below
json = "{}"
# create an instance of CantonCall from a JSON string
canton_call_instance = CantonCall.from_json(json)
# print the JSON string representation of the object
print(CantonCall.to_json())

# convert the object into a dict
canton_call_dict = canton_call_instance.to_dict()
# create an instance of CantonCall from a dict
canton_call_from_dict = CantonCall.from_dict(canton_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


