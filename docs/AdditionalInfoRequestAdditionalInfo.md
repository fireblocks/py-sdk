# AdditionalInfoRequestAdditionalInfo

Additional payment information based on the payment rail type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**account_holder_city** | **str** | The city where the account holder resides | 
**account_holder_country** | **str** | The country where the account holder resides (ISO 3166-1 alpha-2 code) | 
**account_holder_address1** | **str** | The primary address line of the account holder | 
**account_holder_address2** | **str** | The secondary address line of the account holder (optional) | [optional] 
**account_holder_district** | **str** | The district or region where the account holder resides | [optional] 
**account_holder_postal_code** | **str** | The postal code of the account holder&#39;s address | 
**iban** | **str** | The International Bank Account Number (IBAN) | 
**iban_city** | **str** | The city associated with the IBAN | 
**iban_country** | **str** | The country associated with the IBAN (ISO 3166-1 alpha-2 code) | 
**aba_routing_number** | **str** | The ABA routing number for the bank | 
**aba_account_number** | **str** | The account number at the bank | 
**aba_country** | **str** | The country for the ABA transfer (ISO 3166-1 alpha-2 code) | 
**spei_clabe** | **str** | The CLABE (Clave Bancaria Estandarizada) number for SPEI transfers | 
**spei_name** | **str** | The name associated with the SPEI account | [optional] 
**rail** | **str** | The payment rail type for Lebanese bank transfers | 
**addressing_system** | **str** | The addressing system used for Lebanese bank transfers (Bank Account Number) | 
**country** | **str** | The country for the transfer (ISO 3166-1 alpha-2 code) | 
**bank_name** | **str** | The name of the bank | 
**beneficiary_rfc** | **str** | The RFC (Registro Federal de Contribuyentes) of the beneficiary | [optional] 
**sender_document_id** | **str** | The document ID of the sender | [optional] 
**clabe** | **str** | The CLABE (Clave Bancaria Estandarizada) number | 
**pix_key** | **str** | The PIX key used for the transfer | 
**bank_code** | **str** | The bank code or identifier | 
**key_type** | **str** | The type of PIX key being used | 
**account_holder_address** | **str** | The address of the account holder | [optional] 
**bic** | **str** | The Bank Identifier Code (BIC/SWIFT code) | [optional] 
**bank_branch** | **str** | The bank branch information | [optional] 
**bank_address** | **str** | The address of the bank | [optional] 
**purpose_code** | **str** | The purpose code for the transfer | [optional] 
**tax_id** | **str** | The tax identification number | [optional] 
**account_number** | **str** | The bank account number | 
**routing_number** | **str** | The bank routing number (ABA routing number) | 
**account_type** | **str** | The type of bank account | 
**swift_code** | **str** | The SWIFT/BIC code of the bank | 
**bank_address_line** | **str** | The street address of the bank | 
**bank_address_city** | **str** | The city where the bank is located | 
**bank_address_state** | **str** | The state where the bank is located | [optional] 
**bank_address_country** | **str** | The country where the bank is located (ISO 3166-1 alpha-2 code) | 
**bank_address_postal_code** | **str** | The postal code of the bank&#39;s address | 
**branch_number** | **str** | The branch number of the bank | [optional] 
**mobile_phone_number** | **str** | The mobile phone number associated with the mobile money account | 
**provider** | **str** | The mobile money service provider | 
**beneficiary_document_id** | **str** | The document ID of the beneficiary | [optional] 
**beneficiary_relationship** | **str** | The relationship between sender and beneficiary | [optional] 

## Example

```python
from fireblocks.models.additional_info_request_additional_info import AdditionalInfoRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalInfoRequestAdditionalInfo from a JSON string
additional_info_request_additional_info_instance = AdditionalInfoRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(AdditionalInfoRequestAdditionalInfo.to_json())

# convert the object into a dict
additional_info_request_additional_info_dict = additional_info_request_additional_info_instance.to_dict()
# create an instance of AdditionalInfoRequestAdditionalInfo from a dict
additional_info_request_additional_info_from_dict = AdditionalInfoRequestAdditionalInfo.from_dict(additional_info_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


