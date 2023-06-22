import typing_extensions

from clarivate.wos_starter.client.apis.tags import TagValues
from clarivate.wos_starter.client.apis.tags.documents_api import DocumentsApi
from clarivate.wos_starter.client.apis.tags.journals_api import JournalsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.JOURNALS: JournalsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.JOURNALS: JournalsApi,
    }
)
