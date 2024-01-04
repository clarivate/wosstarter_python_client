# DocumentNames


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authors** | [**List[AuthorName]**](AuthorName.md) | Authors of document | [optional] 
**inventors** | [**List[OtherName]**](OtherName.md) |  | [optional] 
**book_corp** | [**List[OtherName]**](OtherName.md) |  | [optional] 
**book_editors** | [**List[OtherName]**](OtherName.md) |  | [optional] 
**books** | [**List[OtherName]**](OtherName.md) |  | [optional] 
**additional_authors** | [**List[OtherName]**](OtherName.md) |  | [optional] 
**anonymous** | [**List[OtherName]**](OtherName.md) |  | [optional] 
**assignees** | [**List[OtherName]**](OtherName.md) |  | [optional] 
**corp** | [**List[OtherName]**](OtherName.md) |  | [optional] 
**editors** | [**List[OtherName]**](OtherName.md) |  | [optional] 
**investigators** | [**List[OtherName]**](OtherName.md) |  | [optional] 
**sponsors** | [**List[OtherName]**](OtherName.md) |  | [optional] 
**issuing_organizations** | [**List[OtherName]**](OtherName.md) |  | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.document_names import DocumentNames

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentNames from a JSON string
document_names_instance = DocumentNames.from_json(json)
# print the JSON string representation of the object
print DocumentNames.to_json()

# convert the object into a dict
document_names_dict = document_names_instance.to_dict()
# create an instance of DocumentNames from a dict
document_names_form_dict = document_names.from_dict(document_names_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


