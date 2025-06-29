# SwapOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the swap operation | 
**account_id** | **str** | The id of the vault account or account id | 
**provider_id** | **str** | The ID of the provider | 
**category** | [**ProviderCategoryEnum**](ProviderCategoryEnum.md) |  | 
**protocol** | [**SwapProviderProtocolsEnum**](SwapProviderProtocolsEnum.md) |  | 
**status** | **str** | **CREATED** – The swap request has been created but not yet started. **PENDING_USER_ACTION** – Awaiting a user action (e.g. signature or approval). **PENDING_PROVIDER_ACTION** – Awaiting the provider to process the request. **PROCESSING** – The swap is actively being executed on‐chain. **COMPLETED** – The swap has finished successfully. **CANCELED** – The swap was cancelled by user or provider before completion. **FAILED** – The swap attempted but encountered an error. | 
**input_amount** | **str** | The amount of tokens the swapper will provide | 
**input_asset** | **str** | The id of the asset the swapper will provide | 
**slippage_tolerance** | **float** | The slippage tolerance is a percentage. The slippage tolerance is the maximum amount the price can change between the time the transaction is submitted and the time it is executed | 
**output_min_amount** | **str** | The minimum amount of tokens the swapper will receive | 
**output_max_amount** | **str** | Maximum amount of tokens that the swapper will receive | 
**output_asset** | **str** | The id of the asset the swapper will receive | 
**output_final_amount** | **str** | Final amount of tokens that the swapper will receive | [optional] 
**required_actions** | [**List[SwapRequiredAction]**](SwapRequiredAction.md) | The required actions for the swap, including the type of action, the status of the action, and the transaction id | 
**error** | [**SwapFlowError**](SwapFlowError.md) |  | [optional] 
**created_at** | **datetime** | The creation time of the swap operation (ISO Date time). | 
**updated_at** | **datetime** | The last update time of the swap operation (ISO Date time). | 
**created_by** | **str** | Fireblocks user id that issued the swap | 

## Example

```python
from fireblocks.models.swap_operation import SwapOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SwapOperation from a JSON string
swap_operation_instance = SwapOperation.from_json(json)
# print the JSON string representation of the object
print(SwapOperation.to_json())

# convert the object into a dict
swap_operation_dict = swap_operation_instance.to_dict()
# create an instance of SwapOperation from a dict
swap_operation_from_dict = SwapOperation.from_dict(swap_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


