# ContractDataDecodeError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Bad request error message | 
**code** | **float** | Error code | 

## Example

```python
from fireblocks.models.contract_data_decode_error import ContractDataDecodeError

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDataDecodeError from a JSON string
contract_data_decode_error_instance = ContractDataDecodeError.from_json(json)
# print the JSON string representation of the object
print(ContractDataDecodeError.to_json())

# convert the object into a dict
contract_data_decode_error_dict = contract_data_decode_error_instance.to_dict()
# create an instance of ContractDataDecodeError from a dict
contract_data_decode_error_from_dict = ContractDataDecodeError.from_dict(contract_data_decode_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


