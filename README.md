# Candidate Data Upload Application

This is a Flask web application that allows users to upload candidate data in CSV format, which is then stored in a Neo4j graph database. The application provides functionalities to display candidate information and download candidate details as a PDF file, complete with sample images.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Running the Application](#running-the-application)
6. [Usage](#usage)
7. [Sample CSV Format](#sample-csv-format)
8. [License](#license)
9. [Acknowledgements](#acknowledgements)

## Features

- **Upload Candidate Data**: Users can upload a CSV file containing candidate details.
- **Graph Database Integration**: Data is stored in a Neo4j graph database, allowing for complex relationships between candidates, colleges, degrees, and skills.
- **PDF Generation**: Candidate details can be downloaded as a PDF file, which includes a predefined image for each candidate.
- **User-Friendly Interface**: A simple web interface makes it easy for users to interact with the application.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **Neo4j**: A powerful graph database that allows for the representation of complex relationships.
- **Pandas**: A data manipulation library that makes it easy to work with CSV files.
- **ReportLab**: A library for generating PDFs in Python.

## Requirements

To run this application, you will need the following:

- Python 3.x
- Neo4j (running locally or on a server)

### Python Libraries

The application requires the following Python libraries:

- Flask
- neo4j
- pandas
- reportlab

- Here's how the application works, along with the corresponding files:

-Upload CSV File:
   User navigates to upload.html (located in the templates folder) and uploads a CSV file containing candidate data.
File: templates/upload.html

-Processing the CSV:
   The uploaded CSV file is processed in the app.py file. The application reads the CSV using Pandas and extracts candidate data.
The application then creates nodes and relationships in the Neo4j database for each candidate.
File: app.py

-Generating PDF:
   After processing, users can request to download candidate details. The application generates a PDF using the ReportLab library, including candidate information and predefined sample images.
File: app.py

-Downloading the PDF:
   The generated PDF is served to the user for download.
File: app.py


