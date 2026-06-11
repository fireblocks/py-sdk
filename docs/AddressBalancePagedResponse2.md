# AddressBalancePagedResponse2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AddressBalanceItemDto]**](AddressBalanceItemDto.md) | Array of address balance data | 
**next** | **str** | Cursor for next page | [optional] 
**prev** | **str** | Cursor for previous page (reserved for future support) | [optional] 
**total** | **float** | Total count of items | [optional] 

## Example

```python
from fireblocks.models.address_balance_paged_response2 import AddressBalancePagedResponse2

# TODO update the JSON string below
json = "{}"
# create an instance of AddressBalancePagedResponse2 from a JSON string
address_balance_paged_response2_instance = AddressBalancePagedResponse2.from_json(json)
# print the JSON string representation of the object
print(AddressBalancePagedResponse2.to_json())

# convert the object into a dict
address_balance_paged_response2_dict = address_balance_paged_response2_instance.to_dict()
# create an instance of AddressBalancePagedResponse2 from a dict
address_balance_paged_response2_from_dict = AddressBalancePagedResponse2.from_dict(address_balance_paged_response2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


