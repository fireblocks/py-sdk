# OrderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**via** | [**AccessType**](AccessType.md) |  | 
**status** | [**OrderStatus**](OrderStatus.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**receipt** | [**TransferReceipt**](TransferReceipt.md) |  | [optional] 
**general_fees** | [**List[Fee]**](Fee.md) |  | [optional] 
**execution_steps** | [**List[ExecutionStep]**](ExecutionStep.md) |  | 
**execution_response_details** | [**ExecutionResponseDetails**](ExecutionResponseDetails.md) |  | 
**settlement** | [**Settlement**](Settlement.md) |  | 
**participants_identification** | [**ParticipantsIdentification**](ParticipantsIdentification.md) |  | [optional] 
**payment_instructions** | [**List[PaymentInstructions]**](PaymentInstructions.md) | Payment instructions for the order, the client can use one of these to pay the order. | [optional] 
**created_by** | **str** | The ID of the user who created the order | 
**customer_internal_reference_id** | **str** | Internal reference ID for the customer | [optional] 
**note** | **str** | Optional note for the Order | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from fireblocks.models.order_details import OrderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetails from a JSON string
order_details_instance = OrderDetails.from_json(json)
# print the JSON string representation of the object
print(OrderDetails.to_json())

# convert the object into a dict
order_details_dict = order_details_instance.to_dict()
# create an instance of OrderDetails from a dict
order_details_from_dict = OrderDetails.from_dict(order_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


