# OrderRequirementDetails

Order requirement details for an order that is awaiting compliance requirements. Returned by GET /trading/orders/{orderId}/requirement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requirement_id** | **str** | Unique identifier of the order requirement request as issued by the provider. | 
**due_by** | **datetime** | ISO-8601 timestamp indicating when the order requirement submission is due. | [optional] 
**required_data** | **str** | A JSON Schema (Draft-7) in string format describing the shape of the &#x60;data&#x60; object expected on the corresponding POST /trading/orders/{orderId}/requirement/data request. The schema is the contract: the client builds the &#x60;data&#x60; payload to match it, and SDKs can validate before sending. The string content is expected to be valid JSON (application/json).  | 
**required_files** | [**List[OrderRequirementFile]**](OrderRequirementFile.md) | Descriptors for files the provider requires as part of the order requirement response. Empty when no files are required. Each entry&#39;s &#x60;fileKey&#x60; is used to correlate uploads on the corresponding upload request. | 

## Example

```python
from fireblocks.models.order_requirement_details import OrderRequirementDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRequirementDetails from a JSON string
order_requirement_details_instance = OrderRequirementDetails.from_json(json)
# print the JSON string representation of the object
print(OrderRequirementDetails.to_json())

# convert the object into a dict
order_requirement_details_dict = order_requirement_details_instance.to_dict()
# create an instance of OrderRequirementDetails from a dict
order_requirement_details_from_dict = OrderRequirementDetails.from_dict(order_requirement_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


