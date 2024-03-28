# DocumentsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**hits** | [**List[Document]**](Document.md) |  | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.documents_list import DocumentsList


json = '{"metadata": {"page": 1, "limit": 1, "total": 305}, "hits": [{"uid": "WOS:A1991KR78500001", "title": "A MODULAR NEURAL NETWORK MODEL OF CONCEPT-ACQUISITION", "types": ["Article"], "sourceTypes": ["Article"], "source": {"sourceTitle": "COGNITIVE SCIENCE", "publishYear": 1991, "publishMonth": "OCT-DEC", "volume": "15", "issue": "4", "pages": {"range": "461-508", "begin": "461", "end": "508", "count": 48}}, "names": {"authors": [{"displayName": "SCHYNS, PG", "wosStandard": "SCHYNS, PG", "researcherId": "AAT-6989-2020"}]}, "links": {"record": [], "references": [], "related": []}, "citations": [], "identifiers": {"doi": "10.1207/s15516709cog1504_1", "issn": "0364-0213"}, "keywords": {"authorKeywords": []}}]}'
# create an instance of DocumentsList from a JSON string
documents_list_instance = DocumentsList.from_json(json)
# print the JSON string representation of the object
print(documents_list_instance.to_json())

# convert the object into a dict
documents_list_dict = documents_list_instance.to_dict()
# create an instance of DocumentsList from a dict
documents_list_form_dict = DocumentsList.from_dict(documents_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


