# AddConnectedAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[AddedConnectedAccountItem]**](AddedConnectedAccountItem.md) | Created accounts — main account first, sub-accounts after (NLV2 hierarchy). | 

## Example

```python
from fireblocks.models.add_connected_account_response import AddConnectedAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddConnectedAccountResponse from a JSON string
add_connected_account_response_instance = AddConnectedAccountResponse.from_json(json)
# print the JSON string representation of the object
print(AddConnectedAccountResponse.to_json())

# convert the object into a dict
add_connected_account_response_dict = add_connected_account_response_instance.to_dict()
# create an instance of AddConnectedAccountResponse from a dict
add_connected_account_response_from_dict = AddConnectedAccountResponse.from_dict(add_connected_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


