# ContractMethodPattern


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method_calls** | **List[str]** |  | 
**operator** | **str** | Operator for method calls | 
**payload_suffix** | **str** | Payload suffix for method calls | [optional] 

## Example

```python
from fireblocks.models.contract_method_pattern import ContractMethodPattern

# TODO update the JSON string below
json = "{}"
# create an instance of ContractMethodPattern from a JSON string
contract_method_pattern_instance = ContractMethodPattern.from_json(json)
# print the JSON string representation of the object
print(ContractMethodPattern.to_json())

# convert the object into a dict
contract_method_pattern_dict = contract_method_pattern_instance.to_dict()
# create an instance of ContractMethodPattern from a dict
contract_method_pattern_from_dict = ContractMethodPattern.from_dict(contract_method_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


