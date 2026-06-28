# AllowlistEntryResponse

Single allowlist entry envelope, paired with the account-level allowlist sync metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AllowlistEntry**](AllowlistEntry.md) |  | 
**metadata** | [**AllowlistMetadata**](AllowlistMetadata.md) |  | [optional] 

## Example

```python
from fireblocks.models.allowlist_entry_response import AllowlistEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllowlistEntryResponse from a JSON string
allowlist_entry_response_instance = AllowlistEntryResponse.from_json(json)
# print the JSON string representation of the object
print(AllowlistEntryResponse.to_json())

# convert the object into a dict
allowlist_entry_response_dict = allowlist_entry_response_instance.to_dict()
# create an instance of AllowlistEntryResponse from a dict
allowlist_entry_response_from_dict = AllowlistEntryResponse.from_dict(allowlist_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


