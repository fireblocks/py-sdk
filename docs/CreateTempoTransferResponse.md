# CreateTempoTransferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Fireblocks transaction ID. | [optional] 
**status** | **str** | The current status of the transaction. | [optional] 

## Example

```python
from fireblocks.models.create_tempo_transfer_response import CreateTempoTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTempoTransferResponse from a JSON string
create_tempo_transfer_response_instance = CreateTempoTransferResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTempoTransferResponse.to_json())

# convert the object into a dict
create_tempo_transfer_response_dict = create_tempo_transfer_response_instance.to_dict()
# create an instance of CreateTempoTransferResponse from a dict
create_tempo_transfer_response_from_dict = CreateTempoTransferResponse.from_dict(create_tempo_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


