# MobileMoneyAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**mobile_phone_number** | **str** | Mobile phone number in E.164 format | 
**provider** | **str** | Mobile money provider | 
**beneficiary_document_id** | **str** | Beneficiary document identification (may be required) | [optional] 
**beneficiary_relationship** | **str** | Relationship to beneficiary for AML purposes | [optional] 
**success_payment_instruction_redirect_url** | **str** | The URL to redirect to after the payment instruction is successful | [optional] 
**payment_redirect** | [**PaymentRedirect**](PaymentRedirect.md) |  | [optional] 

## Example

```python
from fireblocks.models.mobile_money_address import MobileMoneyAddress

# TODO update the JSON string below
json = "{}"
# create an instance of MobileMoneyAddress from a JSON string
mobile_money_address_instance = MobileMoneyAddress.from_json(json)
# print the JSON string representation of the object
print(MobileMoneyAddress.to_json())

# convert the object into a dict
mobile_money_address_dict = mobile_money_address_instance.to_dict()
# create an instance of MobileMoneyAddress from a dict
mobile_money_address_from_dict = MobileMoneyAddress.from_dict(mobile_money_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


