# NonWalletQuoteFee

The estimated fees for the swap operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_execution_fee** | **str** | The gas fee in the asset unit. | 
**network_fee_asset_id** | **str** | The network fee in Fireblocks asset representation | 
**provider_fee** | **str** | The provider fee in the asset unit. | 
**provider_fee_asset_id** | **str** | The provider fee in Fireblocks asset representation | 
**provider_fee_rate** | **float** | Percentages of the provider fee out of the gross amount | 

## Example

```python
from fireblocks.models.non_wallet_quote_fee import NonWalletQuoteFee

# TODO update the JSON string below
json = "{}"
# create an instance of NonWalletQuoteFee from a JSON string
non_wallet_quote_fee_instance = NonWalletQuoteFee.from_json(json)
# print the JSON string representation of the object
print(NonWalletQuoteFee.to_json())

# convert the object into a dict
non_wallet_quote_fee_dict = non_wallet_quote_fee_instance.to_dict()
# create an instance of NonWalletQuoteFee from a dict
non_wallet_quote_fee_from_dict = NonWalletQuoteFee.from_dict(non_wallet_quote_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


