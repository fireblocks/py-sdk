# CreateEarnActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ActionIntent UUID for tracking the lending action workflow. | 
**status** | **str** | Lifecycle status (e.g. CREATED, IN_PROGRESS, COMPLETED). | 

## Example

```python
from fireblocks.models.create_earn_action_response import CreateEarnActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEarnActionResponse from a JSON string
create_earn_action_response_instance = CreateEarnActionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateEarnActionResponse.to_json())

# convert the object into a dict
create_earn_action_response_dict = create_earn_action_response_instance.to_dict()
# create an instance of CreateEarnActionResponse from a dict
create_earn_action_response_from_dict = CreateEarnActionResponse.from_dict(create_earn_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


