import json

# Read the JSONL file
input_file = 'berkeley-function-call-leaderboard/bfcl_eval/groundtruth_data/raw_groundtruth_weilin_fixed.jsonl'
output_file = 'berkeley-function-call-leaderboard/bfcl_eval/groundtruth_data/sorted_groundtruth_weilin.jsonl'

# Read all lines and parse JSON
data_list = []
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():  # Skip empty lines
            data_list.append(json.loads(line))

# Sort by ID in ascending order
# Extract numeric part from ID (e.g., "Mindat_v1_112" -> 112)
data_list.sort(key=lambda x: int(x['id'].split('_')[-1]))

# Write sorted data to output file
with open(output_file, 'w', encoding='utf-8') as f:
    for item in data_list:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f"Sorting complete! Sorted data saved to {output_file}")
print(f"Total records: {len(data_list)}")