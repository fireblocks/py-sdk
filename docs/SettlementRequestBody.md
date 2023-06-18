# SettlementRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main_exchange_account_id** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.settlement_request_body import SettlementRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementRequestBody from a JSON string
settlement_request_body_instance = SettlementRequestBody.from_json(json)
# print the JSON string representation of the object
print SettlementRequestBody.to_json()

# convert the object into a dict
settlement_request_body_dict = settlement_request_body_instance.to_dict()
# create an instance of SettlementRequestBody from a dict
settlement_request_body_form_dict = settlement_request_body.from_dict(settlement_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


