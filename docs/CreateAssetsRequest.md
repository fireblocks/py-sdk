# CreateAssetsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eos_account_name** | **str** | Optional - when creating an EOS wallet, the account name. If not provided, a random name will be generated | [optional] 

## Example

```python
from fireblocks_client.models.create_assets_request import CreateAssetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetsRequest from a JSON string
create_assets_request_instance = CreateAssetsRequest.from_json(json)
# print the JSON string representation of the object
print CreateAssetsRequest.to_json()

# convert the object into a dict
create_assets_request_dict = create_assets_request_instance.to_dict()
# create an instance of CreateAssetsRequest from a dict
create_assets_request_form_dict = create_assets_request.from_dict(create_assets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


