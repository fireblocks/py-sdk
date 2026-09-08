# CantonCallParticipantOnboarding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Which call to make. Selects the shape of &#x60;payload&#x60;. | 
**payload** | [**ParticipantOnboardingPayload**](ParticipantOnboardingPayload.md) |  | 

## Example

```python
from fireblocks.models.canton_call_participant_onboarding import CantonCallParticipantOnboarding

# TODO update the JSON string below
json = "{}"
# create an instance of CantonCallParticipantOnboarding from a JSON string
canton_call_participant_onboarding_instance = CantonCallParticipantOnboarding.from_json(json)
# print the JSON string representation of the object
print(CantonCallParticipantOnboarding.to_json())

# convert the object into a dict
canton_call_participant_onboarding_dict = canton_call_participant_onboarding_instance.to_dict()
# create an instance of CantonCallParticipantOnboarding from a dict
canton_call_participant_onboarding_from_dict = CantonCallParticipantOnboarding.from_dict(canton_call_participant_onboarding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


