import pandas as pd
import os

def load_and_clean_dataset(file_path):
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
        df = df.dropna(subset=['questionText', 'answerText', 'category', 'marathi_question', 'marathi_answer'])
        df = df[df['questionText'].str.strip() != '']
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_english_dataset(df):
    english_df = df[['questionText', 'answerText', 'category']]
    english_df.to_csv('data/english_dataset.csv', index=False, encoding='utf-8')
    print("Saved data/english_dataset.csv")

def create_marathi_dataset(df):
    marathi_df = df[['marathi_question', 'marathi_answer', 'category']]
    marathi_df.to_csv('data/marathi_dataset.csv', index=False, encoding='utf-8')
    print("Saved data/marathi_dataset.csv")

def main():
    df = load_and_clean_dataset('data/Translated_dataset.csv')
    if df is not None:
        create_english_dataset(df)
        create_marathi_dataset(df)
    else:
        print("Failed to process dataset.")

if __name__ == "__main__":
    main()
