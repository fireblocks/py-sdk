# WebhookMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the metric | 

## Example

```python
from fireblocks.models.webhook_metric import WebhookMetric

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMetric from a JSON string
webhook_metric_instance = WebhookMetric.from_json(json)
# print the JSON string representation of the object
print(WebhookMetric.to_json())

# convert the object into a dict
webhook_metric_dict = webhook_metric_instance.to_dict()
# create an instance of WebhookMetric from a dict
webhook_metric_from_dict = WebhookMetric.from_dict(webhook_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


