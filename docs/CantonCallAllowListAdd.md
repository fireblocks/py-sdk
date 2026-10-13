# CantonCallAllowListAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Which call to make. Selects the shape of &#x60;payload&#x60;. | 
**vault_account_id** | **str** | The vault account whose Canton wallet makes this call. | 
**blockchain_id** | **str** | The blockchain the vault account&#39;s Canton party is connected to — &#x60;CANTON&#x60; or &#x60;CANTON_TEST&#x60;. | 
**payload** | [**AllowListPayload**](AllowListPayload.md) |  | 

## Example

```python
from fireblocks.models.canton_call_allow_list_add import CantonCallAllowListAdd

# TODO update the JSON string below
json = "{}"
# create an instance of CantonCallAllowListAdd from a JSON string
canton_call_allow_list_add_instance = CantonCallAllowListAdd.from_json(json)
# print the JSON string representation of the object
print(CantonCallAllowListAdd.to_json())

# convert the object into a dict
canton_call_allow_list_add_dict = canton_call_allow_list_add_instance.to_dict()
# create an instance of CantonCallAllowListAdd from a dict
canton_call_allow_list_add_from_dict = CantonCallAllowListAdd.from_dict(canton_call_allow_list_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


