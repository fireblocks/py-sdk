# AssetPriceForbiddenErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Forbidden error message | 
**code** | **float** | Error code | 

## Example

```python
from fireblocks.models.asset_price_forbidden_error_response import AssetPriceForbiddenErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPriceForbiddenErrorResponse from a JSON string
asset_price_forbidden_error_response_instance = AssetPriceForbiddenErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AssetPriceForbiddenErrorResponse.to_json())

# convert the object into a dict
asset_price_forbidden_error_response_dict = asset_price_forbidden_error_response_instance.to_dict()
# create an instance of AssetPriceForbiddenErrorResponse from a dict
asset_price_forbidden_error_response_from_dict = AssetPriceForbiddenErrorResponse.from_dict(asset_price_forbidden_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


