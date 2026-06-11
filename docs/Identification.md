# Identification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_reference_id** | **str** |  | 
**entity_type** | [**BusinessEntityTypeEnum**](BusinessEntityTypeEnum.md) |  | 
**participant_relationship_type** | [**ParticipantRelationshipType**](ParticipantRelationshipType.md) |  | 
**full_name** | [**PersonalIdentificationFullName**](PersonalIdentificationFullName.md) |  | 
**date_of_birth** | **date** |  | 
**postal_address** | [**PostalAddress**](PostalAddress.md) |  | 
**email** | **str** |  | [optional] 
**phone** | **str** | Mobile phone number in E.164 format | [optional] 
**id_number** | **str** | Deprecated. Use identificationDocuments instead. | [optional] 
**id_type** | [**PersonalIdentificationType**](PersonalIdentificationType.md) | Deprecated. Use identificationDocuments instead. | [optional] 
**additional_id_number** | **str** | Deprecated. Use identificationDocuments instead. | [optional] 
**additional_id_type** | [**PersonalIdentificationType**](PersonalIdentificationType.md) | Deprecated. Use identificationDocuments instead. | [optional] 
**nationality** | **str** | The ISO-3166 Alpha-2 country code representing the individual&#39;s nationality. | [optional] 
**identification_documents** | [**List[PersonalIdentificationDocument]**](PersonalIdentificationDocument.md) | List of identification documents for the individual. | [optional] 
**business_name** | **str** |  | 
**registration_number** | **str** |  | 
**date_of_registration** | **date** | The date the business was registered. | [optional] 
**country_of_registration** | **str** | The ISO-3166 Alpha-2 country code where the business is registered. | [optional] 

## Example

```python
from fireblocks.models.identification import Identification

# TODO update the JSON string below
json = "{}"
# create an instance of Identification from a JSON string
identification_instance = Identification.from_json(json)
# print the JSON string representation of the object
print(Identification.to_json())

# convert the object into a dict
identification_dict = identification_instance.to_dict()
# create an instance of Identification from a dict
identification_from_dict = Identification.from_dict(identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


