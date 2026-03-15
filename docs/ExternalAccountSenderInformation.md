# ExternalAccountSenderInformation

Additional data for the external account, depending on the type used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExternalAccountMobileMoneyType**](ExternalAccountMobileMoneyType.md) |  | 
**mobile_phone_number** | **str** | Mobile phone number in E.164 format | 
**provider** | [**ExternalAccountMobileMoneyProvider**](ExternalAccountMobileMoneyProvider.md) |  | 
**email** | **str** |  | 
**success_redirect_url** | **str** | URL to redirect the end user back to after they complete the payment on the bank/mobile provider page (e.g., the merchant checkout page) | [optional] 

## Example

```python
from fireblocks.models.external_account_sender_information import ExternalAccountSenderInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAccountSenderInformation from a JSON string
external_account_sender_information_instance = ExternalAccountSenderInformation.from_json(json)
# print the JSON string representation of the object
print(ExternalAccountSenderInformation.to_json())

# convert the object into a dict
external_account_sender_information_dict = external_account_sender_information_instance.to_dict()
# create an instance of ExternalAccountSenderInformation from a dict
external_account_sender_information_from_dict = ExternalAccountSenderInformation.from_dict(external_account_sender_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


