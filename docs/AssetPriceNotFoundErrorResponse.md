# AssetPriceNotFoundErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Not found error message | 
**code** | **str** | Error code | 

## Example

```python
from fireblocks.models.asset_price_not_found_error_response import AssetPriceNotFoundErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPriceNotFoundErrorResponse from a JSON string
asset_price_not_found_error_response_instance = AssetPriceNotFoundErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AssetPriceNotFoundErrorResponse.to_json())

# convert the object into a dict
asset_price_not_found_error_response_dict = asset_price_not_found_error_response_instance.to_dict()
# create an instance of AssetPriceNotFoundErrorResponse from a dict
asset_price_not_found_error_response_from_dict = AssetPriceNotFoundErrorResponse.from_dict(asset_price_not_found_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


