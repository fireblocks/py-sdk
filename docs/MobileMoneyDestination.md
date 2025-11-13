# MobileMoneyDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**MobileMoneyAddress**](MobileMoneyAddress.md) |  | 

## Example

```python
from fireblocks.models.mobile_money_destination import MobileMoneyDestination

# TODO update the JSON string below
json = "{}"
# create an instance of MobileMoneyDestination from a JSON string
mobile_money_destination_instance = MobileMoneyDestination.from_json(json)
# print the JSON string representation of the object
print(MobileMoneyDestination.to_json())

# convert the object into a dict
mobile_money_destination_dict = mobile_money_destination_instance.to_dict()
# create an instance of MobileMoneyDestination from a dict
mobile_money_destination_from_dict = MobileMoneyDestination.from_dict(mobile_money_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


