# GenieChatMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the message. | 
**session_id** | **str** | The Genie session this message belongs to. | 
**role** | **str** | Who produced the message — &#x60;USER&#x60; for the customer-supplied query, &#x60;ASSISTANT&#x60; for the Genie response. | 
**content** | **str** | The natural-language body of the message. | 
**created_at** | **int** | Message creation timestamp in epoch milliseconds. | [optional] 

## Example

```python
from fireblocks.models.genie_chat_message import GenieChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GenieChatMessage from a JSON string
genie_chat_message_instance = GenieChatMessage.from_json(json)
# print the JSON string representation of the object
print(GenieChatMessage.to_json())

# convert the object into a dict
genie_chat_message_dict = genie_chat_message_instance.to_dict()
# create an instance of GenieChatMessage from a dict
genie_chat_message_from_dict = GenieChatMessage.from_dict(genie_chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


