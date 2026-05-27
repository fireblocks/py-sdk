# GetAuditLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuditLogData]**](AuditLogData.md) |  | [optional] 
**next** | **str** | Cursor to pass as pageCursor in the next request. Null when no further pages exist. | [optional] 
**cursor** | **str** | Deprecated. Use next instead. | [optional] 

## Example

```python
from fireblocks.models.get_audit_logs_response import GetAuditLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuditLogsResponse from a JSON string
get_audit_logs_response_instance = GetAuditLogsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAuditLogsResponse.to_json())

# convert the object into a dict
get_audit_logs_response_dict = get_audit_logs_response_instance.to_dict()
# create an instance of GetAuditLogsResponse from a dict
get_audit_logs_response_from_dict = GetAuditLogsResponse.from_dict(get_audit_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


