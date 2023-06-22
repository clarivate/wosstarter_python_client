# clarivate.wos_starter.client.model.metadata.Metadata

Information about total number of journals in the retrieve, number of recodrs on the page, and the page number

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about total number of journals in the retrieve, number of recodrs on the page, and the page number | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**page** | decimal.Decimal, int,  | decimal.Decimal,  | Page number (default is 1) | [optional] value must be a 32 bit integer
**limit** | decimal.Decimal, int,  | decimal.Decimal,  | Number of records on a page (default is 10). | [optional] value must be a 32 bit integer
**total** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of records for the request. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

