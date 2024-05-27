# PayeeAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**PayeeAccountType**](PayeeAccountType.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.payee_account_response import PayeeAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeAccountResponse from a JSON string
payee_account_response_instance = PayeeAccountResponse.from_json(json)
# print the JSON string representation of the object
print PayeeAccountResponse.to_json()

# convert the object into a dict
payee_account_response_dict = payee_account_response_instance.to_dict()
# create an instance of PayeeAccountResponse from a dict
payee_account_response_form_dict = payee_account_response.from_dict(payee_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


