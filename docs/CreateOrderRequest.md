# CreateOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**via** | [**AccessType**](AccessType.md) |  | 
**execution_request_details** | [**ExecutionRequestDetails**](ExecutionRequestDetails.md) |  | 
**settlement** | [**Settlement**](Settlement.md) |  | 
**participants_identification** | [**ParticipantsIdentification**](ParticipantsIdentification.md) |  | [optional] 
**customer_internal_reference_id** | **str** | Internal reference ID for the customer | [optional] 
**note** | **str** | Optional note for the order | [optional] 

## Example

```python
from fireblocks.models.create_order_request import CreateOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderRequest from a JSON string
create_order_request_instance = CreateOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrderRequest.to_json())

# convert the object into a dict
create_order_request_dict = create_order_request_instance.to_dict()
# create an instance of CreateOrderRequest from a dict
create_order_request_from_dict = CreateOrderRequest.from_dict(create_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


