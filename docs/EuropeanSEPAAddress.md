# EuropeanSEPAAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**iban** | **str** |  | 
**bic** | **str** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**bank_branch** | **str** |  | [optional] 
**bank_address** | **str** |  | [optional] 
**purpose_code** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.european_sepa_address import EuropeanSEPAAddress

# TODO update the JSON string below
json = "{}"
# create an instance of EuropeanSEPAAddress from a JSON string
european_sepa_address_instance = EuropeanSEPAAddress.from_json(json)
# print the JSON string representation of the object
print(EuropeanSEPAAddress.to_json())

# convert the object into a dict
european_sepa_address_dict = european_sepa_address_instance.to_dict()
# create an instance of EuropeanSEPAAddress from a dict
european_sepa_address_from_dict = EuropeanSEPAAddress.from_dict(european_sepa_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


