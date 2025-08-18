# ChannelDvnConfigWithConfirmationsSendConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dvn_addresses** | **List[str]** | Array of required DVN Ethereum addresses that sign ULN messages. | 
**optional_dvn_addresses** | **List[str]** | Array of optional DVN Ethereum addresses that sign ULN messages. | [optional] 
**optional_threshold** | **float** | Minimum number of DVN signatures required (M-of-N). | 
**confirmations** | **float** | Number of block confirmations required | 

## Example

```python
from fireblocks.models.channel_dvn_config_with_confirmations_send_config import ChannelDvnConfigWithConfirmationsSendConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelDvnConfigWithConfirmationsSendConfig from a JSON string
channel_dvn_config_with_confirmations_send_config_instance = ChannelDvnConfigWithConfirmationsSendConfig.from_json(json)
# print the JSON string representation of the object
print(ChannelDvnConfigWithConfirmationsSendConfig.to_json())

# convert the object into a dict
channel_dvn_config_with_confirmations_send_config_dict = channel_dvn_config_with_confirmations_send_config_instance.to_dict()
# create an instance of ChannelDvnConfigWithConfirmationsSendConfig from a dict
channel_dvn_config_with_confirmations_send_config_from_dict = ChannelDvnConfigWithConfirmationsSendConfig.from_dict(channel_dvn_config_with_confirmations_send_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


