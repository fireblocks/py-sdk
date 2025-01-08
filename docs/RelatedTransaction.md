# RelatedTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** | The transaction ID | 
**completed** | **bool** | Is the transaction completed or not | 

## Example

```python
from fireblocks.models.related_transaction import RelatedTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedTransaction from a JSON string
related_transaction_instance = RelatedTransaction.from_json(json)
# print the JSON string representation of the object
print(RelatedTransaction.to_json())

# convert the object into a dict
related_transaction_dict = related_transaction_instance.to_dict()
# create an instance of RelatedTransaction from a dict
related_transaction_from_dict = RelatedTransaction.from_dict(related_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


