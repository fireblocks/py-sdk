# ConnectedAccount


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

## Example

```python
from fireblocks.models.connected_account import ConnectedAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccount from a JSON string
connected_account_instance = ConnectedAccount.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccount.to_json())

# convert the object into a dict
connected_account_dict = connected_account_instance.to_dict()
# create an instance of ConnectedAccount from a dict
connected_account_from_dict = ConnectedAccount.from_dict(connected_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


