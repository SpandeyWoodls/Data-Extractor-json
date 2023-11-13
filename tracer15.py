import fitz  # PyMuPDF
import re
import json
import logging
from bson import ObjectId

# Configure logging
logging.basicConfig(level=logging.INFO, filename='extraction.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to clean the extracted text
def clean_text(text):
    return text.replace('\x00', '').strip()

# Regex patterns
page_number_regex = re.compile(r'Page No\. \d+')
chapter_title_regex = re.compile(r'Chapter \d+: [\w\s]+')
paragraph_title_regex = re.compile(r'^\d+\.\s+[\w\s]+', re.MULTILINE)
sanskrit_text_regex = re.compile(r'[\u0900-\u097F]+')
english_text_regex = re.compile(r'[^\u0900-\u097F]+')

# Function to extract information from PDF
def extract_information_from_pdf(pdf_path):
    extracted_data = []
    current_chapter_title = ""  # Keep track of the current chapter title

    # Open the PDF file
    with fitz.open(pdf_path) as doc:
        # Iterate through each page
        for page_number in range(len(doc)):
            page = doc[page_number]
            raw_text = page.get_text("text")

            # Remove page numbers
            raw_text = page_number_regex.sub("", raw_text)

            # Clean and split the text into paragraphs
            paragraphs = raw_text.split('\n\n')  # Assuming paragraphs are separated by double newlines

            for paragraph in paragraphs:
                paragraph = clean_text(paragraph)

                # Check and update the current chapter title
                chapter_title_match = chapter_title_regex.search(paragraph)
                if chapter_title_match:
                    current_chapter_title = chapter_title_match.group(0)
                    paragraph = paragraph.replace(current_chapter_title, "")  # Remove chapter title from the paragraph

                # Find paragraph title
                para_title_match = paragraph_title_regex.search(paragraph)
                para_title = para_title_match.group(0) if para_title_match else ""

                # Separate Sanskrit and English text
                sanskrit_text = " ".join(sanskrit_text_regex.findall(paragraph))
                english_text = " ".join(english_text_regex.findall(paragraph))

                # Create the data structure
                para_data = {
                    "id": str(ObjectId()),
                    "para_id": f"Astanga_Hridaya_Sutra_Sthan_Vagbhat-page{page_number+1}-para{para_title}",
                    "chapter_title": current_chapter_title,
                    "para_title": para_title,
                    "para_text_english": english_text,
                    "para_text_sanskrit": sanskrit_text
                }

                extracted_data.append(para_data)

                # Log the data insertion
                logging.info(f"Inserted data for para_id: {para_data['para_id']}")
                # Print the data insertion
                print(json.dumps(para_data, ensure_ascii=False))

    return extracted_data

# Path to the PDF file and the output JSON file
pdf_path = r'E:\Greenspirits\greenbooks\Astanga_Hridaya_Sutra_Sthan_Vagbhat.pdf'  # Replace with the correct path to your PDF
output_json_path = r'E:\Greenspirits\ggg\16.json'

# Call the function to extract information
data = extract_information_from_pdf(pdf_path)

# Save the extracted data to a JSON file
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

# Log the completion of the process
logging.info(f"Data extraction completed. JSON file created at {output_json_path}")
