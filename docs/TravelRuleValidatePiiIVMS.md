# TravelRuleValidatePiiIVMS

Information about the originator of the transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**originator_persons** | [**List[TravelRuleValidatePerson]**](TravelRuleValidatePerson.md) | Information about the originator of the transaction | [optional] 
**beneficiary_persons** | [**List[TravelRuleValidatePerson]**](TravelRuleValidatePerson.md) | Information about the beneficiary of the transaction | [optional] 
**account_number** | **List[str]** | Beneficiary account number | [optional] 

## Example

```python
from fireblocks.models.travel_rule_validate_pii_ivms import TravelRuleValidatePiiIVMS

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidatePiiIVMS from a JSON string
travel_rule_validate_pii_ivms_instance = TravelRuleValidatePiiIVMS.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidatePiiIVMS.to_json())

# convert the object into a dict
travel_rule_validate_pii_ivms_dict = travel_rule_validate_pii_ivms_instance.to_dict()
# create an instance of TravelRuleValidatePiiIVMS from a dict
travel_rule_validate_pii_ivms_from_dict = TravelRuleValidatePiiIVMS.from_dict(travel_rule_validate_pii_ivms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


