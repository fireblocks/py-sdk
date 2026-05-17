# RatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rates** | [**List[Rate]**](Rate.md) | List of indicative rates returned for the requested asset pair. | 
**errors** | [**List[ScopeItemFailure]**](ScopeItemFailure.md) | Partial failures encountered while requesting rates. Empty when all rate requests succeed. | 

## Example

```python
from fireblocks.models.rates_response import RatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RatesResponse from a JSON string
rates_response_instance = RatesResponse.from_json(json)
# print the JSON string representation of the object
print(RatesResponse.to_json())

# convert the object into a dict
rates_response_dict = rates_response_instance.to_dict()
# create an instance of RatesResponse from a dict
rates_response_from_dict = RatesResponse.from_dict(rates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


