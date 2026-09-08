# OnboardingResponseTradewebReject

Reject a Tradeweb co-signing delegation offer. Carries no arguments — the DAR has nowhere on-ledger to record a reason, so none is accepted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the offer. Must be one of the values currently listed in the transaction&#39;s &#x60;additionalInfo.cantonDetails.offerResponse.availableResponses&#x60;. | 

## Example

```python
from fireblocks.models.onboarding_response_tradeweb_reject import OnboardingResponseTradewebReject

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingResponseTradewebReject from a JSON string
onboarding_response_tradeweb_reject_instance = OnboardingResponseTradewebReject.from_json(json)
# print the JSON string representation of the object
print(OnboardingResponseTradewebReject.to_json())

# convert the object into a dict
onboarding_response_tradeweb_reject_dict = onboarding_response_tradeweb_reject_instance.to_dict()
# create an instance of OnboardingResponseTradewebReject from a dict
onboarding_response_tradeweb_reject_from_dict = OnboardingResponseTradewebReject.from_dict(onboarding_response_tradeweb_reject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


