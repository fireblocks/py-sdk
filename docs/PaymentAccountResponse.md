# PaymentAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**PaymentAccountType**](PaymentAccountType.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.payment_account_response import PaymentAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAccountResponse from a JSON string
payment_account_response_instance = PaymentAccountResponse.from_json(json)
# print the JSON string representation of the object
print PaymentAccountResponse.to_json()

# convert the object into a dict
payment_account_response_dict = payment_account_response_instance.to_dict()
# create an instance of PaymentAccountResponse from a dict
payment_account_response_form_dict = payment_account_response.from_dict(payment_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


