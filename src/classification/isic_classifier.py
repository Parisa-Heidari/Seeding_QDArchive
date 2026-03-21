import csv
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, "data", "processed", "classification_input.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "final", "classified_metadata.csv")


ISIC_RULES = {
    "Agriculture, forestry and fishing": [
        "agriculture", "farming", "crop", "livestock", "fishery", "fishing", "forestry"
    ],
    "Education": [
        "education", "school", "student", "teacher", "learning", "university"
    ],
    "Human health and social work activities": [
        "health", "hospital", "medical", "nursing", "patient", "care", "social work"
    ],
    "Information and communication": [
        "information", "communication", "media", "digital", "internet", "technology"
    ],
    "Arts, entertainment and recreation": [
        "art", "music", "entertainment", "culture", "recreation", "festival"
    ],
    "Public administration and defence": [
        "government", "policy", "public administration", "defence", "municipal"
    ],
    "Other service activities": []
}


def classify_text(text):
    text = text.lower()

    for category, keywords in ISIC_RULES.items():
        for keyword in keywords:
            if keyword in text:
                return category

    return "Other service activities"


def classify_metadata():
    rows = []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            classification_text = row.get("classification_text", "")
            row["isic_category"] = classify_text(classification_text)
            rows.append(row)

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = list(rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved classified data to: {OUTPUT_FILE}")
    print(f"Number of rows: {len(rows)}")


if __name__ == "__main__":
    classify_metadata()