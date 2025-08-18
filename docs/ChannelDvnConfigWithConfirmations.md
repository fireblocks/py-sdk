# ChannelDvnConfigWithConfirmations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_config** | [**ChannelDvnConfigWithConfirmationsSendConfig**](ChannelDvnConfigWithConfirmationsSendConfig.md) |  | [optional] 
**receive_config** | [**ChannelDvnConfigWithConfirmationsReceiveConfig**](ChannelDvnConfigWithConfirmationsReceiveConfig.md) |  | [optional] 

## Example

```python
from fireblocks.models.channel_dvn_config_with_confirmations import ChannelDvnConfigWithConfirmations

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelDvnConfigWithConfirmations from a JSON string
channel_dvn_config_with_confirmations_instance = ChannelDvnConfigWithConfirmations.from_json(json)
# print the JSON string representation of the object
print(ChannelDvnConfigWithConfirmations.to_json())

# convert the object into a dict
channel_dvn_config_with_confirmations_dict = channel_dvn_config_with_confirmations_instance.to_dict()
# create an instance of ChannelDvnConfigWithConfirmations from a dict
channel_dvn_config_with_confirmations_from_dict = ChannelDvnConfigWithConfirmations.from_dict(channel_dvn_config_with_confirmations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


