# ParticipantOnboardingPayload

Optional, and so is every field in it: omit `payload` entirely to onboard with DTCC's published parties for the blockchain and the default expiry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | When the onboarding request expires if it has not been answered. RFC 3339. | [optional] 
**operator** | **str** | DTCC infra operator party id. Optional — overrides the service&#39;s default for the blockchain. | [optional] 
**compliance** | **str** | DTCC compliance party id. Optional — overrides the service&#39;s default for the blockchain. | [optional] 
**registrar** | **str** | DTCC registrar party id — co-signs the accept. Optional — overrides the service&#39;s default for the blockchain. | [optional] 
**client_onboarder** | **str** | DTCC client onboarder party id — co-signs the accept. Optional — overrides the service&#39;s default for the blockchain. | [optional] 
**upgrader** | **str** | DTCC upgrader party id — the Model Upgrade Tool authority. Optional — overrides the service&#39;s default for the blockchain. | [optional] 

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


