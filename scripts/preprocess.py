import pandas as pd

# Step 1: Load the CSV file
file_path = "../data/your_dataset.csv"  # Update path if needed
df = pd.read_csv(file_path)

# Step 2: Strip extra spaces from column names
df.columns = df.columns.str.strip()
print("Columns after strip:", df.columns)

# Step 3: Select only the required columns
df = df[['Sentence', 'Label']]

# Step 4: Rename columns to something consistent
df.columns = ['feedback_text', 'sentiment']

# Step 5: Optional - remove empty rows
df.dropna(inplace=True)

# Step 6: Optional - reset index
df.reset_index(drop=True, inplace=True)

# Step 7: Save cleaned dataset to a new CSV
output_path = "../data/feedback_dataset_clean.csv"
df.to_csv(output_path, index=False)

print(f"Preprocessed CSV saved at: {output_path}")
print(df.head())
