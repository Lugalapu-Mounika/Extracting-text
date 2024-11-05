# Extracting-text

This project provides a GUI-based application using Tkinter in Python to extract text from scanned documents, images, PDFs, and Word files using AWS Textract. The tool enables users to upload files, process them, and display the extracted text within the application.

**Features**
Upload & Process Files: Supports .jpg, .png, .txt, .pdf, and .docx file formats.
AWS Textract Integration: Utilizes AWS Textract to extract text from images and PDF files.
GUI Interface: Built with Tkinter, allowing easy file uploads and display of extracted text.
Multi-file Support: Processes and displays text from images, text files, PDFs, and Word documents.

**Requirements**
Python 3.x
AWS Account: With Textract enabled and AWS credentials configured.
Packages:
tkinter: For the GUI.
boto3: For AWS Textract integration.
Pillow: For image processing.
python-docx: For processing .docx files.

**Set Up**
Install dependencies
pip install boto3 Pillow python-docx
Set up AWS credentials using the AWS CLI or by configuring ~/.aws/credentials with a profile named user
**Run the application**
python app.py

**How to Use**
Launch the Application: Running the script opens a window with an "Upload file & analyze text" button.
Upload a File: Click the button, select an image, PDF, text, or Word document, and confirm upload.
View Extracted Text: The extracted text is displayed in the text area within the application.
 
