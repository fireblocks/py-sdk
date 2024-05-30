# CreateAssetsBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | The ID of the new asset | [optional] 
**vault_account_id_from** | **str** | The smallest vault account ID in the range | [optional] 
**vault_account_id_to** | **str** | The largest vault account ID in the range | [optional] 

## Example

```python
from fireblocks_client.models.create_assets_bulk_request import CreateAssetsBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetsBulkRequest from a JSON string
create_assets_bulk_request_instance = CreateAssetsBulkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAssetsBulkRequest.to_json())

# convert the object into a dict
create_assets_bulk_request_dict = create_assets_bulk_request_instance.to_dict()
# create an instance of CreateAssetsBulkRequest from a dict
create_assets_bulk_request_from_dict = CreateAssetsBulkRequest.from_dict(create_assets_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


