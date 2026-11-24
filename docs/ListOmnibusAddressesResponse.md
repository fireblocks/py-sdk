# ListOmnibusAddressesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of addresses matching the request (respecting &#x60;fromIndex&#x60; and &#x60;search&#x60;, ignoring pagination). Returned only on the first page. | [optional] 
**data** | [**List[OmnibusAddress]**](OmnibusAddress.md) | A page of deposit addresses, ordered by index, highest first | 
**next** | **str** | The cursor for the next page. Absent on the last page. | [optional] 

## Example

```python
from fireblocks.models.list_omnibus_addresses_response import ListOmnibusAddressesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOmnibusAddressesResponse from a JSON string
list_omnibus_addresses_response_instance = ListOmnibusAddressesResponse.from_json(json)
# print the JSON string representation of the object
print(ListOmnibusAddressesResponse.to_json())

# convert the object into a dict
list_omnibus_addresses_response_dict = list_omnibus_addresses_response_instance.to_dict()
# create an instance of ListOmnibusAddressesResponse from a dict
list_omnibus_addresses_response_from_dict = ListOmnibusAddressesResponse.from_dict(list_omnibus_addresses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


