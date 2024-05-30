# ThirdPartyRouting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_third_party_routing** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.third_party_routing import ThirdPartyRouting

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyRouting from a JSON string
third_party_routing_instance = ThirdPartyRouting.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyRouting.to_json())

# convert the object into a dict
third_party_routing_dict = third_party_routing_instance.to_dict()
# create an instance of ThirdPartyRouting from a dict
third_party_routing_from_dict = ThirdPartyRouting.from_dict(third_party_routing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


