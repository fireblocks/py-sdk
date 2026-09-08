# DirectAccessResponseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_providers** | **List[str]** | The underlying providers or tools that this direct-access route is composed of, in execution order. Response-only: this field is populated by the server and is never accepted from client requests. | [optional] 

## Example

```python
from fireblocks.models.direct_access_response_info import DirectAccessResponseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DirectAccessResponseInfo from a JSON string
direct_access_response_info_instance = DirectAccessResponseInfo.from_json(json)
# print the JSON string representation of the object
print(DirectAccessResponseInfo.to_json())

# convert the object into a dict
direct_access_response_info_dict = direct_access_response_info_instance.to_dict()
# create an instance of DirectAccessResponseInfo from a dict
direct_access_response_info_from_dict = DirectAccessResponseInfo.from_dict(direct_access_response_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


