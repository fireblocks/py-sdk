# SmartTransferStatisticInflow

Inflow tickets data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coins** | [**List[SmartTransferCoinStatistic]**](SmartTransferCoinStatistic.md) |  | [optional] 
**ticket_count** | **int** |  | [optional] 

## Example

```python
from fireblocks.models.smart_transfer_statistic_inflow import SmartTransferStatisticInflow

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferStatisticInflow from a JSON string
smart_transfer_statistic_inflow_instance = SmartTransferStatisticInflow.from_json(json)
# print the JSON string representation of the object
print(SmartTransferStatisticInflow.to_json())

# convert the object into a dict
smart_transfer_statistic_inflow_dict = smart_transfer_statistic_inflow_instance.to_dict()
# create an instance of SmartTransferStatisticInflow from a dict
smart_transfer_statistic_inflow_from_dict = SmartTransferStatisticInflow.from_dict(smart_transfer_statistic_inflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


