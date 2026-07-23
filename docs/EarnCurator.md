# EarnCurator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Curator display name. | [optional] 
**icon_url** | **str** | URL of the curator&#39;s icon/logo. | [optional] 

## Example

```python
from fireblocks.models.earn_curator import EarnCurator

# TODO update the JSON string below
json = "{}"
# create an instance of EarnCurator from a JSON string
earn_curator_instance = EarnCurator.from_json(json)
# print the JSON string representation of the object
print(EarnCurator.to_json())

# convert the object into a dict
earn_curator_dict = earn_curator_instance.to_dict()
# create an instance of EarnCurator from a dict
earn_curator_from_dict = EarnCurator.from_dict(earn_curator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


