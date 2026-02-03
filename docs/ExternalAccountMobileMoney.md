# ExternalAccountMobileMoney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExternalAccountMobileMoneyType**](ExternalAccountMobileMoneyType.md) |  | 
**mobile_phone_number** | **str** | Mobile phone number in E.164 format | 
**provider** | [**ExternalAccountMobileMoneyProvider**](ExternalAccountMobileMoneyProvider.md) |  | 
**email** | **str** |  | 

## Example

```python
from fireblocks.models.external_account_mobile_money import ExternalAccountMobileMoney

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAccountMobileMoney from a JSON string
external_account_mobile_money_instance = ExternalAccountMobileMoney.from_json(json)
# print the JSON string representation of the object
print(ExternalAccountMobileMoney.to_json())

# convert the object into a dict
external_account_mobile_money_dict = external_account_mobile_money_instance.to_dict()
# create an instance of ExternalAccountMobileMoney from a dict
external_account_mobile_money_from_dict = ExternalAccountMobileMoney.from_dict(external_account_mobile_money_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


