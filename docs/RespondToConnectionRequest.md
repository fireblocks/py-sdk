# RespondToConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approve** | **bool** | Approval of the initiated Web3 connection. | 

## Example

```python
from fireblocks_client.models.respond_to_connection_request import RespondToConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RespondToConnectionRequest from a JSON string
respond_to_connection_request_instance = RespondToConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(RespondToConnectionRequest.to_json())

# convert the object into a dict
respond_to_connection_request_dict = respond_to_connection_request_instance.to_dict()
# create an instance of RespondToConnectionRequest from a dict
respond_to_connection_request_from_dict = RespondToConnectionRequest.from_dict(respond_to_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


