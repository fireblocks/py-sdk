# AuditorData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**image_url** | **str** |  | 
**link** | **str** |  | 

## Example

```python
from fireblocks_client.models.auditor_data import AuditorData

# TODO update the JSON string below
json = "{}"
# create an instance of AuditorData from a JSON string
auditor_data_instance = AuditorData.from_json(json)
# print the JSON string representation of the object
print(AuditorData.to_json())

# convert the object into a dict
auditor_data_dict = auditor_data_instance.to_dict()
# create an instance of AuditorData from a dict
auditor_data_from_dict = AuditorData.from_dict(auditor_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


