# SmartTransferStatisticOutflow

Outflow tickets data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coins** | [**List[SmartTransferCoinStatistic]**](SmartTransferCoinStatistic.md) |  | [optional] 
**ticket_count** | **int** |  | [optional] 

## Example

```python
from fireblocks.models.smart_transfer_statistic_outflow import SmartTransferStatisticOutflow

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferStatisticOutflow from a JSON string
smart_transfer_statistic_outflow_instance = SmartTransferStatisticOutflow.from_json(json)
# print the JSON string representation of the object
print(SmartTransferStatisticOutflow.to_json())

# convert the object into a dict
smart_transfer_statistic_outflow_dict = smart_transfer_statistic_outflow_instance.to_dict()
# create an instance of SmartTransferStatisticOutflow from a dict
smart_transfer_statistic_outflow_from_dict = SmartTransferStatisticOutflow.from_dict(smart_transfer_statistic_outflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


