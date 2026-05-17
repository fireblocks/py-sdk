# GenieCreateSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the newly created Genie session. Use this when sending messages in the conversation. | 
**created_at** | **int** | Session creation timestamp in epoch milliseconds. | [optional] 
**title** | **str** | Session title. May be empty until the first message has been processed. | [optional] 

## Example

```python
from fireblocks.models.genie_create_session_response import GenieCreateSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenieCreateSessionResponse from a JSON string
genie_create_session_response_instance = GenieCreateSessionResponse.from_json(json)
# print the JSON string representation of the object
print(GenieCreateSessionResponse.to_json())

# convert the object into a dict
genie_create_session_response_dict = genie_create_session_response_instance.to_dict()
# create an instance of GenieCreateSessionResponse from a dict
genie_create_session_response_from_dict = GenieCreateSessionResponse.from_dict(genie_create_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


