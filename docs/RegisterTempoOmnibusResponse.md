# RegisterTempoOmnibusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** | The ID of the wallet activation transaction. Absent when no activation transaction was submitted. | [optional] 
**status** | **str** | The status of the Tempo omnibus wallet. &#x60;READY&#x60; is returned with 200; &#x60;PROCESSING&#x60; and &#x60;PENDING_ACTIVATION&#x60; are returned with 202. A failed activation is returned as an error. | 

## Example

```python
from fireblocks.models.register_tempo_omnibus_response import RegisterTempoOmnibusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterTempoOmnibusResponse from a JSON string
register_tempo_omnibus_response_instance = RegisterTempoOmnibusResponse.from_json(json)
# print the JSON string representation of the object
print(RegisterTempoOmnibusResponse.to_json())

# convert the object into a dict
register_tempo_omnibus_response_dict = register_tempo_omnibus_response_instance.to_dict()
# create an instance of RegisterTempoOmnibusResponse from a dict
register_tempo_omnibus_response_from_dict = RegisterTempoOmnibusResponse.from_dict(register_tempo_omnibus_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


