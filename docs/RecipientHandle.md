# RecipientHandle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** | The value of the recipient handle | 

## Example

```python
from fireblocks.models.recipient_handle import RecipientHandle

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientHandle from a JSON string
recipient_handle_instance = RecipientHandle.from_json(json)
# print the JSON string representation of the object
print(RecipientHandle.to_json())

# convert the object into a dict
recipient_handle_dict = recipient_handle_instance.to_dict()
# create an instance of RecipientHandle from a dict
recipient_handle_from_dict = RecipientHandle.from_dict(recipient_handle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


