# ParticipantsIdentification

KYC/AML participant identification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**originator** | [**Identification**](Identification.md) |  | [optional] 
**beneficiary** | [**Identification**](Identification.md) |  | [optional] 

## Example

```python
from fireblocks.models.participants_identification import ParticipantsIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantsIdentification from a JSON string
participants_identification_instance = ParticipantsIdentification.from_json(json)
# print the JSON string representation of the object
print(ParticipantsIdentification.to_json())

# convert the object into a dict
participants_identification_dict = participants_identification_instance.to_dict()
# create an instance of ParticipantsIdentification from a dict
participants_identification_from_dict = ParticipantsIdentification.from_dict(participants_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


