# AddressesFilters

Filter options for the `addresses` report type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_ids** | **List[str]** | Restrict to the listed vault account IDs. Max 1000 items. Pass a single ID as a one-element array. | [optional] 
**assets** | **List[str]** | Filter by asset symbol (e.g., BTC, ETH). Max 1000 items. Pass a single symbol as a one-element array. | [optional] 

## Example

```python
from fireblocks.models.addresses_filters import AddressesFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AddressesFilters from a JSON string
addresses_filters_instance = AddressesFilters.from_json(json)
# print the JSON string representation of the object
print(AddressesFilters.to_json())

# convert the object into a dict
addresses_filters_dict = addresses_filters_instance.to_dict()
# create an instance of AddressesFilters from a dict
addresses_filters_from_dict = AddressesFilters.from_dict(addresses_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


