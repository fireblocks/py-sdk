# DraftReviewAndValidationResponse

Draft validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft_response** | [**DraftResponse**](DraftResponse.md) |  | 
**validation** | [**PolicyValidation**](PolicyValidation.md) |  | 

## Example

```python
from fireblocks.models.draft_review_and_validation_response import DraftReviewAndValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DraftReviewAndValidationResponse from a JSON string
draft_review_and_validation_response_instance = DraftReviewAndValidationResponse.from_json(json)
# print the JSON string representation of the object
print(DraftReviewAndValidationResponse.to_json())

# convert the object into a dict
draft_review_and_validation_response_dict = draft_review_and_validation_response_instance.to_dict()
# create an instance of DraftReviewAndValidationResponse from a dict
draft_review_and_validation_response_from_dict = DraftReviewAndValidationResponse.from_dict(draft_review_and_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


