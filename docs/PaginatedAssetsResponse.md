# PaginatedAssetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | Total number of assets in the internal wallet | [optional] 
**data** | [**UnmanagedWallet**](UnmanagedWallet.md) |  | 
**next** | **str** | Cursor for the next page of results | [optional] 

## Example

```python
from fireblocks.models.paginated_assets_response import PaginatedAssetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAssetsResponse from a JSON string
paginated_assets_response_instance = PaginatedAssetsResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedAssetsResponse.to_json())

# convert the object into a dict
paginated_assets_response_dict = paginated_assets_response_instance.to_dict()
# create an instance of PaginatedAssetsResponse from a dict
paginated_assets_response_from_dict = PaginatedAssetsResponse.from_dict(paginated_assets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


