# PaymentAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | [**PaymentAccountType**](PaymentAccountType.md) |  | 

## Example

```python
from fireblocks_client.models.payment_account import PaymentAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAccount from a JSON string
payment_account_instance = PaymentAccount.from_json(json)
# print the JSON string representation of the object
print PaymentAccount.to_json()

# convert the object into a dict
payment_account_dict = payment_account_instance.to_dict()
# create an instance of PaymentAccount from a dict
payment_account_form_dict = payment_account.from_dict(payment_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


