# BusinessIdentification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_reference_id** | **str** |  | 
**entity_type** | [**BusinessEntityTypeEnum**](BusinessEntityTypeEnum.md) |  | 
**participant_relationship_type** | [**ParticipantRelationshipType**](ParticipantRelationshipType.md) |  | 
**business_name** | **str** |  | 
**registration_number** | **str** |  | 
**postal_address** | [**PostalAddress**](PostalAddress.md) |  | 
**email** | **str** |  | [optional] 
**phone** | **str** | Mobile phone number in E.164 format | [optional] 
**date_of_registration** | **date** | The date the business was registered. | [optional] 
**country_of_registration** | **str** | The ISO-3166 Alpha-2 country code where the business is registered. | [optional] 

## Example

```python
from fireblocks.models.business_identification import BusinessIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessIdentification from a JSON string
business_identification_instance = BusinessIdentification.from_json(json)
# print the JSON string representation of the object
print(BusinessIdentification.to_json())

# convert the object into a dict
business_identification_dict = business_identification_instance.to_dict()
# create an instance of BusinessIdentification from a dict
business_identification_from_dict = BusinessIdentification.from_dict(business_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


