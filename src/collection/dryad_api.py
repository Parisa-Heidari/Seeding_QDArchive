import requests
from src.processing.utils import empty_record


DRYAD_API_URL = "https://datadryad.org/api/v2/datasets"


def fetch_dryad_metadata(limit=5):
    records = []
    params = {
        "page[size]": limit
    }

    response = requests.get(DRYAD_API_URL, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()
    items = data.get("_embedded", {}).get("stash:datasets", [])

    for item in items:
        record = empty_record()
        record["source"] = "dryad"
        record["dataset_id"] = str(item.get("id", ""))
        record["title"] = item.get("title", "")
        record["abstract"] = item.get("abstract", "")
        record["authors"] = extract_authors(item)
        record["year"] = extract_year(item)
        record["publisher"] = "Dryad"
        record["keywords"] = item.get("keywords", []) if isinstance(item.get("keywords", []), list) else []
        record["subjects"] = []
        record["language"] = ""
        record["country"] = ""
        record["doi"] = item.get("identifier", "")
        record["url"] = extract_url(item)

        records.append(record)

    return records

def extract_authors(item):
    authors = []
    embedded = item.get("_embedded", {})
    authors_data = embedded.get("stash:authors", [])
    for author in authors_data:
        name = author.get("name", "")
        if name:
            authors.append(name)
    return authors

def extract_year(item):
    publication_date = item.get("publicationDate", "")
    if publication_date and len(publication_date) >= 4:
        return publication_date[:4]
    return ""

def extract_url(item):
    links = item.get("_links", {})
    self_link = links.get("stash:version", {}).get("href", "")
    return self_link

if __name__ == "__main__":
    data = fetch_dryad_metadata(limit=3)
    for item in data:
        print(item)
