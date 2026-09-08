# DirectAccessResponse

Response-only counterpart of DirectAccess. Adds the server-populated `subProviders` field. Never use this schema in a request body — requests must keep using DirectAccess (via AccessType).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates this uses direct provider access | 
**provider_id** | **str** | The ID of the provider | 
**sub_providers** | **List[str]** | The underlying providers or tools that this direct-access route is composed of, in execution order. Response-only: this field is populated by the server and is never accepted from client requests. | [optional] 

## Example

```python
from fireblocks.models.direct_access_response import DirectAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DirectAccessResponse from a JSON string
direct_access_response_instance = DirectAccessResponse.from_json(json)
# print the JSON string representation of the object
print(DirectAccessResponse.to_json())

# convert the object into a dict
direct_access_response_dict = direct_access_response_instance.to_dict()
# create an instance of DirectAccessResponse from a dict
direct_access_response_from_dict = DirectAccessResponse.from_dict(direct_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


