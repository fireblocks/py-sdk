# ContractDataLogDataParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | The data to decode, which can be a string or an object containing the data and its type. | 
**topics** | **List[str]** | The topics of the log, which is an array of strings. | 

## Example

```python
from fireblocks.models.contract_data_log_data_param import ContractDataLogDataParam

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDataLogDataParam from a JSON string
contract_data_log_data_param_instance = ContractDataLogDataParam.from_json(json)
# print the JSON string representation of the object
print(ContractDataLogDataParam.to_json())

# convert the object into a dict
contract_data_log_data_param_dict = contract_data_log_data_param_instance.to_dict()
# create an instance of ContractDataLogDataParam from a dict
contract_data_log_data_param_from_dict = ContractDataLogDataParam.from_dict(contract_data_log_data_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


