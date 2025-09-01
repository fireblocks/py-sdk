# ScreeningMetadataConfig

Screening metadata configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | Direction of transaction | 
**provider** | **str** | Screening provider | [optional] 
**risk_rating** | **str** | Risk rating threshold | [optional] 
**risk_score** | **str** | Risk score threshold | [optional] 
**exposure_type** | **str** | Exposure type | [optional] 
**category** | **List[str]** |  | [optional] 
**name** | **List[str]** |  | [optional] 
**category_id** | **List[str]** |  | [optional] 
**status** | **str** | Transaction status | [optional] 
**source_address** | **str** | Source address | [optional] 
**dest_address** | **str** | Destination address | [optional] 

## Example

```python
from fireblocks.models.screening_metadata_config import ScreeningMetadataConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningMetadataConfig from a JSON string
screening_metadata_config_instance = ScreeningMetadataConfig.from_json(json)
# print the JSON string representation of the object
print(ScreeningMetadataConfig.to_json())

# convert the object into a dict
screening_metadata_config_dict = screening_metadata_config_instance.to_dict()
# create an instance of ScreeningMetadataConfig from a dict
screening_metadata_config_from_dict = ScreeningMetadataConfig.from_dict(screening_metadata_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


