##  Student
23263054

##  Assigned Repositories
- Repo 13 – CESSDA  
- Repo 2 – Dryad  

---

##  Project Goal
Build an automated data pipeline to:
- collect qualitative research datasets  
- store and standardize metadata  
- classify datasets using ISIC categories  
- prepare data for analysis  

---

##  Deadline
**Classification phase completed by April 15**

---

##  Classification Phase

###  Data Sources

This project collects qualitative research datasets from:

- **Dryad**  
  - Accessed via a public API  
  - Provides real dataset metadata  

- **CESSDA**  
  - Currently simulated using structured sample data  
  - Ensures pipeline consistency  
  - Will be replaced with real integration in future work  

---

###  Data Collection

Metadata collection is implemented in: src/collection/

- `dryad_api.py` → retrieves real data from Dryad API  
- `cessda_scraper.py` → generates structured sample data  

All datasets are converted into a **common metadata schema**.

---

###  Data Processing

The processing pipeline includes the following steps:

#### 1. Merge Metadata
- Combines Dryad and CESSDA datasets  
- Script: `merge_metadata.py`  
- Output:data/processed/combined_metadata.csv
- 
#### 2. Clean Metadata
- Removes extra spaces  
- Standardizes fields  
- Fixes year format  
- Removes duplicates  
- Script: `clean_metadata.py`  
- Output: data/processed/cleaned_metadata.csv
- 
#### 3. Prepare Classification Input
- Combines text fields into a single input field  
- Fields used:
  - title  
  - abstract  
  - keywords  
  - subjects  
- Script: `prepare_classification_input.py`  
- Output:data/processed/classification_input.csv
- 
---

###  Classification Method

A **rule-based keyword matching approach** is used.

- Each ISIC category is associated with keywords  
- The dataset text is scanned for matches  
- The first matching category is assigned  

#### Example categories:
- Agriculture, forestry and fishing  
- Education  
- Human health and social work activities  
- Information and communication  
- Arts, entertainment and recreation  
- Public administration and defence  

If no keywords match, the dataset is classified as:
Other service activities

Classification logic is implemented in:

src/classification/isic_classifier.py

---

###  Output

Final classified dataset: data/final/classified_metadata.csv


Each record includes:
- original metadata  
- processed classification text  
- assigned ISIC category  

---

###  Pipeline Overview
Collection → Processing → Preparation → Classification → Output


---

###  Future Work

- Integrate real CESSDA API or scraping solution  
- Improve classification accuracy  
- Explore machine learning-based classification  
- Perform detailed analysis and visualization  

