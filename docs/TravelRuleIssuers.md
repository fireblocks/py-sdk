# TravelRuleIssuers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year_founded** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**is_regulated** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**regulatory_authorities** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**name** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**logo** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**website** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**legal_name** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**legal_structure** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**incorporation_country** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**business_number** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**address_line1** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**city** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**country** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 
**description** | [**TravelRuleIssuer**](TravelRuleIssuer.md) |  | 

## Example

```python
from fireblocks_client.models.travel_rule_issuers import TravelRuleIssuers

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleIssuers from a JSON string
travel_rule_issuers_instance = TravelRuleIssuers.from_json(json)
# print the JSON string representation of the object
print TravelRuleIssuers.to_json()

# convert the object into a dict
travel_rule_issuers_dict = travel_rule_issuers_instance.to_dict()
# create an instance of TravelRuleIssuers from a dict
travel_rule_issuers_form_dict = travel_rule_issuers.from_dict(travel_rule_issuers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


