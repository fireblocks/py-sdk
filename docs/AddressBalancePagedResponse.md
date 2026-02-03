# AddressBalancePagedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AddressBalanceItemDto]**](AddressBalanceItemDto.md) | Array of address balance data | 
**next** | **str** | Cursor for next page | [optional] 
**prev** | **str** | Cursor for previous page (reserved for future support) | [optional] 
**total** | **float** | Total count of items | [optional] 

## Example

```python
from fireblocks.models.address_balance_paged_response import AddressBalancePagedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressBalancePagedResponse from a JSON string
address_balance_paged_response_instance = AddressBalancePagedResponse.from_json(json)
# print the JSON string representation of the object
print(AddressBalancePagedResponse.to_json())

# convert the object into a dict
address_balance_paged_response_dict = address_balance_paged_response_instance.to_dict()
# create an instance of AddressBalancePagedResponse from a dict
address_balance_paged_response_from_dict = AddressBalancePagedResponse.from_dict(address_balance_paged_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


