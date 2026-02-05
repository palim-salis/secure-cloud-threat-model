# Data Flow Description

This document describes how data flows through the system and
identifies key interaction points relevant to threat modeling.
## External Entities

- **Client**
  - Authenticated internal users or services
  - Initiates requests to the Web API over HTTPS
## Processes

- **Web API**
  - Validates authentication tokens
  - Authorizes requests
  - Processes document upload and retrieval
## Data Stores

- **Document Storage**
  - Stores uploaded documents
  - Data is encrypted at rest

- **Log Store**
  - Stores security-relevant logs and audit events
## Data Flows

1. **Client → Web API**
   - Authentication token included in request
   - Requests sent over HTTPS

2. **Web API → Identity Provider**
   - Token validation request

3. **Web API → Document Storage**
   - Upload and retrieve document data

4. **Web API → Log Store**
   - Security events (authentication, access, errors)
## Trust Boundary Crossings

- Client to Web API crosses the public internet boundary
- Web API to internal cloud services occurs within a trusted boundary
