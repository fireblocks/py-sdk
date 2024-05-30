# ContractDoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str** | A description of the contract | [optional] 
**events** | **str** | A description of the contract&#x60;s events | [optional] 
**kind** | **str** | Is it devdoc or userdoc | 
**methods** | [**Dict[str, FunctionDoc]**](FunctionDoc.md) | The description of the contract functions | 
**version** | **str** | The version of the contract | 

## Example

```python
from fireblocks_client.models.contract_doc import ContractDoc

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDoc from a JSON string
contract_doc_instance = ContractDoc.from_json(json)
# print the JSON string representation of the object
print(ContractDoc.to_json())

# convert the object into a dict
contract_doc_dict = contract_doc_instance.to_dict()
# create an instance of ContractDoc from a dict
contract_doc_from_dict = ContractDoc.from_dict(contract_doc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


