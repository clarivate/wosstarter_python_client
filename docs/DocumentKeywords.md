# DocumentKeywords

Author keywords

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_keywords** | **List[str]** |  | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.document_keywords import DocumentKeywords

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentKeywords from a JSON string
document_keywords_instance = DocumentKeywords.from_json(json)
# print the JSON string representation of the object
print DocumentKeywords.to_json()

# convert the object into a dict
document_keywords_dict = document_keywords_instance.to_dict()
# create an instance of DocumentKeywords from a dict
document_keywords_form_dict = document_keywords.from_dict(document_keywords_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


