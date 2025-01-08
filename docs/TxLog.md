# TxLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The log address | 
**topics** | **List[str]** | Array of log topics | 
**data** | **str** | The log data | 
**block_number** | **int** | Block number where the log occurred | 
**transaction_hash** | **str** | Transaction hash associated with the log | 
**transaction_index** | **int** | Transaction index in the block | 
**block_hash** | **str** | The hash of the block | 
**log_index** | **int** | Log index in the block | 
**removed** | **bool** | Indicates if the log was removed | 

## Example

```python
from fireblocks.models.tx_log import TxLog

# TODO update the JSON string below
json = "{}"
# create an instance of TxLog from a JSON string
tx_log_instance = TxLog.from_json(json)
# print the JSON string representation of the object
print(TxLog.to_json())

# convert the object into a dict
tx_log_dict = tx_log_instance.to_dict()
# create an instance of TxLog from a dict
tx_log_from_dict = TxLog.from_dict(tx_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


