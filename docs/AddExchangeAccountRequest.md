# AddExchangeAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_type** | [**ExchangeType**](ExchangeType.md) |  | 
**name** | **str** | Display name of the exchange account | 
**creds** | **str** | Encrypted credentials | [optional] 
**key** | **str** | Api key of the exchange | [optional] 
**main_account_id** | **str** | Optional - main account id of the exchange | [optional] 

## Example

```python
from fireblocks.models.add_exchange_account_request import AddExchangeAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddExchangeAccountRequest from a JSON string
add_exchange_account_request_instance = AddExchangeAccountRequest.from_json(json)
# print the JSON string representation of the object
print(AddExchangeAccountRequest.to_json())

# convert the object into a dict
add_exchange_account_request_dict = add_exchange_account_request_instance.to_dict()
# create an instance of AddExchangeAccountRequest from a dict
add_exchange_account_request_from_dict = AddExchangeAccountRequest.from_dict(add_exchange_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


