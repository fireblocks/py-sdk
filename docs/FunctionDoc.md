# FunctionDoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str** | A description of the function | [optional] 
**params** | **Dict[str, str]** | A description of the function parameters | [optional] 
**returns** | **Dict[str, str]** | A description of the function return values. only for read functions | [optional] 

## Example

```python
from fireblocks.models.function_doc import FunctionDoc

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionDoc from a JSON string
function_doc_instance = FunctionDoc.from_json(json)
# print the JSON string representation of the object
print(FunctionDoc.to_json())

# convert the object into a dict
function_doc_dict = function_doc_instance.to_dict()
# create an instance of FunctionDoc from a dict
function_doc_from_dict = FunctionDoc.from_dict(function_doc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


