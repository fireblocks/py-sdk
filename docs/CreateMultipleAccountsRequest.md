# CreateMultipleAccountsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count | [optional] 
**asset_ids** | **List[str]** | Array of asset IDs | [optional] 

## Example

```python
from fireblocks.models.create_multiple_accounts_request import CreateMultipleAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMultipleAccountsRequest from a JSON string
create_multiple_accounts_request_instance = CreateMultipleAccountsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMultipleAccountsRequest.to_json())

# convert the object into a dict
create_multiple_accounts_request_dict = create_multiple_accounts_request_instance.to_dict()
# create an instance of CreateMultipleAccountsRequest from a dict
create_multiple_accounts_request_from_dict = CreateMultipleAccountsRequest.from_dict(create_multiple_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


