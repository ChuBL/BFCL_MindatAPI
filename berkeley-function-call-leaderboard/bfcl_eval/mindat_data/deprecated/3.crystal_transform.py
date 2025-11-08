import json
import sys

def transform_crystal_system(data):
    """
    Transform crystal_system field: if it has only one string value, 
    convert it from ["value"] to ["value", ["value"]]
    Keep unchanged if:
    - It already has multiple values (e.g., ["A", "B"])
    - The first element is a list (e.g., [["A", "B"]])
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "crystal_system":
                # Check if it's a list with exactly one element AND that element is a string
                if isinstance(value, list) and len(value) == 1 and isinstance(value[0], str):
                    # Transform to ["value", ["value"]]
                    data[key] = [value[0], [value[0]]]
                # If the first element is a list (e.g., [["A", "B"]]), keep unchanged
                # If it has multiple string values (e.g., ["A", "B"]), keep unchanged
            else:
                # Recursively process nested structures
                transform_crystal_system(value)
    elif isinstance(data, list):
        for item in data:
            transform_crystal_system(item)
    
    return data

def process_jsonl_file(input_file, output_file):
    """
    Process JSONL file line by line
    """
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        for line_num, line in enumerate(infile, 1):
            line = line.strip()
            if not line:
                continue
            
            try:
                # Parse JSON
                data = json.loads(line)
                
                # Transform the data
                transformed_data = transform_crystal_system(data)
                
                # Write to output file
                outfile.write(json.dumps(transformed_data, ensure_ascii=False) + '\n')
                
                print(f"Processed line {line_num}")
                
            except json.JSONDecodeError as e:
                print(f"Error parsing line {line_num}: {e}")
                continue

if __name__ == "__main__":
    
    input_file = "berkeley-function-call-leaderboard/bfcl_eval/test/weilin/fin/sorted_groundtruth_weilin.jsonl"
    output_file = "berkeley-function-call-leaderboard/bfcl_eval/test/weilin/fin/sorted_groundtruth_weilin_crynorm.jsonl"
    
    print(f"Processing {input_file}...")
    process_jsonl_file(input_file, output_file)
    print(f"Done! Output saved to {output_file}")