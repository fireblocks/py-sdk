# RenameConnectedAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | The new name for the connected account | 

## Example

```python
from fireblocks.models.rename_connected_account_request import RenameConnectedAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RenameConnectedAccountRequest from a JSON string
rename_connected_account_request_instance = RenameConnectedAccountRequest.from_json(json)
# print the JSON string representation of the object
print(RenameConnectedAccountRequest.to_json())

# convert the object into a dict
rename_connected_account_request_dict = rename_connected_account_request_instance.to_dict()
# create an instance of RenameConnectedAccountRequest from a dict
rename_connected_account_request_from_dict = RenameConnectedAccountRequest.from_dict(rename_connected_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


