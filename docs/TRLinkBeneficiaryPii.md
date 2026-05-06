# TRLinkBeneficiaryPii

Beneficiary PII data in IVMS101 format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ivms101** | [**TRLinkIvms**](TRLinkIvms.md) |  | 

## Example

```python
from fireblocks.models.tr_link_beneficiary_pii import TRLinkBeneficiaryPii

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkBeneficiaryPii from a JSON string
tr_link_beneficiary_pii_instance = TRLinkBeneficiaryPii.from_json(json)
# print the JSON string representation of the object
print(TRLinkBeneficiaryPii.to_json())

# convert the object into a dict
tr_link_beneficiary_pii_dict = tr_link_beneficiary_pii_instance.to_dict()
# create an instance of TRLinkBeneficiaryPii from a dict
tr_link_beneficiary_pii_from_dict = TRLinkBeneficiaryPii.from_dict(tr_link_beneficiary_pii_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


