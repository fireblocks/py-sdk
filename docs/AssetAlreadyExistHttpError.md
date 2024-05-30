# AssetAlreadyExistHttpError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | HTTP status code | [optional] 
**message** | **str** | Error message | [optional] 
**error** | **str** | Short description of the HTTP error | [optional] 

## Example

```python
from fireblocks.models.asset_already_exist_http_error import AssetAlreadyExistHttpError

# TODO update the JSON string below
json = "{}"
# create an instance of AssetAlreadyExistHttpError from a JSON string
asset_already_exist_http_error_instance = AssetAlreadyExistHttpError.from_json(json)
# print the JSON string representation of the object
print(AssetAlreadyExistHttpError.to_json())

# convert the object into a dict
asset_already_exist_http_error_dict = asset_already_exist_http_error_instance.to_dict()
# create an instance of AssetAlreadyExistHttpError from a dict
asset_already_exist_http_error_from_dict = AssetAlreadyExistHttpError.from_dict(asset_already_exist_http_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


