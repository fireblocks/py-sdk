# BulkSigningKeyJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Id of the registration job. | 
**status** | **str** | QUEUED means the job is waiting for another bulk registration to finish, since only a limited number run at once. IN_PROGRESS means it is running. COMPLETED means every submitted key is present in the workspace. FAILED means the request was refused before any key was registered, so &#x60;reason&#x60; has to be acted on before resubmitting is worth anything. INCOMPLETE means some keys are not registered; resubmitting the same request retries exactly those, and &#x60;reason&#x60; says whether that is likely to help -- keys not registered because of a transient failure will succeed, a key whose certificate or proof was rejected will be rejected again. | 
**total** | **float** | Keys in the submitted request. | 
**created** | **float** | Keys registered by this job. | 
**already_registered** | **float** | Keys already present in the workspace, recognized and skipped. | 
**failed** | **float** | Keys rejected. See &#x60;reason&#x60;. | 
**reason** | **str** | Free text describing what went wrong. Null while the job is healthy. | [optional] 
**file_hash** | **str** | Hex digest over the submitted keys. Two jobs sharing a digest were the same set of keys, which makes a sequence of resubmissions recognizable. | [optional] 
**created_at** | **float** | Creation date (timestamp) in milliseconds. | 
**updated_at** | **float** | Last progress update (timestamp) in milliseconds. | 

## Example

```python
from fireblocks.models.bulk_signing_key_job import BulkSigningKeyJob

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSigningKeyJob from a JSON string
bulk_signing_key_job_instance = BulkSigningKeyJob.from_json(json)
# print the JSON string representation of the object
print(BulkSigningKeyJob.to_json())

# convert the object into a dict
bulk_signing_key_job_dict = bulk_signing_key_job_instance.to_dict()
# create an instance of BulkSigningKeyJob from a dict
bulk_signing_key_job_from_dict = BulkSigningKeyJob.from_dict(bulk_signing_key_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


