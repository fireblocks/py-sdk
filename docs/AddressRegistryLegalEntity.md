# AddressRegistryLegalEntity

Legal entity resolved for an address-registry lookup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | Legal entity / company display name | 
**country_code** | **str** | Jurisdiction country code (e.g. ISO 3166-1 alpha-2) | 
**company_id** | **str** | Company identifier for the resolved legal entity (UUID) | 

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


