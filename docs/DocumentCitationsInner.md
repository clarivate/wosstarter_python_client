# DocumentCitationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db** | **str** | Web of Science Citation Database (collection) Abbreviation Name | [optional] 
**count** | **int** | Citation Count | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.document_citations_inner import DocumentCitationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCitationsInner from a JSON string
document_citations_inner_instance = DocumentCitationsInner.from_json(json)
# print the JSON string representation of the object
print DocumentCitationsInner.to_json()

# convert the object into a dict
document_citations_inner_dict = document_citations_inner_instance.to_dict()
# create an instance of DocumentCitationsInner from a dict
document_citations_inner_form_dict = document_citations_inner.from_dict(document_citations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


