# TRLinkSetDestinationTravelRuleMessageIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the operation was successful | 
**updated_destinations** | **float** | Number of destinations updated | 
**failed_destinations** | **float** | Number of destinations that failed to update | 
**errors** | **List[str]** | List of errors (if any) | [optional] 

## Example

```python
from fireblocks.models.tr_link_set_destination_travel_rule_message_id_response import TRLinkSetDestinationTravelRuleMessageIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkSetDestinationTravelRuleMessageIdResponse from a JSON string
tr_link_set_destination_travel_rule_message_id_response_instance = TRLinkSetDestinationTravelRuleMessageIdResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkSetDestinationTravelRuleMessageIdResponse.to_json())

# convert the object into a dict
tr_link_set_destination_travel_rule_message_id_response_dict = tr_link_set_destination_travel_rule_message_id_response_instance.to_dict()
# create an instance of TRLinkSetDestinationTravelRuleMessageIdResponse from a dict
tr_link_set_destination_travel_rule_message_id_response_from_dict = TRLinkSetDestinationTravelRuleMessageIdResponse.from_dict(tr_link_set_destination_travel_rule_message_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


