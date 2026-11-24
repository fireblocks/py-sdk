# ReadOnlyDraftReviewAndValidationResponse

Read-only draft validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft_response** | [**ReadOnlyDraftResponse**](ReadOnlyDraftResponse.md) |  | 
**validation** | [**PolicyValidation**](PolicyValidation.md) |  | 

## Example

```python
from fireblocks.models.read_only_draft_review_and_validation_response import ReadOnlyDraftReviewAndValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadOnlyDraftReviewAndValidationResponse from a JSON string
read_only_draft_review_and_validation_response_instance = ReadOnlyDraftReviewAndValidationResponse.from_json(json)
# print the JSON string representation of the object
print(ReadOnlyDraftReviewAndValidationResponse.to_json())

# convert the object into a dict
read_only_draft_review_and_validation_response_dict = read_only_draft_review_and_validation_response_instance.to_dict()
# create an instance of ReadOnlyDraftReviewAndValidationResponse from a dict
read_only_draft_review_and_validation_response_from_dict = ReadOnlyDraftReviewAndValidationResponse.from_dict(read_only_draft_review_and_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


