# clarivate.wos_starter.client.model.document.Document

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uid** | str,  | str,  | Web of Science Unique Identifier | 
**title** | str,  | str,  | Document title | [optional] 
**[types](#types)** | list, tuple,  | tuple,  | Normalized Document Types | [optional] 
**[sourceTypes](#sourceTypes)** | list, tuple,  | tuple,  | Source Document Types | [optional] 
**[source](#source)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Web of Science document source metadata | [optional] 
**[names](#names)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[links](#links)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Web of Science URLs | [optional] 
**[citations](#citations)** | list, tuple,  | tuple,  | Times Cited | [optional] 
**[identifiers](#identifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Document and Source Identifiers | [optional] 
**[keywords](#keywords)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Author keywords | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# types

Normalized Document Types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Normalized Document Types | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Normalized Document type | 

# sourceTypes

Source Document Types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Source Document Types | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Source Document type | 

# source

Web of Science document source metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Web of Science document source metadata | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sourceTitle** | str,  | str,  | Source title | [optional] 
**publishYear** | decimal.Decimal, int,  | decimal.Decimal,  | Published Year | [optional] value must be a 32 bit integer
**publishMonth** | str,  | str,  | Published Month | [optional] 
**volume** | str,  | str,  | Volume | [optional] 
**issue** | str,  | str,  | Issue | [optional] 
**supplement** | str,  | str,  | Journal supplement | [optional] 
**specialIssue** | str,  | str,  | Journal special issue | [optional] 
**articleNumber** | str,  | str,  | Source Article Number | [optional] 
**[pages](#pages)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# pages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**range** | str,  | str,  | Page range | [optional] 
**begin** | str,  | str,  | Page begin | [optional] 
**end** | str,  | str,  | Page end | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of pages | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[authors](#authors)** | list, tuple,  | tuple,  | Authors of document | [optional] 
**[inventors](#inventors)** | list, tuple,  | tuple,  |  | [optional] 
**[bookCorp](#bookCorp)** | list, tuple,  | tuple,  |  | [optional] 
**[bookEditors](#bookEditors)** | list, tuple,  | tuple,  |  | [optional] 
**[books](#books)** | list, tuple,  | tuple,  |  | [optional] 
**[additionalAuthors](#additionalAuthors)** | list, tuple,  | tuple,  |  | [optional] 
**[anonymous](#anonymous)** | list, tuple,  | tuple,  |  | [optional] 
**[assignees](#assignees)** | list, tuple,  | tuple,  |  | [optional] 
**[corp](#corp)** | list, tuple,  | tuple,  |  | [optional] 
**[editors](#editors)** | list, tuple,  | tuple,  |  | [optional] 
**[investigators](#investigators)** | list, tuple,  | tuple,  |  | [optional] 
**[sponsors](#sponsors)** | list, tuple,  | tuple,  |  | [optional] 
**[issuingOrganizations](#issuingOrganizations)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# authors

Authors of document

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Authors of document | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AuthorName**](AuthorName.md) | [**AuthorName**](AuthorName.md) | [**AuthorName**](AuthorName.md) |  | 

# inventors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# bookCorp

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# bookEditors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# books

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# additionalAuthors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# anonymous

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# assignees

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# corp

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# editors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# investigators

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# sponsors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# issuingOrganizations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) | [**OtherName**](OtherName.md) |  | 

# links

Web of Science URLs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Web of Science URLs | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**record** | str,  | str,  |  | [optional] 
**citingArticles** | str,  | str,  |  | [optional] 
**references** | str,  | str,  |  | [optional] 
**related** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# citations

Times Cited

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Times Cited | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**db** | str,  | str,  | Web of Science Citation Database (collection) Abbreviation Name | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Citation Count | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# identifiers

Document and Source Identifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Document and Source Identifiers | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**doi** | str,  | str,  |  | [optional] 
**issn** | str,  | str,  |  | [optional] 
**eissn** | str,  | str,  |  | [optional] 
**isbn** | str,  | str,  |  | [optional] 
**eisbn** | str,  | str,  |  | [optional] 
**pmid** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# keywords

Author keywords

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Author keywords | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[authorKeywords](#authorKeywords)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# authorKeywords

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

