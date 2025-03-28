# GetDeployableAddressRequestDto

Request body for calculating deterministic address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_descriptor** | **str** | The base asset identifier of the blockchain (legacyId) to calculate deterministic address | 
**template_id** | **str** | The template identifier | 
**init_params** | [**List[ParameterWithValue]**](ParameterWithValue.md) | The deploy function parameters and values of the contract template | 
**salt** | **str** | The salt to calculate the deterministic address. Must be a number between 0 and 2^256 -1, for it to fit in the bytes32 parameter | 

## Example

```python
from fireblocks.models.get_deployable_address_request_dto import GetDeployableAddressRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeployableAddressRequestDto from a JSON string
get_deployable_address_request_dto_instance = GetDeployableAddressRequestDto.from_json(json)
# print the JSON string representation of the object
print(GetDeployableAddressRequestDto.to_json())

# convert the object into a dict
get_deployable_address_request_dto_dict = get_deployable_address_request_dto_instance.to_dict()
# create an instance of GetDeployableAddressRequestDto from a dict
get_deployable_address_request_dto_from_dict = GetDeployableAddressRequestDto.from_dict(get_deployable_address_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


