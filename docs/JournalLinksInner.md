# JournalLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of URL that describes the product and page | [optional] 
**url** | **str** | URL of Web of Science Product | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.journal_links_inner import JournalLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of JournalLinksInner from a JSON string
journal_links_inner_instance = JournalLinksInner.from_json(json)
# print the JSON string representation of the object
print JournalLinksInner.to_json()

# convert the object into a dict
journal_links_inner_dict = journal_links_inner_instance.to_dict()
# create an instance of JournalLinksInner from a dict
journal_links_inner_form_dict = journal_links_inner.from_dict(journal_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


