# Blockchain

Blockchain entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique blockchain identifier. | 
**blockchain_state** | **str** | Current lifecycle state of the blockchain. | 
**declared_properties** | [**BlockchainDeclaredProperties**](BlockchainDeclaredProperties.md) |  | 
**created_at_utc** | **float** | Creation timestamp (epoch milliseconds, UTC). | 
**updated_at_utc** | **float** | Last update timestamp (epoch milliseconds, UTC). | 
**validation_session_id** | **str** | Validation session data (optional - only present if validation session exists) | [optional] 
**validation_status** | **str** | Status of the latest validation session. | [optional] 
**validation_created_at_utc** | **float** | Validation session creation timestamp (epoch milliseconds, UTC). | [optional] 
**validation_updated_at_utc** | **float** | Validation session last update timestamp (epoch milliseconds, UTC). | [optional] 
**validation_completed_at_utc** | **float** | Validation session completion timestamp (epoch milliseconds, UTC). | [optional] 
**validation_failure_reasons** | **List[str]** | Reasons the latest validation failed, if any. | 
**failed_step** | **str** | Business step at which the activation flow failed. Absent when no failure has been recorded. | [optional] 

## Example

```python
from fireblocks.models.blockchain import Blockchain

# TODO update the JSON string below
json = "{}"
# create an instance of Blockchain from a JSON string
blockchain_instance = Blockchain.from_json(json)
# print the JSON string representation of the object
print(Blockchain.to_json())

# convert the object into a dict
blockchain_dict = blockchain_instance.to_dict()
# create an instance of Blockchain from a dict
blockchain_from_dict = Blockchain.from_dict(blockchain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


