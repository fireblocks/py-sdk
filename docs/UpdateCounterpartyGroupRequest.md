# UpdateCounterpartyGroupRequest

Request body for updating an existing counterparty group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated human-readable name of the group | [optional] 
**description** | **str** | Updated description of the group | [optional] 
**jurisdiction_codes** | **List[str]** | Updated list of jurisdiction codes for the group | [optional] 
**is_active** | **bool** | Whether the counterparty group should be active | [optional] 

## Example

```python
from fireblocks.models.update_counterparty_group_request import UpdateCounterpartyGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCounterpartyGroupRequest from a JSON string
update_counterparty_group_request_instance = UpdateCounterpartyGroupRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCounterpartyGroupRequest.to_json())

# convert the object into a dict
update_counterparty_group_request_dict = update_counterparty_group_request_instance.to_dict()
# create an instance of UpdateCounterpartyGroupRequest from a dict
update_counterparty_group_request_from_dict = UpdateCounterpartyGroupRequest.from_dict(update_counterparty_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


