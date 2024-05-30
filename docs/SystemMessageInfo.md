# SystemMessageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**message** | **str** | A response from Fireblocks that communicates a message about the health of the process being performed. If this object is returned with data, you should expect potential delays or incomplete transaction statuses. | [optional] 

## Example

```python
from fireblocks.models.system_message_info import SystemMessageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SystemMessageInfo from a JSON string
system_message_info_instance = SystemMessageInfo.from_json(json)
# print the JSON string representation of the object
print(SystemMessageInfo.to_json())

# convert the object into a dict
system_message_info_dict = system_message_info_instance.to_dict()
# create an instance of SystemMessageInfo from a dict
system_message_info_from_dict = SystemMessageInfo.from_dict(system_message_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


