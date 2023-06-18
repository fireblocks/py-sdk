# ToCollateralTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**src_address** | **str** |  | [optional] 
**src_tag** | **str** | optional | [optional] 
**fee** | **str** | optional | [optional] 

## Example

```python
from fireblocks_client.models.to_collateral_transaction import ToCollateralTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ToCollateralTransaction from a JSON string
to_collateral_transaction_instance = ToCollateralTransaction.from_json(json)
# print the JSON string representation of the object
print ToCollateralTransaction.to_json()

# convert the object into a dict
to_collateral_transaction_dict = to_collateral_transaction_instance.to_dict()
# create an instance of ToCollateralTransaction from a dict
to_collateral_transaction_form_dict = to_collateral_transaction.from_dict(to_collateral_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


