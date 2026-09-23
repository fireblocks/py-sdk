# AuditLogEntry

One entry in a screening's append-only audit trail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** | Unix timestamp in seconds when the event occurred, encoded as a string. | 
**event_type** | [**AuditEventTypeEnum**](AuditEventTypeEnum.md) |  | 
**data** | **bytearray** | The event payload, JSON serialised and then base64 encoded. Its shape depends on &#x60;eventType&#x60; — decode it to read the event. | 

## Example

```python
from fireblocks.models.audit_log_entry import AuditLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntry from a JSON string
audit_log_entry_instance = AuditLogEntry.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntry.to_json())

# convert the object into a dict
audit_log_entry_dict = audit_log_entry_instance.to_dict()
# create an instance of AuditLogEntry from a dict
audit_log_entry_from_dict = AuditLogEntry.from_dict(audit_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


