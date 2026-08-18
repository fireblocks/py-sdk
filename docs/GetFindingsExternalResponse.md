# GetFindingsExternalResponse

A paginated list of FSPM findings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SecurityFinding]**](SecurityFinding.md) | List of FSPM findings for the current page. | 
**total** | **int** | Total number of findings matching the query. | 
**next** | **str** | Cursor for the next page of results, omitted when there are no more results. | [optional] 

## Example

```python
from fireblocks.models.get_findings_external_response import GetFindingsExternalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFindingsExternalResponse from a JSON string
get_findings_external_response_instance = GetFindingsExternalResponse.from_json(json)
# print the JSON string representation of the object
print(GetFindingsExternalResponse.to_json())

# convert the object into a dict
get_findings_external_response_dict = get_findings_external_response_instance.to_dict()
# create an instance of GetFindingsExternalResponse from a dict
get_findings_external_response_from_dict = GetFindingsExternalResponse.from_dict(get_findings_external_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


