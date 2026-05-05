# TRLinkResolveActionData

Data to submit when resolving an action. The structure varies by action type and is validated by the TRP provider.  For UPLOAD_BENEFICIARY_PII action type: Contains beneficiaryPii with IVMS101-encoded PII data. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beneficiary_pii** | [**TRLinkBeneficiaryPii**](TRLinkBeneficiaryPii.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_resolve_action_data import TRLinkResolveActionData

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkResolveActionData from a JSON string
tr_link_resolve_action_data_instance = TRLinkResolveActionData.from_json(json)
# print the JSON string representation of the object
print(TRLinkResolveActionData.to_json())

# convert the object into a dict
tr_link_resolve_action_data_dict = tr_link_resolve_action_data_instance.to_dict()
# create an instance of TRLinkResolveActionData from a dict
tr_link_resolve_action_data_from_dict = TRLinkResolveActionData.from_dict(tr_link_resolve_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


