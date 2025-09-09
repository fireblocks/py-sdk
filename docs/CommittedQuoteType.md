# CommittedQuoteType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates this is a committed quote | 
**expires_at** | **datetime** | ISO 8601 timestamp of the expiration time of the quote. | 

## Example

```python
from fireblocks.models.committed_quote_type import CommittedQuoteType

# TODO update the JSON string below
json = "{}"
# create an instance of CommittedQuoteType from a JSON string
committed_quote_type_instance = CommittedQuoteType.from_json(json)
# print the JSON string representation of the object
print(CommittedQuoteType.to_json())

# convert the object into a dict
committed_quote_type_dict = committed_quote_type_instance.to_dict()
# create an instance of CommittedQuoteType from a dict
committed_quote_type_from_dict = CommittedQuoteType.from_dict(committed_quote_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


