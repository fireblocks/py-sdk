# SEPAAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**iban** | **str** |  | 
**bic** | **str** | Bank Identifier Code (SWIFT/BIC) | [optional] 
**bank_name** | **str** |  | [optional] 
**bank_branch** | **str** |  | [optional] 
**bank_address** | **str** |  | [optional] 
**purpose_code** | **str** | ISO purpose code for the transfer | [optional] 
**tax_id** | **str** | Beneficiary tax identification number | [optional] 

## Example

```python
from fireblocks.models.sepa_address import SEPAAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SEPAAddress from a JSON string
sepa_address_instance = SEPAAddress.from_json(json)
# print the JSON string representation of the object
print(SEPAAddress.to_json())

# convert the object into a dict
sepa_address_dict = sepa_address_instance.to_dict()
# create an instance of SEPAAddress from a dict
sepa_address_from_dict = SEPAAddress.from_dict(sepa_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


