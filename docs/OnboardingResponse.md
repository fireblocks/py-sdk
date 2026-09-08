# OnboardingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the offer. Must be one of the values currently listed in the transaction&#39;s &#x60;additionalInfo.cantonDetails.offerResponse.availableResponses&#x60;. | 
**reason** | **str** | Why the offer is being rejected. Recorded on-chain, where the counterparty can read it. | 

## Example

```python
from fireblocks.models.onboarding_response import OnboardingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingResponse from a JSON string
onboarding_response_instance = OnboardingResponse.from_json(json)
# print the JSON string representation of the object
print(OnboardingResponse.to_json())

# convert the object into a dict
onboarding_response_dict = onboarding_response_instance.to_dict()
# create an instance of OnboardingResponse from a dict
onboarding_response_from_dict = OnboardingResponse.from_dict(onboarding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


