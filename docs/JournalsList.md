# JournalsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**hits** | [**List[Journal]**](Journal.md) |  | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.journals_list import JournalsList

# TODO update the JSON string below
json = "{}"
# create an instance of JournalsList from a JSON string
journals_list_instance = JournalsList.from_json(json)
# print the JSON string representation of the object
print JournalsList.to_json()

# convert the object into a dict
journals_list_dict = journals_list_instance.to_dict()
# create an instance of JournalsList from a dict
journals_list_form_dict = journals_list.from_dict(journals_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


