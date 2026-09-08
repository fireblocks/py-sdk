# AccessTypeResponse

Response-only counterpart of AccessType. Used by the `via` field of response schemas (Quote, Rate, OrderDetails, OrderSummary — and therefore QuoteOffer, RateOffer and Offer) so that the PROVIDER variant can expose `subProviders` without that field ever becoming reachable from a request body. Request schemas (CreateOrderRequest.via) keep using AccessType.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates this uses account-based access | 
**provider_id** | **str** | The ID of the provider | 
**account_id** | **str** | The ID of the account | 
**sub_providers** | **List[str]** | The underlying providers or tools that this direct-access route is composed of, in execution order. Response-only: this field is populated by the server and is never accepted from client requests. | [optional] 

## Example

```python
from fireblocks.models.access_type_response import AccessTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTypeResponse from a JSON string
access_type_response_instance = AccessTypeResponse.from_json(json)
# print the JSON string representation of the object
print(AccessTypeResponse.to_json())

# convert the object into a dict
access_type_response_dict = access_type_response_instance.to_dict()
# create an instance of AccessTypeResponse from a dict
access_type_response_from_dict = AccessTypeResponse.from_dict(access_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


