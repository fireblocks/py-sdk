# AssetNotFoundErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Not found error code | 
**code** | **str** | Error code | 

## Example

```python
from fireblocks_client.models.asset_not_found_error_response import AssetNotFoundErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetNotFoundErrorResponse from a JSON string
asset_not_found_error_response_instance = AssetNotFoundErrorResponse.from_json(json)
# print the JSON string representation of the object
print AssetNotFoundErrorResponse.to_json()

# convert the object into a dict
asset_not_found_error_response_dict = asset_not_found_error_response_instance.to_dict()
# create an instance of AssetNotFoundErrorResponse from a dict
asset_not_found_error_response_form_dict = asset_not_found_error_response.from_dict(asset_not_found_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


