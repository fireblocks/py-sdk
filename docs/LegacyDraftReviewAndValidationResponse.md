# LegacyDraftReviewAndValidationResponse

Draft validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft_response** | [**LegacyDraftResponse**](LegacyDraftResponse.md) |  | 
**validation** | [**LegacyPolicyValidation**](LegacyPolicyValidation.md) |  | 

## Example

```python
from fireblocks.models.legacy_draft_review_and_validation_response import LegacyDraftReviewAndValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyDraftReviewAndValidationResponse from a JSON string
legacy_draft_review_and_validation_response_instance = LegacyDraftReviewAndValidationResponse.from_json(json)
# print the JSON string representation of the object
print(LegacyDraftReviewAndValidationResponse.to_json())

# convert the object into a dict
legacy_draft_review_and_validation_response_dict = legacy_draft_review_and_validation_response_instance.to_dict()
# create an instance of LegacyDraftReviewAndValidationResponse from a dict
legacy_draft_review_and_validation_response_from_dict = LegacyDraftReviewAndValidationResponse.from_dict(legacy_draft_review_and_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


