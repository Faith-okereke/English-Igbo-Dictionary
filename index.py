import csv
import json

input_file = "english-igbo-dictionary.csv"
output_data = []
seen_terms = set()

with open(input_file, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f) 
    
    for row in reader:
        if  row["en"].strip().lower() in seen_terms:
                    continue
        if row["en"] and row["ig"]:
                    pair = { 
                        "english": row["en"].strip(),
                        "igbo": row["ig"].strip()
                    }
                    output_data.append(pair)
                    seen_terms.add(row["en"].strip().lower())

##This block of code converts the CSV dictionary pair words into a clean JSON format
with open("clean_igbo_english_dictionary.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4, ensure_ascii=False)