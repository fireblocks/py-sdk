# FpsHkPaymentInfo

FPS HK payment information for Hong Kong Faster Payment System transfers (HKD)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for Hong Kong FPS transfers | 
**addressing_system** | **str** | The addressing system used for Hong Kong FPS transfers | 
**recipient_legal_name** | **str** | Full legal name of the recipient | [optional] 
**account_number** | **str** | Recipient bank account number | [optional] 
**bank_code** | **str** | Hong Kong bank code | [optional] 
**phone** | **str** | Recipient phone number in E.164 format | [optional] 
**email** | **str** | Recipient email address | [optional] 
**fps_id** | **str** | Hong Kong FPS identifier | [optional] 

## Example

```python
from fireblocks.models.fps_hk_payment_info import FpsHkPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FpsHkPaymentInfo from a JSON string
fps_hk_payment_info_instance = FpsHkPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(FpsHkPaymentInfo.to_json())

# convert the object into a dict
fps_hk_payment_info_dict = fps_hk_payment_info_instance.to_dict()
# create an instance of FpsHkPaymentInfo from a dict
fps_hk_payment_info_from_dict = FpsHkPaymentInfo.from_dict(fps_hk_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


