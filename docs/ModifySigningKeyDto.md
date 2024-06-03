# ModifySigningKeyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **float** |  | 

## Example

```python
from fireblocks.models.modify_signing_key_dto import ModifySigningKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySigningKeyDto from a JSON string
modify_signing_key_dto_instance = ModifySigningKeyDto.from_json(json)
# print the JSON string representation of the object
print(ModifySigningKeyDto.to_json())

# convert the object into a dict
modify_signing_key_dto_dict = modify_signing_key_dto_instance.to_dict()
# create an instance of ModifySigningKeyDto from a dict
modify_signing_key_dto_from_dict = ModifySigningKeyDto.from_dict(modify_signing_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


