# PaymentRedirect

URL returned by the provider that the end user will be redirected to in order to complete the payment on the bank/mobile provider page. After completion, the bank/mobile provider redirects the end user back to successRedirectUrl (provided in the RAMP request)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to redirect to | [optional] 
**expires_at** | **str** | Expiration date of the redirect | [optional] 

## Example

```python
from fireblocks.models.payment_redirect import PaymentRedirect

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRedirect from a JSON string
payment_redirect_instance = PaymentRedirect.from_json(json)
# print the JSON string representation of the object
print(PaymentRedirect.to_json())

# convert the object into a dict
payment_redirect_dict = payment_redirect_instance.to_dict()
# create an instance of PaymentRedirect from a dict
payment_redirect_from_dict = PaymentRedirect.from_dict(payment_redirect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


