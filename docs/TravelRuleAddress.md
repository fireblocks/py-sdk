# TravelRuleAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** | Street address | 
**city** | **str** | City | 
**state** | **str** | State or province | 
**postal_code** | **str** | Postal or ZIP code | 

## Example

```python
from fireblocks.models.travel_rule_address import TravelRuleAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleAddress from a JSON string
travel_rule_address_instance = TravelRuleAddress.from_json(json)
# print the JSON string representation of the object
print(TravelRuleAddress.to_json())

# convert the object into a dict
travel_rule_address_dict = travel_rule_address_instance.to_dict()
# create an instance of TravelRuleAddress from a dict
travel_rule_address_from_dict = TravelRuleAddress.from_dict(travel_rule_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


