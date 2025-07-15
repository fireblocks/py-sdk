# ContractDataDecodeRequestData

The data to decode, which can be a string or an object containing the data and its type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | The data to decode, which can be a string or an object containing the data and its type. | 
**topics** | **List[str]** | The topics of the log, which is an array of strings. | 

## Example

```python
from fireblocks.models.contract_data_decode_request_data import ContractDataDecodeRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDataDecodeRequestData from a JSON string
contract_data_decode_request_data_instance = ContractDataDecodeRequestData.from_json(json)
# print the JSON string representation of the object
print(ContractDataDecodeRequestData.to_json())

# convert the object into a dict
contract_data_decode_request_data_dict = contract_data_decode_request_data_instance.to_dict()
# create an instance of ContractDataDecodeRequestData from a dict
contract_data_decode_request_data_from_dict = ContractDataDecodeRequestData.from_dict(contract_data_decode_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


