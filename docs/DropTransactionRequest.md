# DropTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** |  | [optional] 
**fee_level** | **str** |  | [optional] 
**gas_price** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.drop_transaction_request import DropTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DropTransactionRequest from a JSON string
drop_transaction_request_instance = DropTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(DropTransactionRequest.to_json())

# convert the object into a dict
drop_transaction_request_dict = drop_transaction_request_instance.to_dict()
# create an instance of DropTransactionRequest from a dict
drop_transaction_request_from_dict = DropTransactionRequest.from_dict(drop_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


