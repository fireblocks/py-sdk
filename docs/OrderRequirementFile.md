# OrderRequirementFile

A file the provider requires as part of the order requirement response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_key** | **str** | Stable identifier for this required file. Used to correlate uploads on submission. | 
**description** | **str** | Human-readable description of what the file should contain. | 
**allowed_file_types** | [**List[OrderRequirementAllowedFileType]**](OrderRequirementAllowedFileType.md) | File formats the provider accepts for this entry. | 

## Example

```python
from fireblocks.models.order_requirement_file import OrderRequirementFile

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRequirementFile from a JSON string
order_requirement_file_instance = OrderRequirementFile.from_json(json)
# print the JSON string representation of the object
print(OrderRequirementFile.to_json())

# convert the object into a dict
order_requirement_file_dict = order_requirement_file_instance.to_dict()
# create an instance of OrderRequirementFile from a dict
order_requirement_file_from_dict = OrderRequirementFile.from_dict(order_requirement_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


