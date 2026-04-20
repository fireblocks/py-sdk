# CreateEarnActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Whether to deposit into or withdraw from the lending opportunity. | 
**opportunity_id** | **str** | Identifier of the vault or market (lending opportunity). | 
**vault_account_id** | **str** | Fireblocks vault account that will execute the action. | 
**amount** | **str** | Human-readable token amount (e.g. \&quot;1.6\&quot;) or the keyword \&quot;max\&quot; for the full position or available balance. | 

## Example

```python
from fireblocks.models.create_earn_action_request import CreateEarnActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEarnActionRequest from a JSON string
create_earn_action_request_instance = CreateEarnActionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEarnActionRequest.to_json())

# convert the object into a dict
create_earn_action_request_dict = create_earn_action_request_instance.to_dict()
# create an instance of CreateEarnActionRequest from a dict
create_earn_action_request_from_dict = CreateEarnActionRequest.from_dict(create_earn_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


