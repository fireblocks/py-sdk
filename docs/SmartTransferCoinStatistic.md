# SmartTransferCoinStatistic

Smart transfer coin statistic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.smart_transfer_coin_statistic import SmartTransferCoinStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferCoinStatistic from a JSON string
smart_transfer_coin_statistic_instance = SmartTransferCoinStatistic.from_json(json)
# print the JSON string representation of the object
print(SmartTransferCoinStatistic.to_json())

# convert the object into a dict
smart_transfer_coin_statistic_dict = smart_transfer_coin_statistic_instance.to_dict()
# create an instance of SmartTransferCoinStatistic from a dict
smart_transfer_coin_statistic_from_dict = SmartTransferCoinStatistic.from_dict(smart_transfer_coin_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


