# AllowListPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The vault account whose Canton wallet acts here. | 
**asset** | **str** | Chain asset — &#x60;CANTON&#x60; or &#x60;CANTON_TEST&#x60;. | 
**wallets** | **List[str]** | Canton party ids to add or remove. | 

## Example

```python
from fireblocks.models.allow_list_payload import AllowListPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AllowListPayload from a JSON string
allow_list_payload_instance = AllowListPayload.from_json(json)
# print the JSON string representation of the object
print(AllowListPayload.to_json())

# convert the object into a dict
allow_list_payload_dict = allow_list_payload_instance.to_dict()
# create an instance of AllowListPayload from a dict
allow_list_payload_from_dict = AllowListPayload.from_dict(allow_list_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


