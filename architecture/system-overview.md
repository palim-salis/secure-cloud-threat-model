# System Overview
This project models the security of a cloud-based document management API
used to store and retrieve internal company documents.

The system is designed to support authenticated users and services while
protecting sensitive data through secure-by-default configurations,
centralized logging, and strong access controls.
## Core Components

The system consists of the following components:

- **Client**  
  Internal users or services that access the API over HTTPS.

- **Web API**  
  Exposes endpoints for uploading and retrieving documents.
  Handles authentication and authorization.

- **Identity Provider (IdP)**  
  Issues tokens used to authenticate users and services.

- **Document Storage**  
  Stores encrypted documents at rest.

- **Logging & Monitoring**  
  Collects security-relevant events for audit and investigation.
  ## Trust Boundaries

The system includes the following trust boundaries:

- **Public Boundary**  
  Client to Web API communication over the internet.

- **Private Cloud Boundary**  
  Communication between the Web API, Identity Provider, Storage,
  and Logging services within the cloud environment.

  ## Scope

### In Scope
- Authentication and authorization flows
- API access to document storage
- Data encryption in transit and at rest
- Security logging and auditing

### Out of Scope
- Application source code vulnerabilities
- End-user device security
- Physical security of cloud data centers


