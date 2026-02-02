# ContractAddressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_address** | **str** | The contract&#39;s onchain address | 

## Example

```python
from fireblocks.models.contract_address_response import ContractAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAddressResponse from a JSON string
contract_address_response_instance = ContractAddressResponse.from_json(json)
# print the JSON string representation of the object
print(ContractAddressResponse.to_json())

# convert the object into a dict
contract_address_response_dict = contract_address_response_instance.to_dict()
# create an instance of ContractAddressResponse from a dict
contract_address_response_from_dict = ContractAddressResponse.from_dict(contract_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


