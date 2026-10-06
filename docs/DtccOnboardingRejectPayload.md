# DtccOnboardingRejectPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Why the offer is being rejected. Recorded on-chain, where the counterparty can read it. | 

## Example

```python
from fireblocks.models.dtcc_onboarding_reject_payload import DtccOnboardingRejectPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DtccOnboardingRejectPayload from a JSON string
dtcc_onboarding_reject_payload_instance = DtccOnboardingRejectPayload.from_json(json)
# print the JSON string representation of the object
print(DtccOnboardingRejectPayload.to_json())

# convert the object into a dict
dtcc_onboarding_reject_payload_dict = dtcc_onboarding_reject_payload_instance.to_dict()
# create an instance of DtccOnboardingRejectPayload from a dict
dtcc_onboarding_reject_payload_from_dict = DtccOnboardingRejectPayload.from_dict(dtcc_onboarding_reject_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


