# Data Protection Baseline

## Principles
- Encrypt sensitive data at rest and in transit
- Control access via least privilege
- Use platform-managed keys where possible (SC-28)

## Implementation
- TLS 1.2+ for all client-server communication
- AES-256 encryption for all stored documents
- Access control enforced by RBAC and managed identities
