# AddressRegistryLegalEntityLegacy

Narrow legacy response for deprecated `GET /v1/address_registry/legal_entity?address=…`. Use `GET /v1/address_registry/legal_entities/{address}` for the full field set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | Legal entity / company display name | 
**country_code** | **str** | Jurisdiction country code (e.g. ISO 3166-1 alpha-2) | 
**company_id** | **str** | Company identifier for the resolved legal entity (UUID) | 

## Example

```python
from fireblocks.models.address_registry_legal_entity_legacy import AddressRegistryLegalEntityLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryLegalEntityLegacy from a JSON string
address_registry_legal_entity_legacy_instance = AddressRegistryLegalEntityLegacy.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryLegalEntityLegacy.to_json())

# convert the object into a dict
address_registry_legal_entity_legacy_dict = address_registry_legal_entity_legacy_instance.to_dict()
# create an instance of AddressRegistryLegalEntityLegacy from a dict
address_registry_legal_entity_legacy_from_dict = AddressRegistryLegalEntityLegacy.from_dict(address_registry_legal_entity_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


