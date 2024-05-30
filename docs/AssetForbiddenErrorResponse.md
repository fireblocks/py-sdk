# AssetForbiddenErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Forbidden error code | 
**code** | **str** | Error code | 

## Example

```python
from fireblocks.models.asset_forbidden_error_response import AssetForbiddenErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetForbiddenErrorResponse from a JSON string
asset_forbidden_error_response_instance = AssetForbiddenErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AssetForbiddenErrorResponse.to_json())

# convert the object into a dict
asset_forbidden_error_response_dict = asset_forbidden_error_response_instance.to_dict()
# create an instance of AssetForbiddenErrorResponse from a dict
asset_forbidden_error_response_from_dict = AssetForbiddenErrorResponse.from_dict(asset_forbidden_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


