import json
from itertools import permutations

def generate_permutations_from_string(element_string):
    """
    Generate all permutations for a comma-separated string of elements.
    For "Fe,Mg", generates: ["Fe,Mg", "Mg,Fe"]
    For "A,B,C", generates: ["A,B,C", "A,C,B", "B,A,C", "B,C,A", "C,A,B", "C,B,A"]
    """
    # Split the string by comma to get individual elements
    elements = element_string.split(',')
    
    # If only one element, return original string in a list
    if len(elements) == 1:
        return [element_string]
    
    # Generate all permutations and join them back with commas
    perms = []
    for perm in permutations(elements):
        perms.append(','.join(perm))
    
    return perms

def transform_element_field(data):
    """
    Transform el_inc and el_exc fields by generating all permutations
    for comma-separated element strings.
    Example: ["Mg,Na"] -> ["Mg,Na", "Na,Mg"]
    """
    if isinstance(data, dict):
        for key, value in data.items():
            # Check if this is el_inc or el_exc field
            if key in ["el_inc", "el_exc"] and isinstance(value, list):
                transformed = []
                for item in value:
                    if isinstance(item, str) and ',' in item:
                        # Generate all permutations for this comma-separated string
                        permutations_list = generate_permutations_from_string(item)
                        transformed.extend(permutations_list)
                    else:
                        # Keep single element strings as is
                        transformed.append(item)
                data[key] = transformed
            elif isinstance(value, (dict, list)):
                # Recursively process nested structures
                transform_element_field(value)
    elif isinstance(data, list):
        for item in data:
            transform_element_field(item)
    
    return data

def process_jsonl_file(input_file, output_file):
    """
    Process JSONL file and transform el_inc and el_exc fields
    """
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        line_count = 0
        for line in infile:
            # Skip empty lines
            if not line.strip():
                continue
            
            # Parse JSON line
            data = json.loads(line)
            
            # Transform el_inc and el_exc fields
            transformed_data = transform_element_field(data)
            
            # Write transformed data to output file
            outfile.write(json.dumps(transformed_data, ensure_ascii=False) + '\n')
            line_count += 1
        
        print(f"Processed {line_count} lines")

# Main execution
if __name__ == "__main__":
    input_filename = "berkeley-function-call-leaderboard/bfcl_eval/groundtruth_data/sorted_groundtruth_weilin.jsonl"
    output_filename = "berkeley-function-call-leaderboard/bfcl_eval/groundtruth_data/sorted_groundtruth_weilin_elnorm.jsonl"
    
    print("Starting transformation...")
    process_jsonl_file(input_filename, output_filename)
    print(f"Transformation complete! Output saved to {output_filename}")