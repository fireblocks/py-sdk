# GetBulkSigningKeysJobsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BulkSigningKeyJob]**](BulkSigningKeyJob.md) | Registration jobs for the workspace, newest first. | 
**next** | **str** | Cursor to the next page. Absent on the last page. | [optional] 

## Example

```python
from fireblocks.models.get_bulk_signing_keys_jobs_response import GetBulkSigningKeysJobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBulkSigningKeysJobsResponse from a JSON string
get_bulk_signing_keys_jobs_response_instance = GetBulkSigningKeysJobsResponse.from_json(json)
# print the JSON string representation of the object
print(GetBulkSigningKeysJobsResponse.to_json())

# convert the object into a dict
get_bulk_signing_keys_jobs_response_dict = get_bulk_signing_keys_jobs_response_instance.to_dict()
# create an instance of GetBulkSigningKeysJobsResponse from a dict
get_bulk_signing_keys_jobs_response_from_dict = GetBulkSigningKeysJobsResponse.from_dict(get_bulk_signing_keys_jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


