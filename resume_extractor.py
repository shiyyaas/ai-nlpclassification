import re
import json

# Sample resume texts for testing
resumes = [
    {
        "resume_id": "resume_1",
        "text": """
        Name: Rahul Kumar
        Email: rahul.kumar@example.com
        Phone: +91 98765 43210
        Skills: Python, Machine Learning
        """
    },
    {
        "resume_id": "resume_2",
        "text": """
        Name: Anjali Nair
        Email: anjali.nair@gmail.com
        Phone: 8765432109
        Skills: Java, SQL
        """
    },
    {
        "resume_id": "resume_3",
        "text": """
        Name: Arjun Thomas
        Email: arjun.thomas@outlook.com
        Phone: +91-91234-56789
        Skills: Python, Data Analysis
        """
    }
]

# Email extraction
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# mobile number extraction
phone_pattern = r'(?<!\d)(?:\+?91[\s-]?)?[6-9]\d{4}[\s-]?\d{5}(?!\d)'

results = []

for resume in resumes:
    text = resume["text"]

    emails = list(set(re.findall(email_pattern, text)))

    raw_phones = re.findall(phone_pattern, text)
    phones = []

    for phone in raw_phones:
        digits = re.sub(r'\D', '', phone)

        # Remove country code when present
        if len(digits) == 12 and digits.startswith("91"):
            digits = digits[2:]

        # Validate the 10-digit mobile number
        if len(digits) == 10 and digits[0] in "6789":
            if digits not in phones:
                phones.append(digits)

    results.append({
        "resume_id": resume["resume_id"],
        "emails": emails,
        "phone_numbers": phones
    })

with open("output.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)

print("Extraction completed. Results saved to output.json")
print(json.dumps(results, indent=4))
