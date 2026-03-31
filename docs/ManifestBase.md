# ManifestBase

Base manifest schema with common properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | Indicates whether the endpoint is supported by the provider | 

## Example

```python
from fireblocks.models.manifest_base import ManifestBase

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestBase from a JSON string
manifest_base_instance = ManifestBase.from_json(json)
# print the JSON string representation of the object
print(ManifestBase.to_json())

# convert the object into a dict
manifest_base_dict = manifest_base_instance.to_dict()
# create an instance of ManifestBase from a dict
manifest_base_from_dict = ManifestBase.from_dict(manifest_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


