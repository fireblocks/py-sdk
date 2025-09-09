# ConnectedAccountTotalBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The denominated currency value of the account. | 
**denominated_asset_id** | **str** | The asset ID of the total balance. | 
**has_full_asset_coverage** | **bool** | Indicates whether the total amount represents the complete balance of all assets in the account. When true, all asset balances have been successfully converted to the denominated currency. When false, some assets could not be included in the total due to missing exchange rates or non-convertible assets. | [default to False]

## Example

```python
from fireblocks.models.connected_account_total_balance import ConnectedAccountTotalBalance

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountTotalBalance from a JSON string
connected_account_total_balance_instance = ConnectedAccountTotalBalance.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountTotalBalance.to_json())

# convert the object into a dict
connected_account_total_balance_dict = connected_account_total_balance_instance.to_dict()
# create an instance of ConnectedAccountTotalBalance from a dict
connected_account_total_balance_from_dict = ConnectedAccountTotalBalance.from_dict(connected_account_total_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


