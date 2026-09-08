# CallAccepted

The outgoing transaction that carries the call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The outgoing transaction that carries the call. | 
**status** | **str** | The transaction&#39;s status at the time of this response — &#x60;SUBMITTED&#x60;. | 

## Example

```python
from fireblocks.models.call_accepted import CallAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of CallAccepted from a JSON string
call_accepted_instance = CallAccepted.from_json(json)
# print the JSON string representation of the object
print(CallAccepted.to_json())

# convert the object into a dict
call_accepted_dict = call_accepted_instance.to_dict()
# create an instance of CallAccepted from a dict
call_accepted_from_dict = CallAccepted.from_dict(call_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


