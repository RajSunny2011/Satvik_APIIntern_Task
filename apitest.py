import requests

API_URL = "http://localhost:5000"
headers = {"Content-Type": "application/json","Authorization": "supersecretcode"}

patient_id = "P123"
diagnosis_payload = {
    "name": "Mr. X",
    "diagnosis": "Asthma",
    "prescription": "Inhaler",
    "doctor": "Dr. K",
    "recommendations": ["Use inhaler", "Avoid allergens"]
}

# Submit diagnosis
post_url = f"{API_URL}/submit/{patient_id}"
post_response = requests.post(post_url, json=diagnosis_payload, headers=headers)

print("POST Response:")
print(post_response.status_code, end=": ")
print(post_response.json())

# Retrieve diagnosis
get_url = f"{API_URL}/diagnosis/{patient_id}"
get_response = requests.get(get_url, headers=headers)

print("\nGET Response:")
print(get_response.status_code, end=": ")
print(get_response.json())
