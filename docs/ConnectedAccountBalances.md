# ConnectedAccountBalances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | Asset identifier (e.g., BTC, ETH, USDC). | 
**available_amount** | **str** | Amount available for use. | 
**total_amount** | **str** | Total amount including locked/held balances. | 
**locked_amount** | **str** | Amount currently locked/held. | [optional] 
**credit_amount** | **str** | Credit line amount, if applicable (0 when not used). | [optional] 
**balance_type** | **str** | Wallet type/category (e.g., SPOT, MARGIN, FUNDING). | 
**balance_name** | **str** | Display name for the balance type (at the provider) | [optional] 

## Example

```python
from fireblocks.models.connected_account_balances import ConnectedAccountBalances

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountBalances from a JSON string
connected_account_balances_instance = ConnectedAccountBalances.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountBalances.to_json())

# convert the object into a dict
connected_account_balances_dict = connected_account_balances_instance.to_dict()
# create an instance of ConnectedAccountBalances from a dict
connected_account_balances_from_dict = ConnectedAccountBalances.from_dict(connected_account_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


