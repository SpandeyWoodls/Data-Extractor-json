# Data-Extractor-json
The script utilizes the PyMuPDF library to access and process the text within the PDF, extracting valuable information such as chapter titles, paragraph titles, and the associated English and Sanskrit text.
Ayurvedic Text Extractor
This Python script is designed to parse and extract structured data from a PDF file of the Ayurvedic classic "Astanga Hridaya Sutra Sthan" by Vagbhat. The script utilizes the PyMuPDF library to access and process the text within the PDF, extracting valuable information such as chapter titles, paragraph titles, and the associated English and Sanskrit text.

Features
Extracts chapter titles, paragraph titles, and contents from the PDF.
Separates English and Sanskrit texts for each paragraph.
Generates a unique identifier for each extracted paragraph.
Saves the extracted data as a structured JSON file.
Logs all operations to a file for easy tracking and debugging.
Usage
To use this script, ensure that you have the PyMuPDF library installed in your Python environment:

bash
Copy code
pip install PyMuPDF
Replace the pdf_path and output_json_path variables with the actual paths to your PDF file and desired output JSON file, respectively.

Run the script using Python:

bash
Copy code
python script_name.py
Output
The script outputs a JSON file with the extracted data, structured as follows:

id: A unique identifier for the paragraph.
para_id: A constructed identifier based on the PDF page number and paragraph title.
chapter_title: The title of the chapter in which the paragraph is found.
para_title: The title of the paragraph.
para_text_english: The English text of the paragraph.
para_text_sanskrit: The Sanskrit text of the paragraph.
Logging
All actions performed by the script, such as data insertions, are logged to extraction.log. This log file is useful for debugging and provides a record of the script's operations.
