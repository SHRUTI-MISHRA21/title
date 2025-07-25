import os
import json
import logging
from pdf_analyzer import PDFAnalyzer

def process_pdfs(input_folder: str, output_folder: str):
    analyzer = PDFAnalyzer()
    
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each PDF file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            logging.info(f"Processing PDF: {pdf_path}")
            
            try:
                analysis_result = analyzer.analyze_pdf(pdf_path)
                
                if analysis_result:
                    output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.json")
                    with open(output_file_path, 'w') as json_file:
                        json.dump(analysis_result, json_file)
                    logging.info(f"Saved analysis result to: {output_file_path}")
                else:
                    logging.warning(f"No analysis result for: {pdf_path}")
                    
            except Exception as e:
                logging.error(f"Error processing {pdf_path}: {e}")

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    input_folder = r"C:\title\app\dataset"
    output_folder = r"C:\title\app\src\output_json"
    
    process_pdfs(input_folder, output_folder)

if __name__ == "__main__":
    main()