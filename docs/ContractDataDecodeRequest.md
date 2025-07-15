# ContractDataDecodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ContractDataDecodeRequestData**](ContractDataDecodeRequestData.md) |  | 
**data_type** | [**ContractDataDecodeDataType**](ContractDataDecodeDataType.md) |  | 
**abi** | [**List[AbiFunction]**](AbiFunction.md) | The abi of the function/error/log to decode. | [optional] 

## Example

```python
from fireblocks.models.contract_data_decode_request import ContractDataDecodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDataDecodeRequest from a JSON string
contract_data_decode_request_instance = ContractDataDecodeRequest.from_json(json)
# print the JSON string representation of the object
print(ContractDataDecodeRequest.to_json())

# convert the object into a dict
contract_data_decode_request_dict = contract_data_decode_request_instance.to_dict()
# create an instance of ContractDataDecodeRequest from a dict
contract_data_decode_request_from_dict = ContractDataDecodeRequest.from_dict(contract_data_decode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


