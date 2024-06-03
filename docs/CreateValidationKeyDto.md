# CreateValidationKeyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key_pem** | **str** | The PEM encoded public key of the validation key being added | 
**days_till_expired** | **float** | The number of days from the date the validation key was added until it expires | 

## Example

```python
from fireblocks.models.create_validation_key_dto import CreateValidationKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateValidationKeyDto from a JSON string
create_validation_key_dto_instance = CreateValidationKeyDto.from_json(json)
# print the JSON string representation of the object
print(CreateValidationKeyDto.to_json())

# convert the object into a dict
create_validation_key_dto_dict = create_validation_key_dto_instance.to_dict()
# create an instance of CreateValidationKeyDto from a dict
create_validation_key_dto_from_dict = CreateValidationKeyDto.from_dict(create_validation_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


