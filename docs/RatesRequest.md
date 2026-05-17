# RatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**List[ScopeItem]**](ScopeItem.md) | One or more providers/accounts to request rates from. At least one scope item is required. | 
**base_asset_id** | **str** | The source asset identifier. | 
**quote_asset_id** | **str** | The target asset identifier. | 

## Example

```python
from fireblocks.models.rates_request import RatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RatesRequest from a JSON string
rates_request_instance = RatesRequest.from_json(json)
# print the JSON string representation of the object
print(RatesRequest.to_json())

# convert the object into a dict
rates_request_dict = rates_request_instance.to_dict()
# create an instance of RatesRequest from a dict
rates_request_from_dict = RatesRequest.from_dict(rates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


