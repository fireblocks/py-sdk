# CreateBulkSigningKeysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Id of the registration job. Poll it for progress. | 

## Example

```python
from fireblocks.models.create_bulk_signing_keys_response import CreateBulkSigningKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkSigningKeysResponse from a JSON string
create_bulk_signing_keys_response_instance = CreateBulkSigningKeysResponse.from_json(json)
# print the JSON string representation of the object
print(CreateBulkSigningKeysResponse.to_json())

# convert the object into a dict
create_bulk_signing_keys_response_dict = create_bulk_signing_keys_response_instance.to_dict()
# create an instance of CreateBulkSigningKeysResponse from a dict
create_bulk_signing_keys_response_from_dict = CreateBulkSigningKeysResponse.from_dict(create_bulk_signing_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


