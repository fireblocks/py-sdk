# GetDeployableAddressRequest

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
from fireblocks.models.get_deployable_address_request import GetDeployableAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeployableAddressRequest from a JSON string
get_deployable_address_request_instance = GetDeployableAddressRequest.from_json(json)
# print the JSON string representation of the object
print(GetDeployableAddressRequest.to_json())

# convert the object into a dict
get_deployable_address_request_dict = get_deployable_address_request_instance.to_dict()
# create an instance of GetDeployableAddressRequest from a dict
get_deployable_address_request_from_dict = GetDeployableAddressRequest.from_dict(get_deployable_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


