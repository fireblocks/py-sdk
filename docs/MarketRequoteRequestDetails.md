# MarketRequoteRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates that the order should be re-quoted if the original quote is expired. This will lead to a market order. | 

## Example

```python
from fireblocks.models.market_requote_request_details import MarketRequoteRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MarketRequoteRequestDetails from a JSON string
market_requote_request_details_instance = MarketRequoteRequestDetails.from_json(json)
# print the JSON string representation of the object
print(MarketRequoteRequestDetails.to_json())

# convert the object into a dict
market_requote_request_details_dict = market_requote_request_details_instance.to_dict()
# create an instance of MarketRequoteRequestDetails from a dict
market_requote_request_details_from_dict = MarketRequoteRequestDetails.from_dict(market_requote_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


