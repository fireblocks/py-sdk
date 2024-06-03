# CreateValidationKeyResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_key** | [**ValidationKeyDto**](ValidationKeyDto.md) | Created validation key | 
**admins** | **List[str]** | Admins who have to approve the validation key addition | 
**approval_threshold** | **float** | Minimal number of approvers required. 0 for all | 
**request_id** | **float** | Approval request id. Can be cancelled | 

## Example

```python
from fireblocks.models.create_validation_key_response_dto import CreateValidationKeyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateValidationKeyResponseDto from a JSON string
create_validation_key_response_dto_instance = CreateValidationKeyResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateValidationKeyResponseDto.to_json())

# convert the object into a dict
create_validation_key_response_dto_dict = create_validation_key_response_dto_instance.to_dict()
# create an instance of CreateValidationKeyResponseDto from a dict
create_validation_key_response_dto_from_dict = CreateValidationKeyResponseDto.from_dict(create_validation_key_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


