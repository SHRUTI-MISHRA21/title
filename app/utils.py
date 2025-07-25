def read_pdf_files(input_dir):
    """Read all PDF files from the specified input directory."""
    import os
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
    return [os.path.join(input_dir, f) for f in pdf_files]

def write_json_output(output_dir, filename, data):
    """Write the analysis results to a JSON file in the output directory."""
    import json
    import os

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, f"{filename}.json")
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file)