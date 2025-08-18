# AdapterProcessingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_token_link_id** | **str** | The input token link ID | 
**adapter_link_id** | **str** | The adapter link ID | 

## Example

```python
from fireblocks.models.adapter_processing_result import AdapterProcessingResult

# TODO update the JSON string below
json = "{}"
# create an instance of AdapterProcessingResult from a JSON string
adapter_processing_result_instance = AdapterProcessingResult.from_json(json)
# print the JSON string representation of the object
print(AdapterProcessingResult.to_json())

# convert the object into a dict
adapter_processing_result_dict = adapter_processing_result_instance.to_dict()
# create an instance of AdapterProcessingResult from a dict
adapter_processing_result_from_dict = AdapterProcessingResult.from_dict(adapter_processing_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


