# Journal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Journal unique identifier | [optional] 
**name** | **str** | Journal full name | [optional] 
**jcr_title** | **str** | Journal JCR abbreviation | [optional] 
**iso_title** | **str** | Journal title in (ISO format) | [optional] 
**issn** | **str** | Journal ISSN | [optional] 
**previous_issn** | **List[str]** | Previous ISSNs of the Journal (can be empty) | [optional] 
**e_issn** | **str** | Journal eISSN | [optional] 
**links** | [**List[JournalLinksInner]**](JournalLinksInner.md) | URL to the Web of Science Products | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.journal import Journal

# TODO update the JSON string below
json = "{}"
# create an instance of Journal from a JSON string
journal_instance = Journal.from_json(json)
# print the JSON string representation of the object
print Journal.to_json()

# convert the object into a dict
journal_dict = journal_instance.to_dict()
# create an instance of Journal from a dict
journal_form_dict = journal.from_dict(journal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


