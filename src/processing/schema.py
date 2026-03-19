from typing import TypedDict, List


METADATA_FIELDS = [
    "source",
    "dataset_id",
    "title",
    "abstract",
    "authors",
    "year",
    "publisher",
    "keywords",
    "subjects",
    "language",
    "country",
    "doi",
    "url",
    "collection_date",
]


class DatasetMetadata(TypedDict):
    source: str
    dataset_id: str
    title: str
    abstract: str
    authors: List[str]
    year: str
    publisher: str
    keywords: List[str]
    subjects: List[str]
    language: str
    country: str
    doi: str
    url: str
    collection_date: str
