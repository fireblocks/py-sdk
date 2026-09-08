# CantonCallAllowListRemove


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Which call to make. Selects the shape of &#x60;payload&#x60;. | 
**payload** | [**AllowListPayload**](AllowListPayload.md) |  | 

## Example

```python
from fireblocks.models.canton_call_allow_list_remove import CantonCallAllowListRemove

# TODO update the JSON string below
json = "{}"
# create an instance of CantonCallAllowListRemove from a JSON string
canton_call_allow_list_remove_instance = CantonCallAllowListRemove.from_json(json)
# print the JSON string representation of the object
print(CantonCallAllowListRemove.to_json())

# convert the object into a dict
canton_call_allow_list_remove_dict = canton_call_allow_list_remove_instance.to_dict()
# create an instance of CantonCallAllowListRemove from a dict
canton_call_allow_list_remove_from_dict = CantonCallAllowListRemove.from_dict(canton_call_allow_list_remove_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


