# TravelRuleUpdateVASPDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**did** | **str** | The decentralized identifier of the VASP | 
**pii_didkey** | **str** | The PII DID key of the VASP | 

## Example

```python
from fireblocks_client.models.travel_rule_update_vasp_details import TravelRuleUpdateVASPDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleUpdateVASPDetails from a JSON string
travel_rule_update_vasp_details_instance = TravelRuleUpdateVASPDetails.from_json(json)
# print the JSON string representation of the object
print TravelRuleUpdateVASPDetails.to_json()

# convert the object into a dict
travel_rule_update_vasp_details_dict = travel_rule_update_vasp_details_instance.to_dict()
# create an instance of TravelRuleUpdateVASPDetails from a dict
travel_rule_update_vasp_details_form_dict = travel_rule_update_vasp_details.from_dict(travel_rule_update_vasp_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


