# ToExchangeTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**dst_address** | **str** |  | [optional] 
**dst_tag** | **str** | optional | [optional] 

## Example

```python
from fireblocks_client.models.to_exchange_transaction import ToExchangeTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ToExchangeTransaction from a JSON string
to_exchange_transaction_instance = ToExchangeTransaction.from_json(json)
# print the JSON string representation of the object
print ToExchangeTransaction.to_json()

# convert the object into a dict
to_exchange_transaction_dict = to_exchange_transaction_instance.to_dict()
# create an instance of ToExchangeTransaction from a dict
to_exchange_transaction_form_dict = to_exchange_transaction.from_dict(to_exchange_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


