# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from clarivate.wos_starter.client.paths.documents_uid import Api

from clarivate.wos_starter.client.paths import PathValues

path = PathValues.DOCUMENTS_UID