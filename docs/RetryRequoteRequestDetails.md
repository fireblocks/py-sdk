# RetryRequoteRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates that the order should be re-quoted if the original quote is expired, trying to match the original quote. | 
**count** | **float** | If quote is expired, how many times to re-generate new quotes to try having the order executed as in the original quote. | 
**slippage_bps** | **float** | Slippage tolerance in basis points (bps) for quote orders - 1 is 0.01% and 10000 is 100% | [optional] [default to 1]

## Example

```python
from fireblocks.models.retry_requote_request_details import RetryRequoteRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RetryRequoteRequestDetails from a JSON string
retry_requote_request_details_instance = RetryRequoteRequestDetails.from_json(json)
# print the JSON string representation of the object
print(RetryRequoteRequestDetails.to_json())

# convert the object into a dict
retry_requote_request_details_dict = retry_requote_request_details_instance.to_dict()
# create an instance of RetryRequoteRequestDetails from a dict
retry_requote_request_details_from_dict = RetryRequoteRequestDetails.from_dict(retry_requote_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


