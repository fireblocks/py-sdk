# ConnectedAccountRateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account that generated the quote. | 
**base_asset_id** | **str** | The source asset identifier | 
**quote_asset_id** | **str** | The target asset identifier | 
**rate** | **str** | The exchange rate value | 

## Example

```python
from fireblocks.models.connected_account_rate_response import ConnectedAccountRateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountRateResponse from a JSON string
connected_account_rate_response_instance = ConnectedAccountRateResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountRateResponse.to_json())

# convert the object into a dict
connected_account_rate_response_dict = connected_account_rate_response_instance.to_dict()
# create an instance of ConnectedAccountRateResponse from a dict
connected_account_rate_response_from_dict = ConnectedAccountRateResponse.from_dict(connected_account_rate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


