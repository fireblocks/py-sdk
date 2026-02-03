# AccessRegistrySummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_active_addresses** | **float** | The total number of active addresses in the access registry | 

## Example

```python
from fireblocks.models.access_registry_summary_response import AccessRegistrySummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRegistrySummaryResponse from a JSON string
access_registry_summary_response_instance = AccessRegistrySummaryResponse.from_json(json)
# print the JSON string representation of the object
print(AccessRegistrySummaryResponse.to_json())

# convert the object into a dict
access_registry_summary_response_dict = access_registry_summary_response_instance.to_dict()
# create an instance of AccessRegistrySummaryResponse from a dict
access_registry_summary_response_from_dict = AccessRegistrySummaryResponse.from_dict(access_registry_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


