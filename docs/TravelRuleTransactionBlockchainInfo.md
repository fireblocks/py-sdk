# TravelRuleTransactionBlockchainInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_hash** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 
**destination** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.travel_rule_transaction_blockchain_info import TravelRuleTransactionBlockchainInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleTransactionBlockchainInfo from a JSON string
travel_rule_transaction_blockchain_info_instance = TravelRuleTransactionBlockchainInfo.from_json(json)
# print the JSON string representation of the object
print TravelRuleTransactionBlockchainInfo.to_json()

# convert the object into a dict
travel_rule_transaction_blockchain_info_dict = travel_rule_transaction_blockchain_info_instance.to_dict()
# create an instance of TravelRuleTransactionBlockchainInfo from a dict
travel_rule_transaction_blockchain_info_form_dict = travel_rule_transaction_blockchain_info.from_dict(travel_rule_transaction_blockchain_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


