# ResendWebhooksByTransactionIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates whether the webhooks were successfully resent | 

## Example

```python
from fireblocks_client.models.resend_webhooks_by_transaction_id_response import ResendWebhooksByTransactionIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResendWebhooksByTransactionIdResponse from a JSON string
resend_webhooks_by_transaction_id_response_instance = ResendWebhooksByTransactionIdResponse.from_json(json)
# print the JSON string representation of the object
print ResendWebhooksByTransactionIdResponse.to_json()

# convert the object into a dict
resend_webhooks_by_transaction_id_response_dict = resend_webhooks_by_transaction_id_response_instance.to_dict()
# create an instance of ResendWebhooksByTransactionIdResponse from a dict
resend_webhooks_by_transaction_id_response_form_dict = resend_webhooks_by_transaction_id_response.from_dict(resend_webhooks_by_transaction_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


