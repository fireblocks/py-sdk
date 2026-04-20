# ResendByQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | The total number of notifications that are scheduled to be resent. | [optional] 

## Example

```python
from fireblocks.models.resend_by_query_response import ResendByQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResendByQueryResponse from a JSON string
resend_by_query_response_instance = ResendByQueryResponse.from_json(json)
# print the JSON string representation of the object
print(ResendByQueryResponse.to_json())

# convert the object into a dict
resend_by_query_response_dict = resend_by_query_response_instance.to_dict()
# create an instance of ResendByQueryResponse from a dict
resend_by_query_response_from_dict = ResendByQueryResponse.from_dict(resend_by_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


