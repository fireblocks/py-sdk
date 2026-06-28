# AddressRegistryLegalEntity

Legal entity details for a blockchain address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lei_data** | **bool** | Indicates whether LEI (Legal Entity Identifier) data is available for this address from a verified public registry. A value of &#x60;false&#x60; means no LEI record was found. | 
**entity_name** | **str** | Legal entity display name. | 
**jurisdiction** | **str** | Jurisdiction (e.g. ISO 3166-1 alpha-2 country code). | 
**lei** | **str** | Legal Entity Identifier when available. Empty when &#x60;leiData&#x60; is &#x60;false&#x60;. | 
**travel_rule_providers** | [**List[AddressRegistryTravelRuleProvider]**](AddressRegistryTravelRuleProvider.md) |  | 
**email** | **str** | Travel Rule contact email when available. | 

## Example

```python
from fireblocks.models.address_registry_legal_entity import AddressRegistryLegalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryLegalEntity from a JSON string
address_registry_legal_entity_instance = AddressRegistryLegalEntity.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryLegalEntity.to_json())

# convert the object into a dict
address_registry_legal_entity_dict = address_registry_legal_entity_instance.to_dict()
# create an instance of AddressRegistryLegalEntity from a dict
address_registry_legal_entity_from_dict = AddressRegistryLegalEntity.from_dict(address_registry_legal_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


