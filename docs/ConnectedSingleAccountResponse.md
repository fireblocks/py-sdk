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
**api_key** | **str** | The API key identifier used to connect this account. | [optional] 
**provider_account_name** | **str** | The account name provided by the provider. | [optional] 
**account_type** | [**ConnectedAccountType**](ConnectedAccountType.md) |  | 
**sub_accounts_ids** | **List[str]** | IDs of sub-accounts associated with this connected account. | [optional] 
**total_credit** | [**ConnectedAccountCredit**](ConnectedAccountCredit.md) | Total credit line available on the account. Returned only by the single-account endpoint (Get connected account); the list endpoint does not retrieve balances and never populates it. Omitted when total credit data is unavailable or balance retrieval is skipped. Absence does not imply zero credit. | [optional] 
**available_credit** | [**ConnectedAccountCredit**](ConnectedAccountCredit.md) | Remaining unused credit available on the account. Returned only by the single-account endpoint (Get connected account); the list endpoint does not retrieve balances and never populates it. Omitted when available credit data is unavailable or balance retrieval is skipped. Absence does not imply zero credit. | [optional] 

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


