# TravelRulePiiIVMS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**date_of_birth** | **str** |  | 
**place_of_birth** | **str** |  | 
**address** | **str** |  | 
**identification_number** | **str** |  | 
**nationality** | **str** |  | 
**country_of_residence** | **str** |  | 
**tax_identification_number** | **str** |  | 
**customer_number** | **str** |  | 

## Example

```python
from fireblocks_client.models.travel_rule_pii_ivms import TravelRulePiiIVMS

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRulePiiIVMS from a JSON string
travel_rule_pii_ivms_instance = TravelRulePiiIVMS.from_json(json)
# print the JSON string representation of the object
print TravelRulePiiIVMS.to_json()

# convert the object into a dict
travel_rule_pii_ivms_dict = travel_rule_pii_ivms_instance.to_dict()
# create an instance of TravelRulePiiIVMS from a dict
travel_rule_pii_ivms_form_dict = travel_rule_pii_ivms.from_dict(travel_rule_pii_ivms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


