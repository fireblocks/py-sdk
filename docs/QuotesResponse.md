# QuotesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotes** | [**List[Quote]**](Quote.md) |  | [optional] 

## Example

```python
from fireblocks.models.quotes_response import QuotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuotesResponse from a JSON string
quotes_response_instance = QuotesResponse.from_json(json)
# print the JSON string representation of the object
print(QuotesResponse.to_json())

# convert the object into a dict
quotes_response_dict = quotes_response_instance.to_dict()
# create an instance of QuotesResponse from a dict
quotes_response_from_dict = QuotesResponse.from_dict(quotes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


