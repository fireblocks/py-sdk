# TRLinkSetTransactionTravelRuleMessageIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**travel_rule_message_id** | **str** | Travel Rule Message ID to associate with transaction (null to unset) | 

## Example

```python
from fireblocks.models.tr_link_set_transaction_travel_rule_message_id_request import TRLinkSetTransactionTravelRuleMessageIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkSetTransactionTravelRuleMessageIdRequest from a JSON string
tr_link_set_transaction_travel_rule_message_id_request_instance = TRLinkSetTransactionTravelRuleMessageIdRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkSetTransactionTravelRuleMessageIdRequest.to_json())

# convert the object into a dict
tr_link_set_transaction_travel_rule_message_id_request_dict = tr_link_set_transaction_travel_rule_message_id_request_instance.to_dict()
# create an instance of TRLinkSetTransactionTravelRuleMessageIdRequest from a dict
tr_link_set_transaction_travel_rule_message_id_request_from_dict = TRLinkSetTransactionTravelRuleMessageIdRequest.from_dict(tr_link_set_transaction_travel_rule_message_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


