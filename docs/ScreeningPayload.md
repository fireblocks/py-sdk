# ScreeningPayload

The subject of the screening. Which fields are required depends on the operation and on the connectors configured on the workflow's step.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | The blockchain network of the asset being screened. | [optional] 
**asset** | **str** | The asset identifier being screened. | [optional] 
**asset_amount** | **str** | The amount of the asset involved in the transaction, as a string. | [optional] 
**usd_value** | **str** | The USD value of the transaction amount, as a string. | [optional] 
**customer_ref_id** | **str** | Customer-provided reference identifier for tracking. | [optional] 
**external_id** | **str** | External identifier for the screening (provider-specific). | [optional] 
**address** | **str** | The blockchain address to screen. Used for the &#x60;ADDRESS_SCREENING&#x60; operation. | [optional] 
**direction** | [**TransferDirectionEnum**](TransferDirectionEnum.md) |  | [optional] 
**source_address** | **List[str]** | The source blockchain address(es) of the transaction. | [optional] 
**destination_address** | **List[str]** | The destination blockchain address(es) of the transaction. | [optional] 
**tx_hash** | **str** | The transaction hash on the blockchain. | [optional] 

## Example

```python
from fireblocks.models.screening_payload import ScreeningPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningPayload from a JSON string
screening_payload_instance = ScreeningPayload.from_json(json)
# print the JSON string representation of the object
print(ScreeningPayload.to_json())

# convert the object into a dict
screening_payload_dict = screening_payload_instance.to_dict()
# create an instance of ScreeningPayload from a dict
screening_payload_from_dict = ScreeningPayload.from_dict(screening_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


