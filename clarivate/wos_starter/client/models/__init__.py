# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from clarivate.wos_starter.client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from clarivate.wos_starter.client.model.author_name import AuthorName
from clarivate.wos_starter.client.model.document import Document
from clarivate.wos_starter.client.model.documents_list import DocumentsList
from clarivate.wos_starter.client.model.journal import Journal
from clarivate.wos_starter.client.model.journals_list import JournalsList
from clarivate.wos_starter.client.model.metadata import Metadata
from clarivate.wos_starter.client.model.other_name import OtherName
