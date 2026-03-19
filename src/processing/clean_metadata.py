import csv
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, "data", "processed", "combined_metadata.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "processed", "cleaned_metadata.csv")


def clean_text(value):
    if value is None:
        return ""
    return str(value).strip()


def clean_year(value):
    value = clean_text(value)
    if len(value) >= 4 and value[:4].isdigit():
        return value[:4]
    return ""


def clean_row(row):
    row["source"] = clean_text(row.get("source", "")).lower()
    row["dataset_id"] = clean_text(row.get("dataset_id", ""))
    row["title"] = clean_text(row.get("title", ""))
    row["abstract"] = clean_text(row.get("abstract", ""))
    row["authors"] = clean_text(row.get("authors", ""))
    row["year"] = clean_year(row.get("year", ""))
    row["publisher"] = clean_text(row.get("publisher", ""))
    row["keywords"] = clean_text(row.get("keywords", ""))
    row["subjects"] = clean_text(row.get("subjects", ""))
    row["language"] = clean_text(row.get("language", ""))
    row["country"] = clean_text(row.get("country", ""))
    row["doi"] = clean_text(row.get("doi", ""))
    row["url"] = clean_text(row.get("url", ""))
    row["collection_date"] = clean_text(row.get("collection_date", ""))

    return row


def remove_duplicates(rows):
    seen = set()
    unique_rows = []

    for row in rows:
        key = (row["source"], row["dataset_id"], row["title"])
        if key not in seen:
            seen.add(key)
            unique_rows.append(row)

    return unique_rows


def clean_metadata():
    rows = []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(clean_row(row))

    rows = remove_duplicates(rows)

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved cleaned data to: {OUTPUT_FILE}")
    print(f"Number of rows: {len(rows)}")


if __name__ == "__main__":
    clean_metadata()