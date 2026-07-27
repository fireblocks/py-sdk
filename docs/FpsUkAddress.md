# FpsUkAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**account_number** | **str** | UK bank account number | 
**sort_code** | **str** | UK sort code (format XX-XX-XX) | 

## Example

```python
from fireblocks.models.fps_uk_address import FpsUkAddress

# TODO update the JSON string below
json = "{}"
# create an instance of FpsUkAddress from a JSON string
fps_uk_address_instance = FpsUkAddress.from_json(json)
# print the JSON string representation of the object
print(FpsUkAddress.to_json())

# convert the object into a dict
fps_uk_address_dict = fps_uk_address_instance.to_dict()
# create an instance of FpsUkAddress from a dict
fps_uk_address_from_dict = FpsUkAddress.from_dict(fps_uk_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


