# GetAuditLogsResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** |  | [optional] 
**total** | **float** |  | [optional] 
**cursor** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.get_audit_logs_response_dto import GetAuditLogsResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuditLogsResponseDTO from a JSON string
get_audit_logs_response_dto_instance = GetAuditLogsResponseDTO.from_json(json)
# print the JSON string representation of the object
print(GetAuditLogsResponseDTO.to_json())

# convert the object into a dict
get_audit_logs_response_dto_dict = get_audit_logs_response_dto_instance.to_dict()
# create an instance of GetAuditLogsResponseDTO from a dict
get_audit_logs_response_dto_from_dict = GetAuditLogsResponseDTO.from_dict(get_audit_logs_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


