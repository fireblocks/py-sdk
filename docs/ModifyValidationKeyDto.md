# ModifyValidationKeyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Disable validation key | 

## Example

```python
from fireblocks.models.modify_validation_key_dto import ModifyValidationKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyValidationKeyDto from a JSON string
modify_validation_key_dto_instance = ModifyValidationKeyDto.from_json(json)
# print the JSON string representation of the object
print(ModifyValidationKeyDto.to_json())

# convert the object into a dict
modify_validation_key_dto_dict = modify_validation_key_dto_instance.to_dict()
# create an instance of ModifyValidationKeyDto from a dict
modify_validation_key_dto_from_dict = ModifyValidationKeyDto.from_dict(modify_validation_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


