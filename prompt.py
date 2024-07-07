
promtpt="""You are given the following resume content. Parse the information and convert it into a JSON format with the following structure: 

```json
{
  "name": "John Doe",
  "contact_information": {
    "email": "johndoe@example.com",
    "phone": "+1234567890",
    "address": "123 Main St, City, Country"
  },
  "summary": "Experienced software developer with a strong background in full-stack development...",
  "experience": [
    {
      "job_title": "Senior Software Developer",
      "company": "Tech Company",
      "dates": "January 2020 - Present",
      "responsibilities": [
        "Developed web applications using React and Node.js",
        "Led a team of 5 developers"
      ]
    },
    ...
  ],
  "education": [
    {
      "degree": "Bachelor of Science in Computer Science",
      "institution": "University of Somewhere",
      "dates": "September 2010 - June 2014"
    }
  ],
  "skills": [
    "JavaScript",
    "Python",
    "SQL",
    ...
  ],
  "certifications": [
    {
      "name": "Certified Kubernetes Administrator",
      "issuing_organization": "CNCF",
      "date": "June 2021"
    }
  ]
}"""
