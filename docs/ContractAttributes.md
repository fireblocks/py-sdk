# ContractAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_cases** | **List[str]** |  | 
**standards** | **List[str]** |  | 
**auditor** | [**AuditorData**](AuditorData.md) |  | 

## Example

```python
from fireblocks.models.contract_attributes import ContractAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAttributes from a JSON string
contract_attributes_instance = ContractAttributes.from_json(json)
# print the JSON string representation of the object
print(ContractAttributes.to_json())

# convert the object into a dict
contract_attributes_dict = contract_attributes_instance.to_dict()
# create an instance of ContractAttributes from a dict
contract_attributes_from_dict = ContractAttributes.from_dict(contract_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


