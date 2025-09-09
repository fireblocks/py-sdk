# PersonalIdentification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_reference_id** | **str** |  | 
**entity_type** | **str** |  | 
**participant_relationship_type** | [**ParticipantRelationshipType**](ParticipantRelationshipType.md) |  | 
**full_name** | [**PersonalIdentificationFullName**](PersonalIdentificationFullName.md) |  | 
**date_of_birth** | **date** |  | 
**postal_address** | [**PostalAddress**](PostalAddress.md) |  | 

## Example

```python
from fireblocks.models.personal_identification import PersonalIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalIdentification from a JSON string
personal_identification_instance = PersonalIdentification.from_json(json)
# print the JSON string representation of the object
print(PersonalIdentification.to_json())

# convert the object into a dict
personal_identification_dict = personal_identification_instance.to_dict()
# create an instance of PersonalIdentification from a dict
personal_identification_from_dict = PersonalIdentification.from_dict(personal_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


