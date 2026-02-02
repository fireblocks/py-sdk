# DecodedLog

Decoded event log from a blockchain transaction. Note - Additional dynamic properties may be present beyond the required ones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Contract address that emitted the log | 
**block_hash** | **str** | Hash of the block containing this log | 
**block_number** | **str** | Block number containing this log | 
**transaction_hash** | **str** | Hash of the transaction that generated this log | 
**log_index** | **str** | Index of the log in the transaction | 

## Example

```python
from fireblocks.models.decoded_log import DecodedLog

# TODO update the JSON string below
json = "{}"
# create an instance of DecodedLog from a JSON string
decoded_log_instance = DecodedLog.from_json(json)
# print the JSON string representation of the object
print(DecodedLog.to_json())

# convert the object into a dict
decoded_log_dict = decoded_log_instance.to_dict()
# create an instance of DecodedLog from a dict
decoded_log_from_dict = DecodedLog.from_dict(decoded_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


