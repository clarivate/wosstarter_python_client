# Metadata

Information about total number of journals in the retrieve, number of recodrs on the page, and the page number

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Page number (default is 1) | [optional] 
**limit** | **int** | Number of records on a page (default is 10). | [optional] 
**total** | **int** | Total number of records for the request. | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print Metadata.to_json()

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_form_dict = metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


