# DropTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_status** | **str** |  | [optional] 
**tx_id** | **str** |  | [optional] 
**replaced_tx_hash** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.drop_transaction_response import DropTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DropTransactionResponse from a JSON string
drop_transaction_response_instance = DropTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(DropTransactionResponse.to_json())

# convert the object into a dict
drop_transaction_response_dict = drop_transaction_response_instance.to_dict()
# create an instance of DropTransactionResponse from a dict
drop_transaction_response_from_dict = DropTransactionResponse.from_dict(drop_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


