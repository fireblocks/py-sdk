# AccountHolderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full name of the account holder. | 
**city** | **str** |  | [optional] 
**country** | **str** | Country code, as specified in ISO 3166-1 alpha-2. | [optional] 
**subdivision** | **str** | Country administrative subdivision, as specified in ISO 3166-2. | [optional] 
**address** | **str** | Account holder street address. | [optional] 
**postal_code** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.account_holder_details import AccountHolderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AccountHolderDetails from a JSON string
account_holder_details_instance = AccountHolderDetails.from_json(json)
# print the JSON string representation of the object
print(AccountHolderDetails.to_json())

# convert the object into a dict
account_holder_details_dict = account_holder_details_instance.to_dict()
# create an instance of AccountHolderDetails from a dict
account_holder_details_from_dict = AccountHolderDetails.from_dict(account_holder_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


