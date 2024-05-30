# ExchangeSettlementTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_exchange** | [**List[ToExchangeTransaction]**](ToExchangeTransaction.md) |  | [optional] 
**to_collateral** | [**List[ToCollateralTransaction]**](ToCollateralTransaction.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.exchange_settlement_transactions_response import ExchangeSettlementTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeSettlementTransactionsResponse from a JSON string
exchange_settlement_transactions_response_instance = ExchangeSettlementTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(ExchangeSettlementTransactionsResponse.to_json())

# convert the object into a dict
exchange_settlement_transactions_response_dict = exchange_settlement_transactions_response_instance.to_dict()
# create an instance of ExchangeSettlementTransactionsResponse from a dict
exchange_settlement_transactions_response_from_dict = ExchangeSettlementTransactionsResponse.from_dict(exchange_settlement_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


