from datetime import date


def empty_record():
    return {
        "source": "",
        "dataset_id": "",
        "title": "",
        "abstract": "",
        "authors": [],
        "year": "",
        "publisher": "",
        "keywords": [],
        "subjects": [],
        "language": "",
        "country": "",
        "doi": "",
        "url": "",
        "collection_date": str(date.today()),
    }
