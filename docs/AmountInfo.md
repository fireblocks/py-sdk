# AmountInfo

The details of the requested amount to transfer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | If the transfer is a withdrawal from an exchange, the actual amount that was requested to be transferred. Otherwise, the requested amount. | [optional] 
**requested_amount** | **str** | The amount requested by the user. | [optional] 
**net_amount** | **str** | The net amount of the transaction, after fee deduction. | [optional] 
**amount_usd** | **str** | The USD value of the requested amount. | [optional] 

## Example

```python
from fireblocks_client.models.amount_info import AmountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AmountInfo from a JSON string
amount_info_instance = AmountInfo.from_json(json)
# print the JSON string representation of the object
print AmountInfo.to_json()

# convert the object into a dict
amount_info_dict = amount_info_instance.to_dict()
# create an instance of AmountInfo from a dict
amount_info_form_dict = amount_info.from_dict(amount_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


