# NetworkRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**SourceTransferPeerPathResponse**](SourceTransferPeerPathResponse.md) |  | [optional] 
**destination** | [**DestinationTransferPeerPathResponse**](DestinationTransferPeerPathResponse.md) |  | [optional] 
**tx_hash** | **str** |  | [optional] 
**network_fee** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**net_amount** | **str** | The net amount of the transaction, after fee deduction | [optional] 
**is_dropped** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**destination_address** | **str** |  | [optional] 
**source_address** | **str** |  | [optional] 
**amount_usd** | **str** |  | [optional] 
**index** | **float** |  | [optional] 
**reward_info** | [**RewardInfo**](RewardInfo.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.network_record import NetworkRecord

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRecord from a JSON string
network_record_instance = NetworkRecord.from_json(json)
# print the JSON string representation of the object
print NetworkRecord.to_json()

# convert the object into a dict
network_record_dict = network_record_instance.to_dict()
# create an instance of NetworkRecord from a dict
network_record_form_dict = network_record.from_dict(network_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


