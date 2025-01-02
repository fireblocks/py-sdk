# Players


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the player | 
**type** | **str** | Type of the player | 

## Example

```python
from fireblocks.models.players import Players

# TODO update the JSON string below
json = "{}"
# create an instance of Players from a JSON string
players_instance = Players.from_json(json)
# print the JSON string representation of the object
print(Players.to_json())

# convert the object into a dict
players_dict = players_instance.to_dict()
# create an instance of Players from a dict
players_from_dict = Players.from_dict(players_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


