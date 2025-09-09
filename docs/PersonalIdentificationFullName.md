# PersonalIdentificationFullName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 

## Example

```python
from fireblocks.models.personal_identification_full_name import PersonalIdentificationFullName

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalIdentificationFullName from a JSON string
personal_identification_full_name_instance = PersonalIdentificationFullName.from_json(json)
# print the JSON string representation of the object
print(PersonalIdentificationFullName.to_json())

# convert the object into a dict
personal_identification_full_name_dict = personal_identification_full_name_instance.to_dict()
# create an instance of PersonalIdentificationFullName from a dict
personal_identification_full_name_from_dict = PersonalIdentificationFullName.from_dict(personal_identification_full_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


