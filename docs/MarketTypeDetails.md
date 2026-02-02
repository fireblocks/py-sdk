# MarketTypeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**MarketTypeEnum**](MarketTypeEnum.md) |  | 

## Example

```python
from fireblocks.models.market_type_details import MarketTypeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MarketTypeDetails from a JSON string
market_type_details_instance = MarketTypeDetails.from_json(json)
# print the JSON string representation of the object
print(MarketTypeDetails.to_json())

# convert the object into a dict
market_type_details_dict = market_type_details_instance.to_dict()
# create an instance of MarketTypeDetails from a dict
market_type_details_from_dict = MarketTypeDetails.from_dict(market_type_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


