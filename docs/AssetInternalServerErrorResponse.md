# AssetInternalServerErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Internal server error code | 
**code** | **str** | Error code | 

## Example

```python
from fireblocks_client.models.asset_internal_server_error_response import AssetInternalServerErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetInternalServerErrorResponse from a JSON string
asset_internal_server_error_response_instance = AssetInternalServerErrorResponse.from_json(json)
# print the JSON string representation of the object
print AssetInternalServerErrorResponse.to_json()

# convert the object into a dict
asset_internal_server_error_response_dict = asset_internal_server_error_response_instance.to_dict()
# create an instance of AssetInternalServerErrorResponse from a dict
asset_internal_server_error_response_form_dict = asset_internal_server_error_response.from_dict(asset_internal_server_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


