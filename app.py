from flask import Flask, render_template, request, redirect, send_file
from neo4j import GraphDatabase
import pandas as pd
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

# Neo4j configuration
neo4j_uri = "bolt://localhost:7687"
neo4j_user = "neo4j"  # Your username
neo4j_password = "@Sanjaykumar123"  # Your password
driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

# Upload folder configuration
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to process candidates from CSV
def process_candidates(file_path):
    df = pd.read_csv(file_path)
    with driver.session() as session:
        for _, row in df.iterrows():
            candidate_name = row['Name']
            candidate_email = row['Email']
            college = row['College']
            year_of_passout = row['Year of Passout']
            degree = row['Degree']
            skills = row['Skills'].split(',')

            # Create Candidate node
            session.run("MERGE (c:Candidate {name: $name, email: $email})",
                        name=candidate_name, email=candidate_email)

            # Create relationships
            session.run("MERGE (co:College {name: $college})", college=college)
            session.run("MERGE (d:Degree {name: $degree})", degree=degree)
            session.run("MERGE (y:Year {year: $year})", year=year_of_passout)
            session.run("""
                MATCH (c:Candidate {name: $name}),
                      (co:College {name: $college}),
                      (y:Year {year: $year}),
                      (d:Degree {name: $degree})
                MERGE (c)-[:Studied_at]->(co)
                MERGE (c)-[:Passed_out]->(y)
                MERGE (c)-[:Has_degree]->(d)
            """, name=candidate_name, college=college, year=year_of_passout, degree=degree)

            for skill in skills:
                skill = skill.strip()
                session.run("MERGE (s:Skill {name: $skill})", skill=skill)
                session.run("""
                    MATCH (c:Candidate {name: $name}), (s:Skill {name: $skill})
                    MERGE (c)-[:Has_skill]->(s)
                """, name=candidate_name, skill=skill)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/upload', methods=['GET', 'POST'])  # Allow both GET and POST
def upload_file():
    if request.method == 'POST':
        if 'csvFile' not in request.files:
            return 'No file part', 400
        file = request.files['csvFile']
        if file.filename == '':
            return 'No selected file', 400
        if file and file.filename.endswith('.csv'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            process_candidates(file_path)  # Process candidates from the CSV
            return redirect('/candidate_search')  # Redirect to candidate search
        return 'Invalid file type. Please upload a CSV file.', 400
    return render_template('upload.html')  # Render upload page for GET request

@app.route('/candidate_search', methods=['GET'])
def candidate_search():
    return render_template('candidate_search.html')

@app.route('/candidate_details', methods=['POST'])
def candidate_details():
    candidate_name = request.form.get('candidate_name')

    with driver.session() as session:
        query = """
        MATCH (c:Candidate {name: $name})-[:Studied_at]->(co:College),
              (c)-[:Passed_out]->(y:Year),
              (c)-[:Has_degree]->(d:Degree),
              (c)-[:Has_skill]->(s:Skill)
        RETURN c.name AS name, c.email AS email, co.name AS college, y.year AS year, d.name AS degree, collect(s.name) AS skills
        """
        result = session.run(query, name=candidate_name)
        candidate_info = result.single()

    if candidate_info:
        return create_pdf(candidate_info)
    else:
        return "Candidate not found.", 404

def create_pdf(candidate_info):
    # Create a byte stream buffer
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Draw the candidate details
    p.drawString(100, height - 100, f"Name: {candidate_info['name']}")
    p.drawString(100, height - 120, f"Email: {candidate_info['email']}")
    p.drawString(100, height - 140, f"College: {candidate_info['college']}")
    p.drawString(100, height - 160, f"Year of Passout: {candidate_info['year']}")
    p.drawString(100, height - 180, f"Degree: {candidate_info['degree']}")
    p.drawString(100, height - 200, f"Skills: {', '.join(candidate_info['skills'])}")

    p.showPage()
    p.save()

    # Move to the beginning of the BytesIO buffer
    buffer.seek(0)

    # Return the PDF file
    return send_file(buffer, as_attachment=True, download_name='candidate_details.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
