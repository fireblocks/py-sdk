# OnboardingResponseDtccAccept

Accept a DTCC end-investor onboarding offer. Carries no arguments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the offer. Must be one of the values currently listed in the transaction&#39;s &#x60;additionalInfo.cantonDetails.offerResponse.availableResponses&#x60;. | 

## Example

```python
from fireblocks.models.onboarding_response_dtcc_accept import OnboardingResponseDtccAccept

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingResponseDtccAccept from a JSON string
onboarding_response_dtcc_accept_instance = OnboardingResponseDtccAccept.from_json(json)
# print the JSON string representation of the object
print(OnboardingResponseDtccAccept.to_json())

# convert the object into a dict
onboarding_response_dtcc_accept_dict = onboarding_response_dtcc_accept_instance.to_dict()
# create an instance of OnboardingResponseDtccAccept from a dict
onboarding_response_dtcc_accept_from_dict = OnboardingResponseDtccAccept.from_dict(onboarding_response_dtcc_accept_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


