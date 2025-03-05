# TravelRuleVASP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**did** | **str** |  | 
**name** | **str** |  | 
**verification_status** | **str** |  | 
**address_line1** | **str** |  | 
**address_line2** | **str** |  | 
**city** | **str** |  | 
**country** | **str** |  | 
**email_domains** | **str** |  | 
**website** | **str** |  | 
**logo** | **str** |  | 
**legal_structure** | **str** |  | 
**legal_name** | **str** |  | 
**year_founded** | **str** |  | 
**incorporation_country** | **str** |  | 
**is_regulated** | **str** |  | 
**other_names** | **str** |  | 
**identification_type** | **str** |  | 
**identification_country** | **str** |  | 
**business_number** | **str** |  | 
**regulatory_authorities** | **str** |  | 
**jurisdictions** | **str** |  | 
**street** | **str** |  | 
**number** | **str** |  | 
**unit** | **str** |  | 
**post_code** | **str** |  | 
**state** | **str** |  | 
**certificates** | **str** |  | 
**description** | **str** |  | 
**travel_rule_openvasp** | **str** |  | 
**travel_rule_sygna** | **str** |  | 
**travel_rule_trisa** | **str** |  | 
**travel_rule_trlight** | **str** |  | 
**travel_rule_email** | **str** |  | 
**travel_rule_trp** | **str** |  | 
**travel_rule_shyft** | **str** |  | 
**travel_rule_ustravelrulewg** | **str** |  | 
**created_at** | **str** |  | 
**created_by** | **str** |  | 
**updated_at** | **str** |  | 
**updated_by** | **str** |  | 
**last_sent_date** | **str** |  | 
**last_received_date** | **str** |  | 
**documents** | **str** |  | 
**has_admin** | **bool** |  | 
**is_notifiable** | **bool** |  | 
**issuers** | [**TravelRuleIssuers**](TravelRuleIssuers.md) |  | 

## Example

```python
from fireblocks.models.travel_rule_vasp import TravelRuleVASP

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleVASP from a JSON string
travel_rule_vasp_instance = TravelRuleVASP.from_json(json)
# print the JSON string representation of the object
print(TravelRuleVASP.to_json())

# convert the object into a dict
travel_rule_vasp_dict = travel_rule_vasp_instance.to_dict()
# create an instance of TravelRuleVASP from a dict
travel_rule_vasp_from_dict = TravelRuleVASP.from_dict(travel_rule_vasp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


