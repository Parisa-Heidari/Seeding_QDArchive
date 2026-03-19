import csv
import os

from src.collection.dryad_api import fetch_dryad_metadata
from src.collection.cessda_scraper import fetch_cessda_metadata
from src.processing.schema import METADATA_FIELDS


def merge_metadata(dryad_records, cessda_records):
    return dryad_records + cessda_records


def save_to_csv(records, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=METADATA_FIELDS)
        writer.writeheader()

        for record in records:
            row = record.copy()
            row["authors"] = ", ".join(row["authors"])
            row["keywords"] = ", ".join(row["keywords"])
            row["subjects"] = ", ".join(row["subjects"])
            writer.writerow(row)


if __name__ == "__main__":
    dryad_data = fetch_dryad_metadata(limit=5)
    cessda_data = fetch_cessda_metadata(limit=5)

    combined = merge_metadata(dryad_data, cessda_data)
    save_to_csv(combined, "data/processed/combined_metadata.csv")

    print(f"Saved {len(combined)} records to data/processed/combined_metadata.csv")