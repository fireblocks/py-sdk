# CreateCounterpartyGroupRequest

Request body for creating a new counterparty group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name of the group | 
**jurisdiction_codes** | **List[str]** | List of jurisdiction codes to associate with the group | 
**description** | **str** | Optional description of the group | [optional] 

## Example

```python
from fireblocks.models.create_counterparty_group_request import CreateCounterpartyGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCounterpartyGroupRequest from a JSON string
create_counterparty_group_request_instance = CreateCounterpartyGroupRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCounterpartyGroupRequest.to_json())

# convert the object into a dict
create_counterparty_group_request_dict = create_counterparty_group_request_instance.to_dict()
# create an instance of CreateCounterpartyGroupRequest from a dict
create_counterparty_group_request_from_dict = CreateCounterpartyGroupRequest.from_dict(create_counterparty_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


