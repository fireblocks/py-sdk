# TRLinkRequiredActionData

Data describing what fields are required to resolve the action. The structure varies by action type and is defined by the TRP provider.  For UPLOAD_BENEFICIARY_PII action type: Contains beneficiaryRequiredFields and/or originatorRequiredFields listing the IVMS101 field paths that must be provided. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beneficiary_required_fields** | [**List[TRLinkRequiredField]**](TRLinkRequiredField.md) | List of required beneficiary IVMS101 fields | [optional] 
**originator_required_fields** | [**List[TRLinkRequiredField]**](TRLinkRequiredField.md) | List of required originator IVMS101 fields | [optional] 

## Example

```python
from fireblocks.models.tr_link_required_action_data import TRLinkRequiredActionData

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkRequiredActionData from a JSON string
tr_link_required_action_data_instance = TRLinkRequiredActionData.from_json(json)
# print the JSON string representation of the object
print(TRLinkRequiredActionData.to_json())

# convert the object into a dict
tr_link_required_action_data_dict = tr_link_required_action_data_instance.to_dict()
# create an instance of TRLinkRequiredActionData from a dict
tr_link_required_action_data_from_dict = TRLinkRequiredActionData.from_dict(tr_link_required_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


