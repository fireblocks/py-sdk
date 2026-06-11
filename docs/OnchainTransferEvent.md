# OnchainTransferEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the transfer event | 
**transaction_hash** | **str** | Hash of the transaction containing this transfer | 
**log_index** | **str** | Index of the log within the transaction | 
**contract_address** | **str** | Address of the token contract | 
**from_address** | **str** | Address that sent the tokens | 
**to_address** | **str** | Address that received the tokens | 
**value** | **str** | Amount of tokens transferred (in smallest unit) | 
**chain_id** | **int** | Chain ID of the blockchain | 
**base_asset_id** | **str** | The blockchain base asset identifier | 
**block_number** | **int** | Block number containing this transfer | 
**block_hash** | **str** | Hash of the block containing this transfer | 
**block_timestamp** | **datetime** | Timestamp when the block was mined | 
**event_name** | **str** | Name of the event (typically \&quot;Transfer\&quot;) | 

## Example

```python
from fireblocks.models.onchain_transfer_event import OnchainTransferEvent

# TODO update the JSON string below
json = "{}"
# create an instance of OnchainTransferEvent from a JSON string
onchain_transfer_event_instance = OnchainTransferEvent.from_json(json)
# print the JSON string representation of the object
print(OnchainTransferEvent.to_json())

# convert the object into a dict
onchain_transfer_event_dict = onchain_transfer_event_instance.to_dict()
# create an instance of OnchainTransferEvent from a dict
onchain_transfer_event_from_dict = OnchainTransferEvent.from_dict(onchain_transfer_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


