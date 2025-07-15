# ContractDataDecodedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[ContractDataDecodeResponseParams]**](ContractDataDecodeResponseParams.md) | The decoded parameters of the contract function call. | 
**type** | [**ContractDataDecodeDataType**](ContractDataDecodeDataType.md) |  | 

## Example

```python
from fireblocks.models.contract_data_decoded_response import ContractDataDecodedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDataDecodedResponse from a JSON string
contract_data_decoded_response_instance = ContractDataDecodedResponse.from_json(json)
# print the JSON string representation of the object
print(ContractDataDecodedResponse.to_json())

# convert the object into a dict
contract_data_decoded_response_dict = contract_data_decoded_response_instance.to_dict()
# create an instance of ContractDataDecodedResponse from a dict
contract_data_decoded_response_from_dict = ContractDataDecodedResponse.from_dict(contract_data_decoded_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


