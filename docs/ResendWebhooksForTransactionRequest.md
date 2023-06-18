# ResendWebhooksForTransactionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resend_created** | **bool** |  | [optional] 
**resend_status_updated** | **bool** |  | [optional] 

## Example

```python
from fireblocks_client.models.resend_webhooks_for_transaction_request import ResendWebhooksForTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendWebhooksForTransactionRequest from a JSON string
resend_webhooks_for_transaction_request_instance = ResendWebhooksForTransactionRequest.from_json(json)
# print the JSON string representation of the object
print ResendWebhooksForTransactionRequest.to_json()

# convert the object into a dict
resend_webhooks_for_transaction_request_dict = resend_webhooks_for_transaction_request_instance.to_dict()
# create an instance of ResendWebhooksForTransactionRequest from a dict
resend_webhooks_for_transaction_request_form_dict = resend_webhooks_for_transaction_request.from_dict(resend_webhooks_for_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


