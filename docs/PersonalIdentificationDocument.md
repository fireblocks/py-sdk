# PersonalIdentificationDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identification document number. | [optional] 
**type** | [**PersonalIdentificationType**](PersonalIdentificationType.md) |  | [optional] 
**expiration_date** | **date** | The expiration date of the identification document. | [optional] 

## Example

```python
from fireblocks.models.personal_identification_document import PersonalIdentificationDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalIdentificationDocument from a JSON string
personal_identification_document_instance = PersonalIdentificationDocument.from_json(json)
# print the JSON string representation of the object
print(PersonalIdentificationDocument.to_json())

# convert the object into a dict
personal_identification_document_dict = personal_identification_document_instance.to_dict()
# create an instance of PersonalIdentificationDocument from a dict
personal_identification_document_from_dict = PersonalIdentificationDocument.from_dict(personal_identification_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


