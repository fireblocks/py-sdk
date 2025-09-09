# CreateQuoteScopeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The ID of the provider associated with the account. | 
**account_id** | **str** | The ID of the account associated with the provider. | 

## Example

```python
from fireblocks.models.create_quote_scope_inner import CreateQuoteScopeInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuoteScopeInner from a JSON string
create_quote_scope_inner_instance = CreateQuoteScopeInner.from_json(json)
# print the JSON string representation of the object
print(CreateQuoteScopeInner.to_json())

# convert the object into a dict
create_quote_scope_inner_dict = create_quote_scope_inner_instance.to_dict()
# create an instance of CreateQuoteScopeInner from a dict
create_quote_scope_inner_from_dict = CreateQuoteScopeInner.from_dict(create_quote_scope_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


