# EmbeddedWalletPaginatedDevicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EmbeddedWalletDevice]**](EmbeddedWalletDevice.md) | The data of the current page | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks.models.embedded_wallet_paginated_devices_response import EmbeddedWalletPaginatedDevicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletPaginatedDevicesResponse from a JSON string
embedded_wallet_paginated_devices_response_instance = EmbeddedWalletPaginatedDevicesResponse.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletPaginatedDevicesResponse.to_json())

# convert the object into a dict
embedded_wallet_paginated_devices_response_dict = embedded_wallet_paginated_devices_response_instance.to_dict()
# create an instance of EmbeddedWalletPaginatedDevicesResponse from a dict
embedded_wallet_paginated_devices_response_from_dict = EmbeddedWalletPaginatedDevicesResponse.from_dict(embedded_wallet_paginated_devices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


