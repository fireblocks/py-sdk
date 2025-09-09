# PlatformAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**account_id** | **str** |  | 

## Example

```python
from fireblocks.models.platform_account import PlatformAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformAccount from a JSON string
platform_account_instance = PlatformAccount.from_json(json)
# print the JSON string representation of the object
print(PlatformAccount.to_json())

# convert the object into a dict
platform_account_dict = platform_account_instance.to_dict()
# create an instance of PlatformAccount from a dict
platform_account_from_dict = PlatformAccount.from_dict(platform_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


