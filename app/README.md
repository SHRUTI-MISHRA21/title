# PDF Batch Processor

## Overview
The PDF Batch Processor is a Python application designed to analyze PDF documents in bulk. It extracts titles and headings from each PDF file and saves the results in JSON format. This project utilizes the `PDFAnalyzer` class to perform the analysis and provides a simple interface for processing multiple PDF files from a specified input directory.

## Project Structure
```
pdf-batch-processor
├── src
│   ├── main.py          # Entry point for processing PDF files
│   ├── pdf_analyzer.py  # Contains the PDFAnalyzer class for analyzing PDFs
│   └── utils.py         # Utility functions for file handling
├── input_pdfs           # Directory for input PDF files
├── output_json          # Directory for output JSON files
├── requirements.txt      # Lists project dependencies
└── README.md            # Project documentation
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd pdf-batch-processor
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Place your PDF files in the `input_pdfs` directory.
2. Run the application:
   ```
   python src/main.py
   ```
3. The analysis results will be saved as JSON files in the `output_json` directory.

## Dependencies
This project requires the following Python package:
- `PyMuPDF`: For processing PDF files.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## THIS 
docker run --rm -v C:\title\app\dataset:/app/app/dataset l:latest