# InteracPaymentInfo

Interac e-Transfer payment information for Canadian dollar transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for Interac transfers | 
**addressing_system** | **str** | The addressing system used for Interac transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**country** | **str** | The country for the transfer (ISO 3166-1 alpha-2 code) | 
**recipient_handle_type** | **str** | The type of recipient handler being used | 
**recipient_handle_value** | **str** | Email address registered for Interac e-Transfer | 
**message** | **str** | The message to be sent to the recipient | 

## Example

```python
from fireblocks.models.interac_payment_info import InteracPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InteracPaymentInfo from a JSON string
interac_payment_info_instance = InteracPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(InteracPaymentInfo.to_json())

# convert the object into a dict
interac_payment_info_dict = interac_payment_info_instance.to_dict()
# create an instance of InteracPaymentInfo from a dict
interac_payment_info_from_dict = InteracPaymentInfo.from_dict(interac_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


