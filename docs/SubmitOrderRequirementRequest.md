# SubmitOrderRequirementRequest

Body of POST /trading/orders/{orderId}/requirement/data. Carries the textual response (`data`). Any required files are uploaded separately via POST /trading/orders/{orderId}/requirement/file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | Free-form object that MUST conform to the &#x60;requiredData&#x60; JSON Schema returned by the GET endpoint. Carries text/select fields. | 

## Example

```python
from fireblocks.models.submit_order_requirement_request import SubmitOrderRequirementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitOrderRequirementRequest from a JSON string
submit_order_requirement_request_instance = SubmitOrderRequirementRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitOrderRequirementRequest.to_json())

# convert the object into a dict
submit_order_requirement_request_dict = submit_order_requirement_request_instance.to_dict()
# create an instance of SubmitOrderRequirementRequest from a dict
submit_order_requirement_request_from_dict = SubmitOrderRequirementRequest.from_dict(submit_order_requirement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


