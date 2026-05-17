# AddressReverseLookupResponse

Reverse-lookup result mapping a blockchain address to its owning vault account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The queried blockchain address. | 
**type** | **str** | Source type of the resolved address. | 
**vault_account_id** | **str** | Vault account ID that owns the address. | 
**blockchains** | **List[str]** | Blockchain assets associated with this address in the vault account. | 

## Example

```python
from fireblocks.models.address_reverse_lookup_response import AddressReverseLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressReverseLookupResponse from a JSON string
address_reverse_lookup_response_instance = AddressReverseLookupResponse.from_json(json)
# print the JSON string representation of the object
print(AddressReverseLookupResponse.to_json())

# convert the object into a dict
address_reverse_lookup_response_dict = address_reverse_lookup_response_instance.to_dict()
# create an instance of AddressReverseLookupResponse from a dict
address_reverse_lookup_response_from_dict = AddressReverseLookupResponse.from_dict(address_reverse_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


