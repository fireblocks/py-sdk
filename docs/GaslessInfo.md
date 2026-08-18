# GaslessInfo

Relay (meta-transaction) details. Returned only for meta-transactions (`isMetaTx` is `true`). For meta-transactions the deprecated top-level `fee` field is omitted; use `feeInfo` instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_meta_tx** | **bool** | Indicates the transaction is a meta-transaction (gas paid by a relay tenant). | [optional] 
**relay_tenant_id** | **str** | The tenant ID of the relay that sponsors the gas for the meta-transaction. | [optional] 
**relay_tenant_name** | **str** | The tenant name of the relay that sponsors the gas for the meta-transaction. | [optional] 
**relay_vault_account_id** | **str** | The vault account ID of the relay that sponsors the gas for the meta-transaction. | [optional] 

## Example

```python
from fireblocks.models.gasless_info import GaslessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GaslessInfo from a JSON string
gasless_info_instance = GaslessInfo.from_json(json)
# print the JSON string representation of the object
print(GaslessInfo.to_json())

# convert the object into a dict
gasless_info_dict = gasless_info_instance.to_dict()
# create an instance of GaslessInfo from a dict
gasless_info_from_dict = GaslessInfo.from_dict(gasless_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


