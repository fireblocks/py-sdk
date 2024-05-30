# ResendTransactionWebhooksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resend_created** | **bool** |  | [optional] 
**resend_status_updated** | **bool** |  | [optional] 

## Example

```python
from fireblocks.models.resend_transaction_webhooks_request import ResendTransactionWebhooksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendTransactionWebhooksRequest from a JSON string
resend_transaction_webhooks_request_instance = ResendTransactionWebhooksRequest.from_json(json)
# print the JSON string representation of the object
print(ResendTransactionWebhooksRequest.to_json())

# convert the object into a dict
resend_transaction_webhooks_request_dict = resend_transaction_webhooks_request_instance.to_dict()
# create an instance of ResendTransactionWebhooksRequest from a dict
resend_transaction_webhooks_request_from_dict = ResendTransactionWebhooksRequest.from_dict(resend_transaction_webhooks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


