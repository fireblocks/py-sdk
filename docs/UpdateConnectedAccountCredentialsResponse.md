# UpdateConnectedAccountCredentialsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[AddedConnectedAccountItem]**](AddedConnectedAccountItem.md) | The account whose credentials are pending update (status WAITING_FOR_APPROVAL). Old credentials stay live until the change is approved. | 

## Example

```python
from fireblocks.models.update_connected_account_credentials_response import UpdateConnectedAccountCredentialsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConnectedAccountCredentialsResponse from a JSON string
update_connected_account_credentials_response_instance = UpdateConnectedAccountCredentialsResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateConnectedAccountCredentialsResponse.to_json())

# convert the object into a dict
update_connected_account_credentials_response_dict = update_connected_account_credentials_response_instance.to_dict()
# create an instance of UpdateConnectedAccountCredentialsResponse from a dict
update_connected_account_credentials_response_from_dict = UpdateConnectedAccountCredentialsResponse.from_dict(update_connected_account_credentials_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


