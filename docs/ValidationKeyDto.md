# ValidationKeyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | External validation key id set by Fireblocks. | 
**public_key_pem** | **str** | PEM encoded public key used for the validation. | 
**days_till_expired** | **float** |  | 
**enabled** | **bool** | True if the validation key is enabled. | 
**created_at** | **float** | Creation date (timestamp) in milliseconds. | 

## Example

```python
from fireblocks.models.validation_key_dto import ValidationKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationKeyDto from a JSON string
validation_key_dto_instance = ValidationKeyDto.from_json(json)
# print the JSON string representation of the object
print(ValidationKeyDto.to_json())

# convert the object into a dict
validation_key_dto_dict = validation_key_dto_instance.to_dict()
# create an instance of ValidationKeyDto from a dict
validation_key_dto_from_dict = ValidationKeyDto.from_dict(validation_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


