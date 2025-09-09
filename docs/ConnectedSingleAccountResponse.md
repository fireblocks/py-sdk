# ConnectedSingleAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the connected account. | 
**name** | **str** | Human-readable name of the connected account. | 
**provider_id** | **str** | The ID of the venue the account belongs to. | 
**status** | [**ConnectedAccountApprovalStatus**](ConnectedAccountApprovalStatus.md) |  | 
**total_balance** | [**ConnectedAccountTotalBalance**](ConnectedAccountTotalBalance.md) |  | 
**manifest** | [**ConnectedAccountManifest**](ConnectedAccountManifest.md) |  | 
**parent_id** | **str** | The ID of the parent main account, if this is a sub account. | [optional] 
**sub_accounts_ids** | **List[str]** | IDs of sub-accounts associated with this connected account. | [optional] 

## Example

```python
from fireblocks.models.connected_single_account_response import ConnectedSingleAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedSingleAccountResponse from a JSON string
connected_single_account_response_instance = ConnectedSingleAccountResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectedSingleAccountResponse.to_json())

# convert the object into a dict
connected_single_account_response_dict = connected_single_account_response_instance.to_dict()
# create an instance of ConnectedSingleAccountResponse from a dict
connected_single_account_response_from_dict = ConnectedSingleAccountResponse.from_dict(connected_single_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


