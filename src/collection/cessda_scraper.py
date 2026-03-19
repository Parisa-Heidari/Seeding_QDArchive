from src.processing.utils import empty_record


def fetch_cessda_metadata(limit=5):
    records = []

    for i in range(limit):
        record = empty_record()
        record["source"] = "cessda"
        record["dataset_id"] = f"cessda_{i+1}"
        record["title"] = f"Sample CESSDA Dataset {i+1}"
        record["abstract"] = "Sample abstract from CESSDA."
        record["authors"] = ["Researcher X"]
        record["year"] = "2023"
        record["publisher"] = "CESSDA"
        record["keywords"] = ["interviews", "archive"]
        record["subjects"] = ["qualitative studies"]
        record["language"] = "English"
        record["country"] = ""
        record["doi"] = ""
        record["url"] = "https://www.cessda.eu/"
        records.append(record)

    return records


if __name__ == "__main__":
    data = fetch_cessda_metadata(limit=3)
    print("Number of records:", len(data))
    for item in data:
        print(item)