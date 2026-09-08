# EndInvestorPayload

Shared by invite / invite-cancel / offboard — identical wire shape, different verb.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The vault account whose Canton wallet acts here. | 
**asset** | **str** | Chain asset — &#x60;CANTON&#x60; or &#x60;CANTON_TEST&#x60;. | 
**end_investor** | **str** | The end investor&#39;s Canton party id. | 

## Example

```python
from fireblocks.models.end_investor_payload import EndInvestorPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EndInvestorPayload from a JSON string
end_investor_payload_instance = EndInvestorPayload.from_json(json)
# print the JSON string representation of the object
print(EndInvestorPayload.to_json())

# convert the object into a dict
end_investor_payload_dict = end_investor_payload_instance.to_dict()
# create an instance of EndInvestorPayload from a dict
end_investor_payload_from_dict = EndInvestorPayload.from_dict(end_investor_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


