# TransactionTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the tag | 
**label** | **str** | The tag label | 

## Example

```python
from fireblocks.models.transaction_tag import TransactionTag

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTag from a JSON string
transaction_tag_instance = TransactionTag.from_json(json)
# print the JSON string representation of the object
print(TransactionTag.to_json())

# convert the object into a dict
transaction_tag_dict = transaction_tag_instance.to_dict()
# create an instance of TransactionTag from a dict
transaction_tag_from_dict = TransactionTag.from_dict(transaction_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


