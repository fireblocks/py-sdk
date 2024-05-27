# AssetDoesNotExistHttpError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | HTTP status code | [optional] 
**message** | **str** | Error message | [optional] 
**error** | **str** | Short description of the HTTP error | [optional] 

## Example

```python
from fireblocks_client.models.asset_does_not_exist_http_error import AssetDoesNotExistHttpError

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDoesNotExistHttpError from a JSON string
asset_does_not_exist_http_error_instance = AssetDoesNotExistHttpError.from_json(json)
# print the JSON string representation of the object
print AssetDoesNotExistHttpError.to_json()

# convert the object into a dict
asset_does_not_exist_http_error_dict = asset_does_not_exist_http_error_instance.to_dict()
# create an instance of AssetDoesNotExistHttpError from a dict
asset_does_not_exist_http_error_form_dict = asset_does_not_exist_http_error.from_dict(asset_does_not_exist_http_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


