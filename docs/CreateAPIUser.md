# CreateAPIUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Users role | 
**name** | **str** | Users name | 
**csr_pem** | **str** | CSR file that is used to verify API requests. read more https://developers.fireblocks.com/docs/quickstart | 
**co_signer_setup_type** | **str** | Different environments allow for different setup options, field is required for management/signer role | [optional] 
**co_signer_setup_is_first_user** | **bool** | pass as true if this is the first user on the coSigner machine | [optional] 

## Example

```python
from fireblocks.models.create_api_user import CreateAPIUser

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPIUser from a JSON string
create_api_user_instance = CreateAPIUser.from_json(json)
# print the JSON string representation of the object
print(CreateAPIUser.to_json())

# convert the object into a dict
create_api_user_dict = create_api_user_instance.to_dict()
# create an instance of CreateAPIUser from a dict
create_api_user_from_dict = CreateAPIUser.from_dict(create_api_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


