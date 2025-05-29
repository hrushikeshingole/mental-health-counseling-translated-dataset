Mental Health Counseling Dataset (English and Marathi)
Overview
This dataset contains mental health counseling questions and answers in both English and Marathi. It is derived from the open-source Counsel Chat dataset, which originally contained English-language question-answer pairs from mental health counseling sessions. The dataset has been extended by translating the questions and answers into Marathi using a combination of Google Translate API and manual translation to ensure accuracy and cultural relevance.
The dataset is split into two separate files:

english_dataset.csv: Contains questions and answers in English, along with their associated categories.
marathi_dataset.csv: Contains questions and answers in Marathi, along with their associated categories.

This dataset is intended for researchers, developers, and mental health professionals interested in building or analyzing mental health counseling tools, especially for bilingual applications targeting English and Marathi speakers.
Dataset Description
Source
The original data comes from the Counsel Chat dataset, an open-source collection of mental health counseling Q&A pairs. The dataset was translated into Marathi to make it accessible to Marathi-speaking communities.
Translation Process

Automated Translation: Initial translations were performed using the Google Translate API to convert English questions and answers into Marathi.
Manual Refinement: The automated translations were reviewed and corrected by native Marathi speakers to ensure linguistic accuracy, cultural sensitivity, and contextual appropriateness.
Validation: The final translations were validated to maintain consistency with the original English content while ensuring the Marathi translations are natural and meaningful.

Structure
The dataset is provided in CSV format with the following columns:

Full Dataset (Translated_dataset.csv):

questionText: The question asked in English.
answerText: The counselor's response in English.
category: The mental health category (e.g., Depression, Addiction, Stress).
marathi_question: The question translated into Marathi.
marathi_answer: The counselor's response translated into Marathi.


English Dataset (english_dataset.csv):

questionText: The question asked in English.
answerText: The counselor's response in English.
category: The mental health category.


Marathi Dataset (marathi_dataset.csv):

marathi_question: The question in Marathi.
marathi_answer: The counselor's response in Marathi.
category: The mental health category.



Categories
The dataset includes the following mental health categories:

Depression
Addiction
Stress
(Additional categories may be present based on the original Counsel Chat dataset)

File Details

Format: CSV (Comma-Separated Values)
Encoding: UTF-8 (to support Marathi characters)
Size: Varies based on the number of entries (refer to the dataset files for exact counts)
License: CC BY-SA 4.0 (inherited from the original Counsel Chat dataset)

Usage
This dataset can be used for various purposes, including:

Natural Language Processing (NLP): Training chatbots or question-answering models for mental health counseling in English and Marathi.
Mental Health Research: Analyzing common mental health concerns and counselor responses in bilingual contexts.
Educational Tools: Developing applications or resources for mental health education in English and Marathi-speaking communities.

Example Usage
To load and process the dataset in Python:
import pandas as pd

# Load English dataset
english_df = pd.read_csv('english_dataset.csv')
print(english_df.head())

# Load Marathi dataset
marathi_df = pd.read_csv('marathi_dataset.csv')
print(marathi_df.head())

Prerequisites

Python 3.x
Libraries: pandas for data manipulation
UTF-8 compatible text editor or IDE for handling Marathi text

Installation

Clone the repository:git clone https://github.com/your-username/mental-health-counseling-dataset.git


Navigate to the dataset directory:cd mental-health-counseling-dataset


Install required Python libraries:pip install pandas



Splitting the Dataset
The original Translated_dataset.csv can be split into English and Marathi datasets using the provided Python script (split_dataset.py). See the "Scripts" section for details.
Scripts
A Python script (split_dataset.py) is included to split the full dataset into English and Marathi subsets. The script reads Translated_dataset.csv and generates:

english_dataset.csv
marathi_dataset.csv

Run the script as follows:
python split_dataset.py

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes (e.g., add new translations, improve documentation, or enhance scripts).
Commit your changes (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Create a pull request.

Please ensure that:

Translations are accurate and culturally appropriate.
Code follows PEP 8 style guidelines.
Changes are tested before submission.

License
This dataset is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0). You are free to share and adapt the dataset, provided you give appropriate credit and distribute any derivative works under the same license.
Contact
For questions or feedback, please open an issue on the GitHub repository or contact [your-email@example.com].
Acknowledgments

The original Counsel Chat dataset for providing the English Q&A pairs.
Google Translate API for facilitating initial translations.
Native Marathi speakers for manual translation and validation.


