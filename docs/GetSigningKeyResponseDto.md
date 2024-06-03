# GetSigningKeyResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SigningKeyDto]**](SigningKeyDto.md) | Response object for getting external signing keys. | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks.models.get_signing_key_response_dto import GetSigningKeyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetSigningKeyResponseDto from a JSON string
get_signing_key_response_dto_instance = GetSigningKeyResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetSigningKeyResponseDto.to_json())

# convert the object into a dict
get_signing_key_response_dto_dict = get_signing_key_response_dto_instance.to_dict()
# create an instance of GetSigningKeyResponseDto from a dict
get_signing_key_response_dto_from_dict = GetSigningKeyResponseDto.from_dict(get_signing_key_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


