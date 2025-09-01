# UsWirePaymentInfo

US Wire payment information for US domestic wire transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for US wire transfers | 
**addressing_system** | **str** | The addressing system used for US wire transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**country** | **str** | The country for the transfer (ISO 3166-1 alpha-2 code) | 
**account_number** | **str** | The bank account number | 
**routing_number** | **str** | The bank routing number (ABA routing number) | 
**swift_code** | **str** | The SWIFT/BIC code of the bank | 
**bank_name** | **str** | The name of the bank | 
**bank_address_line** | **str** | The street address of the bank | 
**bank_address_city** | **str** | The city where the bank is located | 
**bank_address_state** | **str** | The state where the bank is located | [optional] 
**bank_address_country** | **str** | The country where the bank is located (ISO 3166-1 alpha-2 code) | 
**bank_address_postal_code** | **str** | The postal code of the bank&#39;s address | 
**branch_number** | **str** | The branch number of the bank | [optional] 

## Example

```python
from fireblocks.models.us_wire_payment_info import UsWirePaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UsWirePaymentInfo from a JSON string
us_wire_payment_info_instance = UsWirePaymentInfo.from_json(json)
# print the JSON string representation of the object
print(UsWirePaymentInfo.to_json())

# convert the object into a dict
us_wire_payment_info_dict = us_wire_payment_info_instance.to_dict()
# create an instance of UsWirePaymentInfo from a dict
us_wire_payment_info_from_dict = UsWirePaymentInfo.from_dict(us_wire_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


