# UpdateAssetUserMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**AssetMetadataRequest**](AssetMetadataRequest.md) |  | [optional] 

## Example

```python
from fireblocks.models.update_asset_user_metadata_request import UpdateAssetUserMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssetUserMetadataRequest from a JSON string
update_asset_user_metadata_request_instance = UpdateAssetUserMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAssetUserMetadataRequest.to_json())

# convert the object into a dict
update_asset_user_metadata_request_dict = update_asset_user_metadata_request_instance.to_dict()
# create an instance of UpdateAssetUserMetadataRequest from a dict
update_asset_user_metadata_request_from_dict = UpdateAssetUserMetadataRequest.from_dict(update_asset_user_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


