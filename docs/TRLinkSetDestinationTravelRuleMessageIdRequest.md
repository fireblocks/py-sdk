# TRLinkSetDestinationTravelRuleMessageIdRequest

Request to set TRM ID for specific transaction destination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Destination amount for matching | 
**destination** | [**TRLinkTransferPeerPath**](TRLinkTransferPeerPath.md) |  | 
**travel_rule_message_id** | **str** | Travel Rule Message ID to associate with destination (null to unset) | 

## Example

```python
from fireblocks.models.tr_link_set_destination_travel_rule_message_id_request import TRLinkSetDestinationTravelRuleMessageIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkSetDestinationTravelRuleMessageIdRequest from a JSON string
tr_link_set_destination_travel_rule_message_id_request_instance = TRLinkSetDestinationTravelRuleMessageIdRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkSetDestinationTravelRuleMessageIdRequest.to_json())

# convert the object into a dict
tr_link_set_destination_travel_rule_message_id_request_dict = tr_link_set_destination_travel_rule_message_id_request_instance.to_dict()
# create an instance of TRLinkSetDestinationTravelRuleMessageIdRequest from a dict
tr_link_set_destination_travel_rule_message_id_request_from_dict = TRLinkSetDestinationTravelRuleMessageIdRequest.from_dict(tr_link_set_destination_travel_rule_message_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


