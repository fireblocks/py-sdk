# AddressBalanceItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_address** | **str** | The account address | 
**balance** | **str** | The current balance of the account | 
**last_updated** | **datetime** | The timestamp when this balance was last updated | 

## Example

```python
from fireblocks.models.address_balance_item_dto import AddressBalanceItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddressBalanceItemDto from a JSON string
address_balance_item_dto_instance = AddressBalanceItemDto.from_json(json)
# print the JSON string representation of the object
print(AddressBalanceItemDto.to_json())

# convert the object into a dict
address_balance_item_dto_dict = address_balance_item_dto_instance.to_dict()
# create an instance of AddressBalanceItemDto from a dict
address_balance_item_dto_from_dict = AddressBalanceItemDto.from_dict(address_balance_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


