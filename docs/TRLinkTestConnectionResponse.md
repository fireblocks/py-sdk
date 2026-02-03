# TRLinkTestConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the connection test was successful | 
**message** | **str** | Additional message about the connection test (present when success is false) | [optional] 
**timestamp** | **datetime** | Timestamp when the test was performed (ISO 8601 format) | 
**partner_ident** | **str** | Partner identification code | [optional] 
**partner_name** | **str** | Partner display name | [optional] 

## Example

```python
from fireblocks.models.tr_link_test_connection_response import TRLinkTestConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkTestConnectionResponse from a JSON string
tr_link_test_connection_response_instance = TRLinkTestConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkTestConnectionResponse.to_json())

# convert the object into a dict
tr_link_test_connection_response_dict = tr_link_test_connection_response_instance.to_dict()
# create an instance of TRLinkTestConnectionResponse from a dict
tr_link_test_connection_response_from_dict = TRLinkTestConnectionResponse.from_dict(tr_link_test_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


