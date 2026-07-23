# EarnMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Protocol display name (e.g. \&quot;Aave\&quot;, \&quot;Aave Horizon\&quot;). | [optional] 
**icon_url** | **str** | URL of the protocol&#39;s icon/logo. | [optional] 

## Example

```python
from fireblocks.models.earn_metadata import EarnMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of EarnMetadata from a JSON string
earn_metadata_instance = EarnMetadata.from_json(json)
# print the JSON string representation of the object
print(EarnMetadata.to_json())

# convert the object into a dict
earn_metadata_dict = earn_metadata_instance.to_dict()
# create an instance of EarnMetadata from a dict
earn_metadata_from_dict = EarnMetadata.from_dict(earn_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


