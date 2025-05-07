# DeployableAddressResponse

Response DTO containing a deployable address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The deployable address | 

## Example

```python
from fireblocks.models.deployable_address_response import DeployableAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeployableAddressResponse from a JSON string
deployable_address_response_instance = DeployableAddressResponse.from_json(json)
# print the JSON string representation of the object
print(DeployableAddressResponse.to_json())

# convert the object into a dict
deployable_address_response_dict = deployable_address_response_instance.to_dict()
# create an instance of DeployableAddressResponse from a dict
deployable_address_response_from_dict = DeployableAddressResponse.from_dict(deployable_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


