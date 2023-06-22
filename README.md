# clarivate-wos-starter-python-client
The Web of Science™ Starter API provides basic metadata and search functionality for Web of Science™ Documents and Journals. Based on your subscription, this API can return times cited of documents.

## Resouces
This API follows the REST approach to disclose resources in URL format. Only the GET method is currently available to perform requests over HTTP.

The API is available on the [Clarivate Developer Portal](https://developer.clarivate.com/apis/wos-starter). You can find more details about the subscription and the Plans.

## Content

You can learn more about content at [Web of Science™ Product Page](https://clarivate.com/webofsciencegroup/solutions/web-of-science/) or in the [Web of Science™ Help](https://webofscience.help.clarivate.com/en-us/Content/home.htm).
The following attributes are available from in the API.
* UID (Unique Identifier)
* Title
* Issue
* Pages
* DOI
* Volume
* Times Cited
* ISSN/eISSN
* ISBN
* PubMed ID
* Source
* Web of Science URL
* Citing Articles Web of Science URL
* Publication Date
* Authors
* Author Keywords
* [Document Type](https://webofscience.help.clarivate.com/en-us/Content/document-types.html)
* Cited References Web of Science URL
* ResearcherID
* Book DOI
* Related Records Web of Science URL
* Journal Citations Reports URL



## Credentials

All requests require authentication with an API Key authentication flow. For more details, check the [Guide][https://developer.clarivate.com/help/api-access#key_access].

## Search and field tags for Web of Science documents
Web of Science™ offers [advanced search query builder](https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html). This API does not support all field tags for documents. [Web of Science API Expanded](https://developer.clarivate.com/apis/wos) offers all available field tags. The following table lists the field tags that are supported by this API.
| Field Tag | Description                                                                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TI        | Title of document                                                                                                                                           |
| IS        | ISSN or ISBN                                                                                                                                                |
| SO        | Source title - The result contains all source titles within product database (for example, journal titles and/or book titles if the product includes books) |
| VL        | Volume                                                                                                                                                      |
| PG        | Page                                                                                                                                                        |
| CS        | Issue                                                                                                                                                       |
| PY        | Year Published                                                                                                                                              |
| AU        | Author                                                                                                                                                      |
| AI        | Author Identifier                                                                                                                                                      |
| UT        | Accession Number                                                                                                                                            |
| DO        | DOI                                                                                                                                                         |
| DT        | [Document Type](https://webofscience.help.clarivate.com/en-us/Content/document-types.html)                                                                                                                                                         |
| PMID      | PubMed ID                                                                                                                                                   |
| OG        | Search for preferred organization names and/or their name variants from the Preferred Organization Index. <p> A search on a preferred organization name returns all records that contain the preferred name and all records that contain its name variants. A search on a name variant returns all records that contain the variant. For example, Cornell Law Sch returns all records that contain Cornell Law Sch in the Addresses field. <p> When searching for organization names that contain a Boolean (AND, NOT, NEAR, and SAME), always enclose the word in quotation marks ( \" \" ). For example: <p>   - OG=(Japan Science \"and\" Technology Agency (JST))      <br>   - OG=(\"Near\" East Univ)         <br> - OG=(\"OR\" Hlth Sci Univ)                           |
| TS        | Searches for topic terms in the following fields within a document: <p> - Title <br> - Abstract <br> - Author keywords <br> - Keywords Plus

## Pagination
To ensure fast response time, each search or multiple entity calls (such as `/documents`) retrieve only a certain number of hits/records.

There are two optional request parameters to browse along with the result&#58; _limit_ and _page_.

- limit&#58; Number of returned results, ranging from 0 to 50 (default **10**)
- page&#58; Specifying a page to retrieve (default **1**)

Moreover, this information is shown in the response body, in the tag **metadata**&#58;

```json
\"metadata\": {
  \"total\": 91,
  \"page\": 1,
  \"limit\": 10
}
```

## Errors
The WoS Journals API uses conventional HTTP success or failure status codes. For errors, some extra information is included to indicate what went wrong in the JSON response. The list of HTTP codes is listed below.

| Code  | Title  | Description |
|---|---|---|
| 400  | Bad request  | Request syntax error |
| 401  | Unauthorized  | The API key is invalid or missed |
| 404  | Not found  | The resource is not found |
| 405 | Method not allowed | Method other than GET is not allowed |
| 50X  | Server errors  | Technical error with servers|
Each error response (except `401 Unauthorized` error) contains the code of the error, the title of the error and detailed description of the error: a misprint in an endpoint, wrong URL parameter, etc. The example of the error message is shown below:

```json
  \"error\": {
    \"status\": 404,
    \"title\": \"Resource couldn't be found\",
    \"details\": \"There is no record found in the Web of Science database. Please check your query.\"
  }
```
For the `401 Unauthorized` error the response body is a little bit different:
```json
{
  \"error_description\": \"The access token is missing\",
  \"error\": \"invalid_request\"
}


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import clarivate.wos_starter.client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import clarivate.wos_starter.client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import clarivate.wos_starter.client
from pprint import pprint
from clarivate.wos_starter.client.apis.tags import documents_api
from clarivate.wos_starter.client.model.document import Document
from clarivate.wos_starter.client.model.documents_list import DocumentsList
# Defining the host is optional and defaults to http://api.clarivate.com/apis/wos-starter
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://api.clarivate.com/apis/wos-starter"
)


# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    q = "PY=2020" # str | Web of Science advanced [advanced search query builder](https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html). The supported field tags are listed in description.
db = "WOS" # str | Web of Science Database abbreviation * WOS - Web of Science Core collection * BIOABS - Biological Abstracts * BCI - BIOSIS Citation Index * BIOSIS - BIOSIS Previews * CCC - Current Contents Connect * DIIDW - Derwent Innovations Index * DRCI - Data Citation Index * MEDLINE - MEDLINE The U.S. National Library of Medicine® (NLM®) premier life sciences database. * ZOOREC - Zoological Records * PPRN - Preprint Citation Index * WOK - All databases  (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=true, isPathParam=false, isHeaderParam=false, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=true, baseName='db', paramName='db', dataType='str', datatypeWithEnum='DbEnum', dataFormat='null', collectionFormat='null', description='Web of Science Database abbreviation * WOS - Web of Science Core collection * BIOABS - Biological Abstracts * BCI - BIOSIS Citation Index * BIOSIS - BIOSIS Previews * CCC - Current Contents Connect * DIIDW - Derwent Innovations Index * DRCI - Data Citation Index * MEDLINE - MEDLINE The U.S. National Library of Medicine® (NLM®) premier life sciences database. * ZOOREC - Zoological Records * PPRN - Preprint Citation Index * WOK - All databases ', unescapedDescription='Web of Science Database abbreviation
* WOS - Web of Science Core collection
* BIOABS - Biological Abstracts
* BCI - BIOSIS Citation Index
* BIOSIS - BIOSIS Previews
* CCC - Current Contents Connect
* DIIDW - Derwent Innovations Index
* DRCI - Data Citation Index
* MEDLINE - MEDLINE The U.S. National Library of Medicine® (NLM®) premier life sciences database.
* ZOOREC - Zoological Records
* PPRN - Preprint Citation Index
* WOK - All databases
', baseType='null', defaultValue='"WOS"', enumDefaultValue='"WOS"', enumName='DbEnum', style='FORM', deepObject='false', allowEmptyValue='false', example='"WOS"', jsonSchema='{
  "name" : "db",
  "in" : "query",
  "description" : "Web of Science Database abbreviation\n* WOS - Web of Science Core collection\n* BIOABS - Biological Abstracts\n* BCI - BIOSIS Citation Index\n* BIOSIS - BIOSIS Previews\n* CCC - Current Contents Connect\n* DIIDW - Derwent Innovations Index\n* DRCI - Data Citation Index\n* MEDLINE - MEDLINE The U.S. National Library of Medicine® (NLM®) premier life sciences database.\n* ZOOREC - Zoological Records\n* PPRN - Preprint Citation Index\n* WOK - All databases\n",
  "required" : false,
  "style" : "form",
  "explode" : true,
  "schema" : {
    "type" : "string",
    "default" : "WOS",
    "enum" : [ "BCI", "BIOABS", "BIOSIS", "CCC", "DIIDW", "DRCI", "MEDLINE", "PPRN", "WOK", "WOS", "ZOOREC" ]
  }
}', isString=true, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=true, _enum=[BCI, BIOABS, BIOSIS, CCC, DIIDW, DRCI, MEDLINE, PPRN, WOK, WOS, ZOOREC], allowableValues={values=[BCI, BIOABS, BIOSIS, CCC, DIIDW, DRCI, MEDLINE, PPRN, WOK, WOS, ZOOREC], enumVars=[{name=BCI, isString=true, value="BCI"}, {name=BIOABS, isString=true, value="BIOABS"}, {name=BIOSIS, isString=true, value="BIOSIS"}, {name=CCC, isString=true, value="CCC"}, {name=DIIDW, isString=true, value="DIIDW"}, {name=DRCI, isString=true, value="DRCI"}, {name=MEDLINE, isString=true, value="MEDLINE"}, {name=PPRN, isString=true, value="PPRN"}, {name=WOK, isString=true, value="WOK"}, {name=WOS, isString=true, value="WOS"}, {name=ZOOREC, isString=true, value="ZOOREC"}]}, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=false, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='null', exclusiveMaximum=false, minimum='null', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='string', baseName='DbSchema', complexType='null', getter='getDb', setter='setDb', description='null', dataType='str', datatypeWithEnum='DbEnum', dataFormat='null', name='db', min='null', max='null', defaultValue='"WOS"', defaultValueWithParam=' = data.db;', baseType='str', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='"WOS"', jsonSchema='{
  "type" : "string",
  "default" : "WOS",
  "enum" : [ "BCI", "BIOABS", "BIOSIS", "CCC", "DIIDW", "DRCI", "MEDLINE", "PPRN", "WOK", "WOS", "ZOOREC" ]
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=true, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=true, isInnerEnum=true, isEnumRef=true, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, isNew=false, isOverridden=null, _enum=[BCI, BIOABS, BIOSIS, CCC, DIIDW, DRCI, MEDLINE, PPRN, WOK, WOS, ZOOREC], allowableValues={enumVars=[{name=BCI, isString=true, value="BCI"}, {name=BIOABS, isString=true, value="BIOABS"}, {name=BIOSIS, isString=true, value="BIOSIS"}, {name=CCC, isString=true, value="CCC"}, {name=DIIDW, isString=true, value="DIIDW"}, {name=DRCI, isString=true, value="DRCI"}, {name=MEDLINE, isString=true, value="MEDLINE"}, {name=PPRN, isString=true, value="PPRN"}, {name=WOK, isString=true, value="WOK"}, {name=WOS, isString=true, value="WOS"}, {name=ZOOREC, isString=true, value="ZOOREC"}], values=[BCI, BIOABS, BIOSIS, CCC, DIIDW, DRCI, MEDLINE, PPRN, WOK, WOS, ZOOREC]}, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='Db', nameInSnakeCase='null', enumName='DbEnum', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})
limit = 10 # int | set the limit of records on the page (1-50) (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=true, isPathParam=false, isHeaderParam=false, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=true, baseName='limit', paramName='limit', dataType='int', datatypeWithEnum='null', dataFormat='int32', collectionFormat='null', description='set the limit of records on the page (1-50)', unescapedDescription='set the limit of records on the page (1-50)', baseType='null', defaultValue='10', enumDefaultValue='null', enumName='null', style='FORM', deepObject='false', allowEmptyValue='false', example='10', jsonSchema='{
  "name" : "limit",
  "in" : "query",
  "description" : "set the limit of records on the page (1-50)",
  "required" : false,
  "style" : "form",
  "explode" : true,
  "schema" : {
    "maximum" : 50,
    "minimum" : 1,
    "type" : "integer",
    "format" : "int32",
    "default" : 10
  }
}', isString=false, isNumeric=false, isInteger=true, isShort=true, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=false, _enum=null, allowableValues=null, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=true, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='50', exclusiveMaximum=false, minimum='1', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='integer', baseName='LimitSchema', complexType='null', getter='getLimit', setter='setLimit', description='null', dataType='int', datatypeWithEnum='int', dataFormat='int32', name='limit', min='null', max='null', defaultValue='10', defaultValueWithParam=' = data.limit;', baseType='int', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='10', jsonSchema='{
  "maximum" : 50,
  "minimum" : 1,
  "type" : "integer",
  "format" : "int32",
  "default" : 10
}', minimum='1', maximum='50', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=false, isNumeric=false, isInteger=true, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=false, isInnerEnum=false, isEnumRef=false, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, isNew=false, isOverridden=null, _enum=null, allowableValues=null, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=true, isInherited=false, discriminatorValue='null', nameInCamelCase='Limit', nameInSnakeCase='null', enumName='null', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=int32, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})
page = 1 # int | set the result page (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=true, isPathParam=false, isHeaderParam=false, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=true, baseName='page', paramName='page', dataType='int', datatypeWithEnum='null', dataFormat='int32', collectionFormat='null', description='set the result page', unescapedDescription='set the result page', baseType='null', defaultValue='1', enumDefaultValue='null', enumName='null', style='FORM', deepObject='false', allowEmptyValue='false', example='1', jsonSchema='{
  "name" : "page",
  "in" : "query",
  "description" : "set the result page",
  "required" : false,
  "style" : "form",
  "explode" : true,
  "schema" : {
    "type" : "integer",
    "format" : "int32",
    "default" : 1
  }
}', isString=false, isNumeric=false, isInteger=true, isShort=true, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=false, _enum=null, allowableValues=null, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=false, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='null', exclusiveMaximum=false, minimum='null', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='integer', baseName='PageSchema', complexType='null', getter='getPage', setter='setPage', description='null', dataType='int', datatypeWithEnum='int', dataFormat='int32', name='page', min='null', max='null', defaultValue='1', defaultValueWithParam=' = data.page;', baseType='int', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='1', jsonSchema='{
  "type" : "integer",
  "format" : "int32",
  "default" : 1
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=false, isNumeric=false, isInteger=true, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=false, isInnerEnum=false, isEnumRef=false, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, isNew=false, isOverridden=null, _enum=null, allowableValues=null, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='Page', nameInSnakeCase='null', enumName='null', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=int32, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})
sort_field = "sortField_example" # str | Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. Supported fields:  * **LD** - Load Date * **PY** - Publication Year * **RS** - Relevance * **TC** - Times Cited  (optional)

    try:
        # Query Web of Science documents 
        api_response = api_instance.documents_get(qdb=dblimit=limitpage=pagesort_field=sort_field)
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling DocumentsApi->documents_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://api.clarivate.com/apis/wos-starter*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DocumentsApi* | [**documents_get**](docs/apis/tags/DocumentsApi.md#documents_get) | **get** /documents | Query Web of Science documents 
*DocumentsApi* | [**documents_uid_get**](docs/apis/tags/DocumentsApi.md#documents_uid_get) | **get** /documents/{uid} | Get Web of Science document by Accesssion Number (UID)
*JournalsApi* | [**journals_get**](docs/apis/tags/JournalsApi.md#journals_get) | **get** /journals | Query Journals by ISSN
*JournalsApi* | [**journals_id_get**](docs/apis/tags/JournalsApi.md#journals_id_get) | **get** /journals/{id} | Get Journal by ID

## Documentation For Models

 - [AuthorName](docs/models/AuthorName.md)
 - [Document](docs/models/Document.md)
 - [DocumentsList](docs/models/DocumentsList.md)
 - [Journal](docs/models/Journal.md)
 - [JournalsList](docs/models/JournalsList.md)
 - [Metadata](docs/models/Metadata.md)
 - [OtherName](docs/models/OtherName.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## ClarivateApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-ApiKey
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in clarivate.wos_starter.client.apis and clarivate.wos_starter.client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from clarivate.wos_starter.client.apis.default_api import DefaultApi`
- `from clarivate.wos_starter.client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import clarivate.wos_starter.client
from clarivate.wos_starter.client.apis import *
from clarivate.wos_starter.client.models import *
```
