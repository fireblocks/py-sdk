# GetByorkVerdictResponse

Response for GET BYORK verdict (current verdict/status for a transaction).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ByorkVerdictResponseStatusEnum**](ByorkVerdictResponseStatusEnum.md) |  | 
**verdict** | [**ByorkVerdictEnum**](ByorkVerdictEnum.md) |  | 

## Example

```python
from fireblocks.models.get_byork_verdict_response import GetByorkVerdictResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetByorkVerdictResponse from a JSON string
get_byork_verdict_response_instance = GetByorkVerdictResponse.from_json(json)
# print the JSON string representation of the object
print(GetByorkVerdictResponse.to_json())

# convert the object into a dict
get_byork_verdict_response_dict = get_byork_verdict_response_instance.to_dict()
# create an instance of GetByorkVerdictResponse from a dict
get_byork_verdict_response_from_dict = GetByorkVerdictResponse.from_dict(get_byork_verdict_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


