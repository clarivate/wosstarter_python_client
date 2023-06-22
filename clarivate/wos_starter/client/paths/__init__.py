# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from clarivate.wos_starter.client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    JOURNALS = "/journals"
    JOURNALS_ID = "/journals/{id}"
    DOCUMENTS = "/documents"
    DOCUMENTS_UID = "/documents/{uid}"
