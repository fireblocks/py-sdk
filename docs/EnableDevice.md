# EnableDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the device should be enabled or disabled | 

## Example

```python
from fireblocks.models.enable_device import EnableDevice

# TODO update the JSON string below
json = "{}"
# create an instance of EnableDevice from a JSON string
enable_device_instance = EnableDevice.from_json(json)
# print the JSON string representation of the object
print(EnableDevice.to_json())

# convert the object into a dict
enable_device_dict = enable_device_instance.to_dict()
# create an instance of EnableDevice from a dict
enable_device_from_dict = EnableDevice.from_dict(enable_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


