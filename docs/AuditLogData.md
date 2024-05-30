# AuditLogData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the audit log | [optional] 
**timestamp** | **str** | The timestamp of the audit log | [optional] 
**created_at** | **str** | The timestamp of the audit log creation | [optional] 
**user** | **str** | The user who performed the action | [optional] 
**subject** | **str** | The subject of the action | [optional] 
**event** | **str** | The event that was performed | [optional] 
**tenant_id** | **str** | The tenant ID of the audit log | [optional] 
**user_id** | **str** | The user ID of the audit log | [optional] 

## Example

```python
from fireblocks.models.audit_log_data import AuditLogData

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogData from a JSON string
audit_log_data_instance = AuditLogData.from_json(json)
# print the JSON string representation of the object
print(AuditLogData.to_json())

# convert the object into a dict
audit_log_data_dict = audit_log_data_instance.to_dict()
# create an instance of AuditLogData from a dict
audit_log_data_from_dict = AuditLogData.from_dict(audit_log_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


