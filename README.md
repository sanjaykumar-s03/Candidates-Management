# Candidate Data Upload Application

   This is a Flask web application that allows users to upload candidate data in CSV format, which is then stored in a Neo4j graph database. The application also enables users to download candidate details as a PDF file, complete with sample images.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Running the Application](#running-the-application)
7. [Sample CSV Format](#sample-csv-format)
8. [Workflow](#workflow)


## Features
 **Upload Candidate Data**: Users can upload a CSV file containing candidate details.
 **Graph Database Integration**: Data is stored in a Neo4j graph database, allowing for complex relationships between candidates, colleges, degrees, and skills.
 **PDF Generation**: Candidate details can be downloaded as a PDF file, which includes a predefined image for each candidate.
 **User-Friendly Interface**: A simple web interface makes it easy for users to interact with the application.

## Technologies Used
**Flask**: A lightweight WSGI web application framework for Python.
 **Neo4j**: A powerful graph database that allows for the representation of complex relationships.
 **Pandas**: A data manipulation library that makes it easy to work with CSV files.
 **ReportLab**: A library for generating PDFs in Python.

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

## Installation
1. **Clone the Repository**:
   Start by cloning this repository to your local machine. Open your terminal or command prompt and run:
      git clone https://github.com/username/my-flask-app.git
      cd my-flask-app


2. **Install Dependencies**:
   Install the required packages using the following command and run :
       pip install -r requirements.txt on the terminal
   
3. **Set Up Neo4j**:
   Make sure you have a Neo4j database running. You can download it from Neo4j's official website.
Update the Neo4j connection details (username, password, etc.) in app.py to match your database setup.

## Running the Application
1.**Start the Flask Server**: 
   In your terminal, run:
      python app.py

2. **Access the Application: Open your web browser and navigate to**:
   http://127.0.0.1:5000

## Sample CSV Format
To ensure proper data processing, your CSV file should follow this format:

   **Name,Email,College,Year of Passout,Degree,Skills
   John Doe,john.doe@example.com,University A,2023,B.Sc. in Computer Science,"Python; Java"
   Jane Smith,jane.smith@example.com,University B,2022,B.A. in Mathematics,"R; SQL"**

Explanation of Fields:
Name: Full name of the candidate.
Email: Email address of the candidate.
College: The college where the candidate studied.
Year of Passout: The year the candidate graduated.
Degree: The degree obtained by the candidate.
Skills: A semicolon-separated list of skills the candidate possesses.

## Workflow
Here’s how the application works, along with the corresponding files:
1. Upload the CSV File
2. User navigates to upload.html (located in the templates folder) and uploads a CSV file containing candidate data.
3. The uploaded CSV file is processed in the app.py file. The application reads the CSV using Pandas and extracts candidate data.
4. The application creates nodes and relationships in the Neo4j database for each candidate.
5. After processing, users can request to download candidate details. The application generates a PDF using the ReportLab library, including candidate information and predefined sample images.
6. The generated PDF is served to the user for download.
