# Identification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_reference_id** | **str** |  | 
**entity_type** | **str** |  | 
**participant_relationship_type** | [**ParticipantRelationshipType**](ParticipantRelationshipType.md) |  | 
**full_name** | [**PersonalIdentificationFullName**](PersonalIdentificationFullName.md) |  | 
**date_of_birth** | **date** |  | 
**postal_address** | [**PostalAddress**](PostalAddress.md) |  | 
**business_name** | **str** |  | 
**registration_number** | **str** |  | 

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


