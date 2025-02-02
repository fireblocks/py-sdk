# AddExchangeAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Exchange account&#39;s identifier | [optional] 
**name** | **str** | Display name of the exchange account | [optional] 
**exchange_type** | [**ExchangeType**](ExchangeType.md) |  | [optional] 

## Example

```python
from fireblocks.models.add_exchange_account_response import AddExchangeAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddExchangeAccountResponse from a JSON string
add_exchange_account_response_instance = AddExchangeAccountResponse.from_json(json)
# print the JSON string representation of the object
print(AddExchangeAccountResponse.to_json())

# convert the object into a dict
add_exchange_account_response_dict = add_exchange_account_response_instance.to_dict()
# create an instance of AddExchangeAccountResponse from a dict
add_exchange_account_response_from_dict = AddExchangeAccountResponse.from_dict(add_exchange_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


