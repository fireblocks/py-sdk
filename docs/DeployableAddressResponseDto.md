# DeployableAddressResponseDto

Response DTO containing a deployable address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The deployable address | 

## Example

```python
from fireblocks.models.deployable_address_response_dto import DeployableAddressResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeployableAddressResponseDto from a JSON string
deployable_address_response_dto_instance = DeployableAddressResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeployableAddressResponseDto.to_json())

# convert the object into a dict
deployable_address_response_dto_dict = deployable_address_response_dto_instance.to_dict()
# create an instance of DeployableAddressResponseDto from a dict
deployable_address_response_dto_from_dict = DeployableAddressResponseDto.from_dict(deployable_address_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


