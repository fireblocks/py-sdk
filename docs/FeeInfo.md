# FeeInfo

Details of the transaction's fee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_fee** | **str** | The fee paid to the network | [optional] 
**service_fee** | **str** | The total fee deducted by the exchange from the actual requested amount (serviceFee &#x3D; amount - netAmount) | [optional] 
**gas_price** | **str** |  | [optional] 
**l1network_fee** | **str** | Layer 1 network fee for Layer 2 blockchain transactions | [optional] 
**l2network_fee** | **str** | Layer 2 network fee (gas price component for Layer 2 transactions) | [optional] 
**paid_by_relay** | **bool** | Wether the fee was paid by the relay or not | [optional] 
**relay_type** | **str** | Wether the relay is the same tenant (LOCAL) or another tenant (THIRD_PARTY) | [optional] 
**relay_id** | **str** | The vault account ID of the relay | [optional] 
**relay_name** | **str** | The name of the tenant, only for THIRD_PARTY relays | [optional] 
**fee_usd** | **str** | The USD value of the fee | [optional] 

## Example

```python
from fireblocks.models.fee_info import FeeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FeeInfo from a JSON string
fee_info_instance = FeeInfo.from_json(json)
# print the JSON string representation of the object
print(FeeInfo.to_json())

# convert the object into a dict
fee_info_dict = fee_info_instance.to_dict()
# create an instance of FeeInfo from a dict
fee_info_from_dict = FeeInfo.from_dict(fee_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


