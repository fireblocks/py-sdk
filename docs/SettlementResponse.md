# SettlementResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**initiator** | **str** |  | [optional] 
**exchange_reply** | **str** |  | [optional] 
**fireblocks_initiated_transactions** | **object** |  | [optional] 
**exchange_requested_transactions** | [**ExchangeSettlementTransactionsResponse**](ExchangeSettlementTransactionsResponse.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.settlement_response import SettlementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementResponse from a JSON string
settlement_response_instance = SettlementResponse.from_json(json)
# print the JSON string representation of the object
print SettlementResponse.to_json()

# convert the object into a dict
settlement_response_dict = settlement_response_instance.to_dict()
# create an instance of SettlementResponse from a dict
settlement_response_form_dict = settlement_response.from_dict(settlement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


