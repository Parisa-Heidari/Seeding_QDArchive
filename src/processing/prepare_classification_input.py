import csv
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, "data", "processed", "cleaned_metadata.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "processed", "classification_input.csv")


def clean_piece(value):
    if value is None:
        return ""
    return str(value).strip()


def build_classification_text(row):
    parts = [
        clean_piece(row.get("title", "")),
        clean_piece(row.get("abstract", "")),
        clean_piece(row.get("keywords", "")),
        clean_piece(row.get("subjects", "")),
    ]

    parts = [part for part in parts if part]
    return " | ".join(parts)


def prepare_classification_input():
    rows = []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["classification_text"] = build_classification_text(row)
            rows.append(row)

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = list(rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved classification input to: {OUTPUT_FILE}")
    print(f"Number of rows: {len(rows)}")


if __name__ == "__main__":
    prepare_classification_input()