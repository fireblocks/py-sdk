# QuoteFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_execution_fee** | **str** | The gas fee in the asset unit. | 
**network_fee_asset_id** | **str** | The network fee in Fireblocks asset representation | 
**provider_fee** | **str** | The provider fee in the asset unit. | 
**provider_fee_asset_id** | **str** | The provider fee in Fireblocks asset representation | 
**provider_fee_rate** | **float** | Percentages of the provider fee out of the gross amount | 
**network_approve_fee** | **str** | The gas fee in the asset unit. | [optional] 

## Example

```python
from fireblocks.models.quote_fee import QuoteFee

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteFee from a JSON string
quote_fee_instance = QuoteFee.from_json(json)
# print the JSON string representation of the object
print(QuoteFee.to_json())

# convert the object into a dict
quote_fee_dict = quote_fee_instance.to_dict()
# create an instance of QuoteFee from a dict
quote_fee_from_dict = QuoteFee.from_dict(quote_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


