# PayeeAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | [**PayeeAccountType**](PayeeAccountType.md) |  | 

## Example

```python
from fireblocks.models.payee_account import PayeeAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeAccount from a JSON string
payee_account_instance = PayeeAccount.from_json(json)
# print the JSON string representation of the object
print(PayeeAccount.to_json())

# convert the object into a dict
payee_account_dict = payee_account_instance.to_dict()
# create an instance of PayeeAccount from a dict
payee_account_from_dict = PayeeAccount.from_dict(payee_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


