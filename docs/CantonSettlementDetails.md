# CantonSettlementDetails

The credit side of a delivery-versus-payment: a venue settled an allocation. Written once, at creation — the transaction is already complete when it appears.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | The shape of this block. Stamped at creation and never changed, so a reader always knows which version it is holding. | [optional] 
**domain** | [**CantonDomainEnum**](CantonDomainEnum.md) |  | [optional] 
**type** | **str** | The settlement type. | [optional] 
**original_transaction_id** | **str** | The allocation this receipt settles. | [optional] 

## Example

```python
from fireblocks.models.canton_settlement_details import CantonSettlementDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CantonSettlementDetails from a JSON string
canton_settlement_details_instance = CantonSettlementDetails.from_json(json)
# print the JSON string representation of the object
print(CantonSettlementDetails.to_json())

# convert the object into a dict
canton_settlement_details_dict = canton_settlement_details_instance.to_dict()
# create an instance of CantonSettlementDetails from a dict
canton_settlement_details_from_dict = CantonSettlementDetails.from_dict(canton_settlement_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


