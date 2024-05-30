# ResendWebhooksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages_count** | **float** |  | [optional] 

## Example

```python
from fireblocks_client.models.resend_webhooks_response import ResendWebhooksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResendWebhooksResponse from a JSON string
resend_webhooks_response_instance = ResendWebhooksResponse.from_json(json)
# print the JSON string representation of the object
print(ResendWebhooksResponse.to_json())

# convert the object into a dict
resend_webhooks_response_dict = resend_webhooks_response_instance.to_dict()
# create an instance of ResendWebhooksResponse from a dict
resend_webhooks_response_from_dict = ResendWebhooksResponse.from_dict(resend_webhooks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


