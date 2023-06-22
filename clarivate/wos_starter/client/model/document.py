# coding: utf-8

"""
    Web of Science™ Starter API

    The Web of Science™ Starter API provides basic metadata and search functionality for Web of Science™ Documents and Journals. Based on your subscription, this API can return times cited of documents.  ## Resouces This API follows the REST approach to disclose resources in URL format. Only the GET method is currently available to perform requests over HTTP.  The API is available on the [Clarivate Developer Portal](https://developer.clarivate.com/apis/wos-starter). You can find more details about the subscription and the Plans.  ## Content  You can learn more about content at [Web of Science™ Product Page](https://clarivate.com/webofsciencegroup/solutions/web-of-science/) or in the [Web of Science™ Help](https://webofscience.help.clarivate.com/en-us/Content/home.htm). The following attributes are available from in the API. * UID (Unique Identifier) * Title * Issue * Pages * DOI * Volume * Times Cited * ISSN/eISSN * ISBN * PubMed ID * Source * Web of Science URL * Citing Articles Web of Science URL * Publication Date * Authors * Author Keywords * [Document Type](https://webofscience.help.clarivate.com/en-us/Content/document-types.html) * Cited References Web of Science URL * ResearcherID * Book DOI * Related Records Web of Science URL * Journal Citations Reports URL    ## Credentials  All requests require authentication with an API Key authentication flow. For more details, check the [Guide][https://developer.clarivate.com/help/api-access#key_access].  ## Search and field tags for Web of Science documents Web of Science™ offers [advanced search query builder](https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html). This API does not support all field tags for documents. [Web of Science API Expanded](https://developer.clarivate.com/apis/wos) offers all available field tags. The following table lists the field tags that are supported by this API. | Field Tag | Description                                                                                                                                                 | |-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------| | TI        | Title of document                                                                                                                                           | | IS        | ISSN or ISBN                                                                                                                                                | | SO        | Source title - The result contains all source titles within product database (for example, journal titles and/or book titles if the product includes books) | | VL        | Volume                                                                                                                                                      | | PG        | Page                                                                                                                                                        | | CS        | Issue                                                                                                                                                       | | PY        | Year Published                                                                                                                                              | | AU        | Author                                                                                                                                                      | | AI        | Author Identifier                                                                                                                                                      | | UT        | Accession Number                                                                                                                                            | | DO        | DOI                                                                                                                                                         | | DT        | [Document Type](https://webofscience.help.clarivate.com/en-us/Content/document-types.html)                                                                                                                                                         | | PMID      | PubMed ID                                                                                                                                                   | | OG        | Search for preferred organization names and/or their name variants from the Preferred Organization Index. <p> A search on a preferred organization name returns all records that contain the preferred name and all records that contain its name variants. A search on a name variant returns all records that contain the variant. For example, Cornell Law Sch returns all records that contain Cornell Law Sch in the Addresses field. <p> When searching for organization names that contain a Boolean (AND, NOT, NEAR, and SAME), always enclose the word in quotation marks ( \" \" ). For example: <p>   - OG=(Japan Science \"and\" Technology Agency (JST))      <br>   - OG=(\"Near\" East Univ)         <br> - OG=(\"OR\" Hlth Sci Univ)                           | | TS        | Searches for topic terms in the following fields within a document: <p> - Title <br> - Abstract <br> - Author keywords <br> - Keywords Plus  ## Pagination To ensure fast response time, each search or multiple entity calls (such as `/documents`) retrieve only a certain number of hits/records.  There are two optional request parameters to browse along with the result&#58; _limit_ and _page_.  - limit&#58; Number of returned results, ranging from 0 to 50 (default **10**) - page&#58; Specifying a page to retrieve (default **1**)  Moreover, this information is shown in the response body, in the tag **metadata**&#58;  ```json \"metadata\": {   \"total\": 91,   \"page\": 1,   \"limit\": 10 } ```  ## Errors The WoS Journals API uses conventional HTTP success or failure status codes. For errors, some extra information is included to indicate what went wrong in the JSON response. The list of HTTP codes is listed below.  | Code  | Title  | Description | |---|---|---| | 400  | Bad request  | Request syntax error | | 401  | Unauthorized  | The API key is invalid or missed | | 404  | Not found  | The resource is not found | | 405 | Method not allowed | Method other than GET is not allowed | | 50X  | Server errors  | Technical error with servers| Each error response (except `401 Unauthorized` error) contains the code of the error, the title of the error and detailed description of the error: a misprint in an endpoint, wrong URL parameter, etc. The example of the error message is shown below:  ```json   \"error\": {     \"status\": 404,     \"title\": \"Resource couldn't be found\",     \"details\": \"There is no record found in the Web of Science database. Please check your query.\"   } ``` For the `401 Unauthorized` error the response body is a little bit different: ```json {   \"error_description\": \"The access token is missing\",   \"error\": \"invalid_request\" }   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from clarivate.wos_starter.client import schemas  # noqa: F401


class Document(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "uid",
        }
        
        class properties:
            uid = schemas.StrSchema
            title = schemas.StrSchema
            
            
            class types(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'types':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class sourceTypes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sourceTypes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class source(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        sourceTitle = schemas.StrSchema
                        publishYear = schemas.Int32Schema
                        publishMonth = schemas.StrSchema
                        volume = schemas.StrSchema
                        issue = schemas.StrSchema
                        supplement = schemas.StrSchema
                        specialIssue = schemas.StrSchema
                        articleNumber = schemas.StrSchema
                        
                        
                        class pages(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    range = schemas.StrSchema
                                    begin = schemas.StrSchema
                                    end = schemas.StrSchema
                                    count = schemas.Int32Schema
                                    __annotations__ = {
                                        "range": range,
                                        "begin": begin,
                                        "end": end,
                                        "count": count,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["range"]) -> MetaOapg.properties.range: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["begin"]) -> MetaOapg.properties.begin: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["range", "begin", "end", "count", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["range"]) -> typing.Union[MetaOapg.properties.range, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["begin"]) -> typing.Union[MetaOapg.properties.begin, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> typing.Union[MetaOapg.properties.end, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["range", "begin", "end", "count", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                range: typing.Union[MetaOapg.properties.range, str, schemas.Unset] = schemas.unset,
                                begin: typing.Union[MetaOapg.properties.begin, str, schemas.Unset] = schemas.unset,
                                end: typing.Union[MetaOapg.properties.end, str, schemas.Unset] = schemas.unset,
                                count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'pages':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    range=range,
                                    begin=begin,
                                    end=end,
                                    count=count,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "sourceTitle": sourceTitle,
                            "publishYear": publishYear,
                            "publishMonth": publishMonth,
                            "volume": volume,
                            "issue": issue,
                            "supplement": supplement,
                            "specialIssue": specialIssue,
                            "articleNumber": articleNumber,
                            "pages": pages,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["sourceTitle"]) -> MetaOapg.properties.sourceTitle: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["publishYear"]) -> MetaOapg.properties.publishYear: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["publishMonth"]) -> MetaOapg.properties.publishMonth: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["volume"]) -> MetaOapg.properties.volume: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["issue"]) -> MetaOapg.properties.issue: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["supplement"]) -> MetaOapg.properties.supplement: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["specialIssue"]) -> MetaOapg.properties.specialIssue: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["articleNumber"]) -> MetaOapg.properties.articleNumber: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["pages"]) -> MetaOapg.properties.pages: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["sourceTitle", "publishYear", "publishMonth", "volume", "issue", "supplement", "specialIssue", "articleNumber", "pages", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sourceTitle"]) -> typing.Union[MetaOapg.properties.sourceTitle, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["publishYear"]) -> typing.Union[MetaOapg.properties.publishYear, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["publishMonth"]) -> typing.Union[MetaOapg.properties.publishMonth, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["volume"]) -> typing.Union[MetaOapg.properties.volume, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["issue"]) -> typing.Union[MetaOapg.properties.issue, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["supplement"]) -> typing.Union[MetaOapg.properties.supplement, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["specialIssue"]) -> typing.Union[MetaOapg.properties.specialIssue, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["articleNumber"]) -> typing.Union[MetaOapg.properties.articleNumber, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["pages"]) -> typing.Union[MetaOapg.properties.pages, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sourceTitle", "publishYear", "publishMonth", "volume", "issue", "supplement", "specialIssue", "articleNumber", "pages", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    sourceTitle: typing.Union[MetaOapg.properties.sourceTitle, str, schemas.Unset] = schemas.unset,
                    publishYear: typing.Union[MetaOapg.properties.publishYear, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    publishMonth: typing.Union[MetaOapg.properties.publishMonth, str, schemas.Unset] = schemas.unset,
                    volume: typing.Union[MetaOapg.properties.volume, str, schemas.Unset] = schemas.unset,
                    issue: typing.Union[MetaOapg.properties.issue, str, schemas.Unset] = schemas.unset,
                    supplement: typing.Union[MetaOapg.properties.supplement, str, schemas.Unset] = schemas.unset,
                    specialIssue: typing.Union[MetaOapg.properties.specialIssue, str, schemas.Unset] = schemas.unset,
                    articleNumber: typing.Union[MetaOapg.properties.articleNumber, str, schemas.Unset] = schemas.unset,
                    pages: typing.Union[MetaOapg.properties.pages, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'source':
                    return super().__new__(
                        cls,
                        *_args,
                        sourceTitle=sourceTitle,
                        publishYear=publishYear,
                        publishMonth=publishMonth,
                        volume=volume,
                        issue=issue,
                        supplement=supplement,
                        specialIssue=specialIssue,
                        articleNumber=articleNumber,
                        pages=pages,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class names(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class authors(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['AuthorName']:
                                    return AuthorName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['AuthorName'], typing.List['AuthorName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'authors':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'AuthorName':
                                return super().__getitem__(i)
                        
                        
                        class inventors(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'inventors':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        
                        
                        class bookCorp(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'bookCorp':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        
                        
                        class bookEditors(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'bookEditors':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        
                        
                        class books(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'books':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        
                        
                        class additionalAuthors(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'additionalAuthors':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        
                        
                        class anonymous(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'anonymous':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        
                        
                        class assignees(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'assignees':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        
                        
                        class corp(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'corp':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        
                        
                        class editors(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'editors':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        
                        
                        class investigators(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'investigators':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        
                        
                        class sponsors(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'sponsors':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        
                        
                        class issuingOrganizations(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['OtherName']:
                                    return OtherName
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['OtherName'], typing.List['OtherName']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'issuingOrganizations':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'OtherName':
                                return super().__getitem__(i)
                        __annotations__ = {
                            "authors": authors,
                            "inventors": inventors,
                            "bookCorp": bookCorp,
                            "bookEditors": bookEditors,
                            "books": books,
                            "additionalAuthors": additionalAuthors,
                            "anonymous": anonymous,
                            "assignees": assignees,
                            "corp": corp,
                            "editors": editors,
                            "investigators": investigators,
                            "sponsors": sponsors,
                            "issuingOrganizations": issuingOrganizations,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["authors"]) -> MetaOapg.properties.authors: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["inventors"]) -> MetaOapg.properties.inventors: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["bookCorp"]) -> MetaOapg.properties.bookCorp: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["bookEditors"]) -> MetaOapg.properties.bookEditors: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["books"]) -> MetaOapg.properties.books: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["additionalAuthors"]) -> MetaOapg.properties.additionalAuthors: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["anonymous"]) -> MetaOapg.properties.anonymous: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["assignees"]) -> MetaOapg.properties.assignees: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["corp"]) -> MetaOapg.properties.corp: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["editors"]) -> MetaOapg.properties.editors: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["investigators"]) -> MetaOapg.properties.investigators: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["sponsors"]) -> MetaOapg.properties.sponsors: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["issuingOrganizations"]) -> MetaOapg.properties.issuingOrganizations: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["authors", "inventors", "bookCorp", "bookEditors", "books", "additionalAuthors", "anonymous", "assignees", "corp", "editors", "investigators", "sponsors", "issuingOrganizations", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["authors"]) -> typing.Union[MetaOapg.properties.authors, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["inventors"]) -> typing.Union[MetaOapg.properties.inventors, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["bookCorp"]) -> typing.Union[MetaOapg.properties.bookCorp, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["bookEditors"]) -> typing.Union[MetaOapg.properties.bookEditors, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["books"]) -> typing.Union[MetaOapg.properties.books, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["additionalAuthors"]) -> typing.Union[MetaOapg.properties.additionalAuthors, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["anonymous"]) -> typing.Union[MetaOapg.properties.anonymous, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["assignees"]) -> typing.Union[MetaOapg.properties.assignees, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["corp"]) -> typing.Union[MetaOapg.properties.corp, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["editors"]) -> typing.Union[MetaOapg.properties.editors, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["investigators"]) -> typing.Union[MetaOapg.properties.investigators, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sponsors"]) -> typing.Union[MetaOapg.properties.sponsors, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["issuingOrganizations"]) -> typing.Union[MetaOapg.properties.issuingOrganizations, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authors", "inventors", "bookCorp", "bookEditors", "books", "additionalAuthors", "anonymous", "assignees", "corp", "editors", "investigators", "sponsors", "issuingOrganizations", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    authors: typing.Union[MetaOapg.properties.authors, list, tuple, schemas.Unset] = schemas.unset,
                    inventors: typing.Union[MetaOapg.properties.inventors, list, tuple, schemas.Unset] = schemas.unset,
                    bookCorp: typing.Union[MetaOapg.properties.bookCorp, list, tuple, schemas.Unset] = schemas.unset,
                    bookEditors: typing.Union[MetaOapg.properties.bookEditors, list, tuple, schemas.Unset] = schemas.unset,
                    books: typing.Union[MetaOapg.properties.books, list, tuple, schemas.Unset] = schemas.unset,
                    additionalAuthors: typing.Union[MetaOapg.properties.additionalAuthors, list, tuple, schemas.Unset] = schemas.unset,
                    anonymous: typing.Union[MetaOapg.properties.anonymous, list, tuple, schemas.Unset] = schemas.unset,
                    assignees: typing.Union[MetaOapg.properties.assignees, list, tuple, schemas.Unset] = schemas.unset,
                    corp: typing.Union[MetaOapg.properties.corp, list, tuple, schemas.Unset] = schemas.unset,
                    editors: typing.Union[MetaOapg.properties.editors, list, tuple, schemas.Unset] = schemas.unset,
                    investigators: typing.Union[MetaOapg.properties.investigators, list, tuple, schemas.Unset] = schemas.unset,
                    sponsors: typing.Union[MetaOapg.properties.sponsors, list, tuple, schemas.Unset] = schemas.unset,
                    issuingOrganizations: typing.Union[MetaOapg.properties.issuingOrganizations, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'names':
                    return super().__new__(
                        cls,
                        *_args,
                        authors=authors,
                        inventors=inventors,
                        bookCorp=bookCorp,
                        bookEditors=bookEditors,
                        books=books,
                        additionalAuthors=additionalAuthors,
                        anonymous=anonymous,
                        assignees=assignees,
                        corp=corp,
                        editors=editors,
                        investigators=investigators,
                        sponsors=sponsors,
                        issuingOrganizations=issuingOrganizations,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class links(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        record = schemas.StrSchema
                        citingArticles = schemas.StrSchema
                        references = schemas.StrSchema
                        related = schemas.StrSchema
                        __annotations__ = {
                            "record": record,
                            "citingArticles": citingArticles,
                            "references": references,
                            "related": related,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["record"]) -> MetaOapg.properties.record: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["citingArticles"]) -> MetaOapg.properties.citingArticles: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["references"]) -> MetaOapg.properties.references: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["related"]) -> MetaOapg.properties.related: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["record", "citingArticles", "references", "related", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["record"]) -> typing.Union[MetaOapg.properties.record, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["citingArticles"]) -> typing.Union[MetaOapg.properties.citingArticles, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["references"]) -> typing.Union[MetaOapg.properties.references, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["related"]) -> typing.Union[MetaOapg.properties.related, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["record", "citingArticles", "references", "related", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    record: typing.Union[MetaOapg.properties.record, str, schemas.Unset] = schemas.unset,
                    citingArticles: typing.Union[MetaOapg.properties.citingArticles, str, schemas.Unset] = schemas.unset,
                    references: typing.Union[MetaOapg.properties.references, str, schemas.Unset] = schemas.unset,
                    related: typing.Union[MetaOapg.properties.related, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'links':
                    return super().__new__(
                        cls,
                        *_args,
                        record=record,
                        citingArticles=citingArticles,
                        references=references,
                        related=related,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class citations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                db = schemas.StrSchema
                                count = schemas.Int32Schema
                                __annotations__ = {
                                    "db": db,
                                    "count": count,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["db"]) -> MetaOapg.properties.db: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["db", "count", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["db"]) -> typing.Union[MetaOapg.properties.db, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["db", "count", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            db: typing.Union[MetaOapg.properties.db, str, schemas.Unset] = schemas.unset,
                            count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                db=db,
                                count=count,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'citations':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class identifiers(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        doi = schemas.StrSchema
                        issn = schemas.StrSchema
                        eissn = schemas.StrSchema
                        isbn = schemas.StrSchema
                        eisbn = schemas.StrSchema
                        pmid = schemas.StrSchema
                        __annotations__ = {
                            "doi": doi,
                            "issn": issn,
                            "eissn": eissn,
                            "isbn": isbn,
                            "eisbn": eisbn,
                            "pmid": pmid,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["doi"]) -> MetaOapg.properties.doi: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["issn"]) -> MetaOapg.properties.issn: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["eissn"]) -> MetaOapg.properties.eissn: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["isbn"]) -> MetaOapg.properties.isbn: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["eisbn"]) -> MetaOapg.properties.eisbn: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["pmid"]) -> MetaOapg.properties.pmid: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["doi", "issn", "eissn", "isbn", "eisbn", "pmid", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["doi"]) -> typing.Union[MetaOapg.properties.doi, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["issn"]) -> typing.Union[MetaOapg.properties.issn, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["eissn"]) -> typing.Union[MetaOapg.properties.eissn, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["isbn"]) -> typing.Union[MetaOapg.properties.isbn, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["eisbn"]) -> typing.Union[MetaOapg.properties.eisbn, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["pmid"]) -> typing.Union[MetaOapg.properties.pmid, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["doi", "issn", "eissn", "isbn", "eisbn", "pmid", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    doi: typing.Union[MetaOapg.properties.doi, str, schemas.Unset] = schemas.unset,
                    issn: typing.Union[MetaOapg.properties.issn, str, schemas.Unset] = schemas.unset,
                    eissn: typing.Union[MetaOapg.properties.eissn, str, schemas.Unset] = schemas.unset,
                    isbn: typing.Union[MetaOapg.properties.isbn, str, schemas.Unset] = schemas.unset,
                    eisbn: typing.Union[MetaOapg.properties.eisbn, str, schemas.Unset] = schemas.unset,
                    pmid: typing.Union[MetaOapg.properties.pmid, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'identifiers':
                    return super().__new__(
                        cls,
                        *_args,
                        doi=doi,
                        issn=issn,
                        eissn=eissn,
                        isbn=isbn,
                        eisbn=eisbn,
                        pmid=pmid,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class keywords(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class authorKeywords(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.StrSchema
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'authorKeywords':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "authorKeywords": authorKeywords,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["authorKeywords"]) -> MetaOapg.properties.authorKeywords: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["authorKeywords", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["authorKeywords"]) -> typing.Union[MetaOapg.properties.authorKeywords, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authorKeywords", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    authorKeywords: typing.Union[MetaOapg.properties.authorKeywords, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'keywords':
                    return super().__new__(
                        cls,
                        *_args,
                        authorKeywords=authorKeywords,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "uid": uid,
                "title": title,
                "types": types,
                "sourceTypes": sourceTypes,
                "source": source,
                "names": names,
                "links": links,
                "citations": citations,
                "identifiers": identifiers,
                "keywords": keywords,
            }
    
    uid: MetaOapg.properties.uid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uid"]) -> MetaOapg.properties.uid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["types"]) -> MetaOapg.properties.types: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceTypes"]) -> MetaOapg.properties.sourceTypes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["names"]) -> MetaOapg.properties.names: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["citations"]) -> MetaOapg.properties.citations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identifiers"]) -> MetaOapg.properties.identifiers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keywords"]) -> MetaOapg.properties.keywords: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uid", "title", "types", "sourceTypes", "source", "names", "links", "citations", "identifiers", "keywords", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uid"]) -> MetaOapg.properties.uid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["types"]) -> typing.Union[MetaOapg.properties.types, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceTypes"]) -> typing.Union[MetaOapg.properties.sourceTypes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["names"]) -> typing.Union[MetaOapg.properties.names, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["citations"]) -> typing.Union[MetaOapg.properties.citations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identifiers"]) -> typing.Union[MetaOapg.properties.identifiers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keywords"]) -> typing.Union[MetaOapg.properties.keywords, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uid", "title", "types", "sourceTypes", "source", "names", "links", "citations", "identifiers", "keywords", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        uid: typing.Union[MetaOapg.properties.uid, str, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        types: typing.Union[MetaOapg.properties.types, list, tuple, schemas.Unset] = schemas.unset,
        sourceTypes: typing.Union[MetaOapg.properties.sourceTypes, list, tuple, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        names: typing.Union[MetaOapg.properties.names, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        citations: typing.Union[MetaOapg.properties.citations, list, tuple, schemas.Unset] = schemas.unset,
        identifiers: typing.Union[MetaOapg.properties.identifiers, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        keywords: typing.Union[MetaOapg.properties.keywords, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Document':
        return super().__new__(
            cls,
            *_args,
            uid=uid,
            title=title,
            types=types,
            sourceTypes=sourceTypes,
            source=source,
            names=names,
            links=links,
            citations=citations,
            identifiers=identifiers,
            keywords=keywords,
            _configuration=_configuration,
            **kwargs,
        )

from clarivate.wos_starter.client.model.author_name import AuthorName
from clarivate.wos_starter.client.model.other_name import OtherName
