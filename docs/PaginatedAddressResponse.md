# PaginatedAddressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[VaultWalletAddress]**](VaultWalletAddress.md) |  | [optional] 
**paging** | [**PaginatedAddressResponsePaging**](PaginatedAddressResponsePaging.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.paginated_address_response import PaginatedAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAddressResponse from a JSON string
paginated_address_response_instance = PaginatedAddressResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedAddressResponse.to_json())

# convert the object into a dict
paginated_address_response_dict = paginated_address_response_instance.to_dict()
# create an instance of PaginatedAddressResponse from a dict
paginated_address_response_from_dict = PaginatedAddressResponse.from_dict(paginated_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


