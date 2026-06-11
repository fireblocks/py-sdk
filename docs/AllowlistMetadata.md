# AllowlistMetadata

Allowlist-specific metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_synced_at** | **datetime** | ISO 8601 timestamp of last sync with provider | [optional] 
**sync_status** | **str** | Status of last sync operation | [optional] 

## Example

```python
from fireblocks.models.allowlist_metadata import AllowlistMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AllowlistMetadata from a JSON string
allowlist_metadata_instance = AllowlistMetadata.from_json(json)
# print the JSON string representation of the object
print(AllowlistMetadata.to_json())

# convert the object into a dict
allowlist_metadata_dict = allowlist_metadata_instance.to_dict()
# create an instance of AllowlistMetadata from a dict
allowlist_metadata_from_dict = AllowlistMetadata.from_dict(allowlist_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


