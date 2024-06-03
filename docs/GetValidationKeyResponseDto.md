# GetValidationKeyResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ValidationKeyDto]**](ValidationKeyDto.md) | Response object for getting external validation keys. | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks.models.get_validation_key_response_dto import GetValidationKeyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetValidationKeyResponseDto from a JSON string
get_validation_key_response_dto_instance = GetValidationKeyResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetValidationKeyResponseDto.to_json())

# convert the object into a dict
get_validation_key_response_dto_dict = get_validation_key_response_dto_instance.to_dict()
# create an instance of GetValidationKeyResponseDto from a dict
get_validation_key_response_dto_from_dict = GetValidationKeyResponseDto.from_dict(get_validation_key_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


