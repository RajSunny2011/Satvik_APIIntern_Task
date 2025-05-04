# 🧠 Medical Imaging & Report Analyzer API

**By Satvik Raj – API Development Intern Task**

**Medical Imaging & Report Analyzer**  
_Submit a patient ID and retrieve diagnosis results._

-   **Flask:** Python
-   **Storage:** Local JSON file (`data.json`)
-   **Authentication:** Token-based via HTTP `Authorization` header

## API Endpoints

### 1. `POST /submit/<patient_id>`

**Description:** Submit diagnosis data for a given patient ID.

**Headers:**

`{"Content-Type": "application/json","Authorization": "supersecretcode"}`

**Request Body:**

```
{
    "P123": {
        "name": "Mr. X",
        "diagnosis": "Asthma",
        "prescription": "Inhaler",
        "doctor": "Dr. K",
        "recommendations": [
            "Use inhaler",
            "Avoid allergens"
        ]
    }
}
```

**Response:**

`{"message": "Diagnosis data submitted", "patient_id": "P123"}`

**Status Codes:**

-   `201 Created` – On success
-   `400 Bad Request` – If fields are missing
-   `401 Unauthorized` – If token is invalid


### 2. `GET /diagnosis/<patient_id>`

**Description:** Retrieve stored diagnosis data for a given patient.

**Headers:**

`{"Authorization": "supersecretcode"}`

**Response:**

```
{'diagnosis': 'Asthma', 'doctor': 'Dr. K', 'name': 'Mr. X', 'patient_id': 'P123', 'prescription': 'Inhaler', 'recommendations': ['Use inhaler', 'Avoid allergens']}
```

**Status Codes:**

- `200 OK` – On success
- `404 Not Found` – If patient ID does not exist
- `401 Unauthorized` – If token is invalid

## Setup
1.  Clone repo

2.  Install dependencies:

```
pip install flask requests
```

3.  Run the API:

```
python main.py
```

4. Test the API:

Use the given python script:
```
python apitest.py
```

*or* use commands

For Post:
```
curl -X POST http://localhost:5000/submit/P123 -H "Content-Type: application/json" -H "Authorization: supersecretcode" -d '{"name":"Mr. X","diagnosis":"Asthma","prescription":"Inhaler","doctor":"Dr. K","recommendations":["Use inhaler","Avoid allergens"]}'
```

For Get:
```
curl -X GET http://localhost:5000/diagnosis/P123 -H "Authorization: supersecretcode"
```


