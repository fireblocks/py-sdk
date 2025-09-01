# AccountIdentifier

Account identifier with type, ID, subtype, and address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AccountType2**](AccountType2.md) |  | 
**id** | **str** | Account ID | [optional] 
**sub_type** | **str** | Account subtype | [optional] 
**address** | **str** | Account address | [optional] 

## Example

```python
from fireblocks.models.account_identifier import AccountIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AccountIdentifier from a JSON string
account_identifier_instance = AccountIdentifier.from_json(json)
# print the JSON string representation of the object
print(AccountIdentifier.to_json())

# convert the object into a dict
account_identifier_dict = account_identifier_instance.to_dict()
# create an instance of AccountIdentifier from a dict
account_identifier_from_dict = AccountIdentifier.from_dict(account_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


