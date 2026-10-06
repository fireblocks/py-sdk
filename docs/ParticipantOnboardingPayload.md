# ParticipantOnboardingPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The vault account that acts as the participant. Its Canton party is derived for you. | 
**blockchain_id** | **str** | The blockchain this party is connected to — &#x60;CANTON&#x60; or &#x60;CANTON_TEST&#x60;. | 
**expires_at** | **datetime** | When the onboarding request expires if it has not been answered. RFC 3339. | [optional] 
**operator** | **str** | DTCC infra operator party id. | 
**compliance** | **str** | DTCC compliance party id. | 
**registrar** | **str** | DTCC registrar party id — co-signs the accept. | 
**client_onboarder** | **str** | DTCC client onboarder party id — co-signs the accept. | 
**upgrader** | **str** | DTCC upgrader party id — the Model Upgrade Tool authority. Supplied by DTCC during the off-chain registration, alongside the other party ids. | 

## Example

```python
from fireblocks.models.participant_onboarding_payload import ParticipantOnboardingPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantOnboardingPayload from a JSON string
participant_onboarding_payload_instance = ParticipantOnboardingPayload.from_json(json)
# print the JSON string representation of the object
print(ParticipantOnboardingPayload.to_json())

# convert the object into a dict
participant_onboarding_payload_dict = participant_onboarding_payload_instance.to_dict()
# create an instance of ParticipantOnboardingPayload from a dict
participant_onboarding_payload_from_dict = ParticipantOnboardingPayload.from_dict(participant_onboarding_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


