from jsonschema import validate
import json
import os

company_index_schema = {
    'company_name': "string",
    'source_url': "string",
}

with open(os.path.abspath('../company_index.json'), 'r') as f:
    data = json.load(f)

validate(instance=data, schema=company_index_schema)


company_profile_schema ={
        "company_name": "string",
        "company_location": "string",
        "company_website": "string",
        "company_webdomain": "string",
        "company_industry": "string",
        "company_employee_size": "string",
        "company_revenue": "string",
        "contact_details": [
            {
                "Contact_name": "string",
                "Contact_jobtitle": "string",
                "Contact_email_domain": "string"
            }
        ]
    }
    
with open(os.path.abspath('../company_profiles.json'), 'r') as f:
    data2 = json.load(f)

validate(instance=data2, schema=company_profile_schema)
    

print("Validated")