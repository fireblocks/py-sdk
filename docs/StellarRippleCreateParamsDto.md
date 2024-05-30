# StellarRippleCreateParamsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | The symbol of the token | 
**name** | **str** | The name of the token | 
**issuer_address** | **str** | The address of the issuer of this token. Will be part of the identifier of this token on chain. | 

## Example

```python
from fireblocks_client.models.stellar_ripple_create_params_dto import StellarRippleCreateParamsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StellarRippleCreateParamsDto from a JSON string
stellar_ripple_create_params_dto_instance = StellarRippleCreateParamsDto.from_json(json)
# print the JSON string representation of the object
print(StellarRippleCreateParamsDto.to_json())

# convert the object into a dict
stellar_ripple_create_params_dto_dict = stellar_ripple_create_params_dto_instance.to_dict()
# create an instance of StellarRippleCreateParamsDto from a dict
stellar_ripple_create_params_dto_from_dict = StellarRippleCreateParamsDto.from_dict(stellar_ripple_create_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


