# GetConnectionsFilterParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**vault_account_id** | **float** |  | [optional] 
**connection_method** | **str** |  | [optional] 
**fee_level** | **str** |  | [optional] 
**app_url** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.get_connections_filter_parameter import GetConnectionsFilterParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetConnectionsFilterParameter from a JSON string
get_connections_filter_parameter_instance = GetConnectionsFilterParameter.from_json(json)
# print the JSON string representation of the object
print GetConnectionsFilterParameter.to_json()

# convert the object into a dict
get_connections_filter_parameter_dict = get_connections_filter_parameter_instance.to_dict()
# create an instance of GetConnectionsFilterParameter from a dict
get_connections_filter_parameter_form_dict = get_connections_filter_parameter.from_dict(get_connections_filter_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


