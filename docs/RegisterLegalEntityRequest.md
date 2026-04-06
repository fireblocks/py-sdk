# RegisterLegalEntityRequest

Request body to register a new legal entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lei** | **str** | Legal Entity Identifier (LEI) code to register. Must be a valid 20-character LEI present in the GLEIF registry. | 
**travel_rule_providers** | [**List[TravelRuleProvider]**](TravelRuleProvider.md) | Travel rule providers to associate with this registration | [optional] 
**travel_rule_contact_email** | **str** | Contact email for travel rule communications | [optional] 

## Example

```python
from fireblocks.models.register_legal_entity_request import RegisterLegalEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterLegalEntityRequest from a JSON string
register_legal_entity_request_instance = RegisterLegalEntityRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterLegalEntityRequest.to_json())

# convert the object into a dict
register_legal_entity_request_dict = register_legal_entity_request_instance.to_dict()
# create an instance of RegisterLegalEntityRequest from a dict
register_legal_entity_request_from_dict = RegisterLegalEntityRequest.from_dict(register_legal_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


