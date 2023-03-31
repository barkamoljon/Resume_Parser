# Resume_Parser
## Documentation for Resume_Parser

Resume_Parser is a Python package for parsing and extracting relevant information from resumes. It utilizes the PyPDF2 library to read and extract text from PDF files, and the Natural Language Toolkit (NLTK) to perform named entity recognition and part-of-speech tagging on the extracted text.

Installation:
To install the package, simply run the following command in your terminal:

Copy code
pip install Resume_Parser
Usage:
The main function of the package is parse_resume(), which takes in a file path to the resume PDF and returns a dictionary of extracted information. The dictionary contains the following keys:

- "name": the name of the candidate
- "email": the email address of the candidate
- "phone": the phone number of the candidate
- "skills": a list of skills mentioned in the resume
- "experience": a list of dictionaries, where each dictionary represents a job experience and contains the following keys:
- "title": the job title
- "company": the name of the company
- "location": the location of the company
- "start_date": the start date of the job
- "end_date": the end date of the job
- "description": a brief description of the job responsibilities
Here's an example of how to use the package:

python
Copy code
from resume_parser import parse_resume

resume_path = "/path/to/resume.pdf"
resume_data = parse_resume(resume_path)

print(resume_data)
Output:

perl
Copy code
{
    "name": "John Doe",
    "email": "johndoe@email.com",
    "phone": "123-456-7890",
    "skills": ["Python", "Java", "C++", "SQL"],
    "experience": [
        {
            "title": "Software Developer",
            "company": "ABC Company",
            "location": "New York, NY",
            "start_date": "2018-01-01",
            "end_date": "2021-05-31",
            "description": "Developed and maintained web applications using Python and Django framework"
        },
        {
            "title": "Intern",
            "company": "XYZ Inc.",
            "location": "San Francisco, CA",
            "start_date": "2017-05-01",
            "end_date": "2017-08-31",
            "description": "Assisted the development team in building and testing software products"
        }
    ]
}
Note:
Resume_Parser is not perfect and may not extract all the information accurately, especially if the resume has complex formatting or the information is not in a standard format. It is recommended to manually review the extracted information to ensure accuracy.
