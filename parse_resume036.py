import json

def parse_resume(resume_text):
    # Implement your parsing logic here
    parsed_resume = {
        "name": "Full Name",
        "contact_information": {
            "email": "email@example.com",
            "phone": "123-456-7890",
            "address": "123 Street Name, City, State, ZIP"
        },
        "professional_summary": "A brief professional summary...",
        "experience": [
            {
                "job_title": "Job Title",
                "company": "Company Name",
                "location": "City, State",
                "start_date": "Month Year",
                "end_date": "Month Year or Present",
                "responsibilities": [
                    "Responsibility 1",
                    "Responsibility 2"
                ]
            }
        ],
        "education": [
            {
                "degree": "Degree",
                "major": "Major",
                "school": "School Name",
                "location": "City, State",
                "graduation_date": "Month Year"
            }
        ],
        "skills": [
            "Skill 1",
            "Skill 2"
        ],
        "certifications": [
            {
                "name": "Certification Name",
                "issuing_organization": "Organization",
                "issue_date": "Month Year"
            }
        ],
        "projects": [
            {
                "name": "Project Name",
                "description": "Brief description of the project",
                "technologies_used": [
                    "Technology 1",
                    "Technology 2"
                ]
            }
        ]
    }
    return json.dumps(parsed_resume, indent=4)

# Example usage
resume_text = """
PASTE RESUME HERE
"""
parsed_resume_json = parse_resume(resume_text)
print(parsed_resume_json)
