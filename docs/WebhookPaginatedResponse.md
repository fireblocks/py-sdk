# WebhookPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Webhook]**](Webhook.md) | The data of the current page | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks.models.webhook_paginated_response import WebhookPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPaginatedResponse from a JSON string
webhook_paginated_response_instance = WebhookPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookPaginatedResponse.to_json())

# convert the object into a dict
webhook_paginated_response_dict = webhook_paginated_response_instance.to_dict()
# create an instance of WebhookPaginatedResponse from a dict
webhook_paginated_response_from_dict = WebhookPaginatedResponse.from_dict(webhook_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


