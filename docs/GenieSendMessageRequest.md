# GenieSendMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The natural-language question or instruction to send to Genie. | 

## Example

```python
from fireblocks.models.genie_send_message_request import GenieSendMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenieSendMessageRequest from a JSON string
genie_send_message_request_instance = GenieSendMessageRequest.from_json(json)
# print the JSON string representation of the object
print(GenieSendMessageRequest.to_json())

# convert the object into a dict
genie_send_message_request_dict = genie_send_message_request_instance.to_dict()
# create an instance of GenieSendMessageRequest from a dict
genie_send_message_request_from_dict = GenieSendMessageRequest.from_dict(genie_send_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


