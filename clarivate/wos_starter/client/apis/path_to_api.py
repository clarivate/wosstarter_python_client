import typing_extensions

from clarivate.wos_starter.client.paths import PathValues
from clarivate.wos_starter.client.apis.paths.journals import Journals
from clarivate.wos_starter.client.apis.paths.journals_id import JournalsId
from clarivate.wos_starter.client.apis.paths.documents import Documents
from clarivate.wos_starter.client.apis.paths.documents_uid import DocumentsUid

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.JOURNALS: Journals,
        PathValues.JOURNALS_ID: JournalsId,
        PathValues.DOCUMENTS: Documents,
        PathValues.DOCUMENTS_UID: DocumentsUid,
    }
)

path_to_api = PathToApi(
    {
        PathValues.JOURNALS: Journals,
        PathValues.JOURNALS_ID: JournalsId,
        PathValues.DOCUMENTS: Documents,
        PathValues.DOCUMENTS_UID: DocumentsUid,
    }
)
