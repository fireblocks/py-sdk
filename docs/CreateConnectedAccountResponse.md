# CreateConnectedAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[CreatedConnectedAccountItem]**](CreatedConnectedAccountItem.md) | Created accounts — main account first, sub-accounts after (NLV2 hierarchy). | 

## Example

```python
from fireblocks.models.create_connected_account_response import CreateConnectedAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectedAccountResponse from a JSON string
create_connected_account_response_instance = CreateConnectedAccountResponse.from_json(json)
# print the JSON string representation of the object
print(CreateConnectedAccountResponse.to_json())

# convert the object into a dict
create_connected_account_response_dict = create_connected_account_response_instance.to_dict()
# create an instance of CreateConnectedAccountResponse from a dict
create_connected_account_response_from_dict = CreateConnectedAccountResponse.from_dict(create_connected_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


