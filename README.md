## Document-Modeling-Runbook RxRocket 🚀
SQL to MongoDB Modeling foundations

SQL Schema Representation (Before Migration to MongoDB)
1. Clients Table
Each client has a unique ID and general onboarding details.
```
CREATE TABLE clients (
    client_id VARCHAR(50) PRIMARY KEY,
    company_name VARCHAR(255),
    onboarding_date TIMESTAMP,
    status VARCHAR(50)
);
```
2. Pharmacy Networks Table
Since a client can have multiple pharmacy networks, this requires a many-to-many relationship.
```
CREATE TABLE pharmacy_networks (
    id SERIAL PRIMARY KEY,
    client_id VARCHAR(50) REFERENCES clients(client_id) ON DELETE CASCADE,
    pharmacy_name VARCHAR(100)
);
```
3. Submitted By Table
```
CREATE TABLE submitted_by (
    id SERIAL PRIMARY KEY,
    client_id VARCHAR(50) REFERENCES clients(client_id) ON DELETE CASCADE,
    name VARCHAR(255),
    email VARCHAR(255),
    role VARCHAR(100)
);
```
4. Claim Details Table
Each client may have one or more claims associated with them.
```
CREATE TABLE claim_details (
    claim_id VARCHAR(50) PRIMARY KEY,
    client_id VARCHAR(50) REFERENCES clients(client_id) ON DELETE CASCADE,
    medication VARCHAR(255),
    dosage VARCHAR(50),
    quantity INT,
    insurance_provider VARCHAR(255),
    prior_auth_required BOOLEAN
);
```
5. Onboarding Notes Table
Since multiple onboarding notes exist, they are stored in a separate table.
```
CREATE TABLE onboarding_notes (
    id SERIAL PRIMARY KEY,
    client_id VARCHAR(50) REFERENCES clients(client_id) ON DELETE CASCADE,
    note TEXT
);
```
## Key Differences Between SQL and MongoDB
Normalization in SQL: SQL breaks the document into separate tables, each with a foreign key reference, reducing duplication.
Denormalization in MongoDB: The JSON document stores nested objects (submittedBy, claimDetails) and arrays (pharmacyNetwork, onboardingNotes), which is better suited for document-oriented workloads.

## Query Complexity:
## In SQL, retrieving the full onboarding details for a client requires JOINs across multiple tables.
🚀 In MongoDB, a single query retrieves the entire document.
```
{
    "_id": "65c1f0a3e4b0fbbd9a3e89c2",
    "clientId": "UHG-12345",
    "companyName": "Pharma Health Inc.",
    "onboardingDate": "2025-01-30T14:25:00.000+00:00",
    "status": "pending",
    "pharmacyNetwork": ["CVS", "Walgreens", "RiteAid"],
    "submittedBy": {
        "name": "Jane Doe",
        "email": "jane.doe@pharmahealth.com",
        "role": "Claims Specialist"
    },
    "claimDetails": {
        "claimId": "RX-98765",
        "medication": "Atorvastatin",
        "dosage": "20mg",
        "quantity": 30,
        "insuranceProvider": "OptumRx",
        "priorAuthorizationRequired": true
    },
    "onboardingNotes": [
        {
            "note": "First note about the onboarding process"
        },
        {
            "note": "Second note regarding client setup"
        }
    ]
}
```
## Key Takeaways
SQL Normalization: The data is stored across multiple tables, linked via client_id. <br>

MongoDB Denormalization: data is stored in a single document, embedding related data inside arrays and objects. <br>

Retrieval Efficiency: In SQL, retrieving the full onboarding record requires multiple JOIN queries, while in MongoDB, 
it can be fetched with a single query. 👍 <br>
