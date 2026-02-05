# Threat-to-Control Mapping

This document maps identified system threats to selected NIST SP 800-53
controls and outlines corresponding mitigation measures. 

The mapping demonstrates how structured security controls
address the highest-priority risks in the system.
| Threat ID | Component | STRIDE | Threat Description | NIST Control(s) | Mitigation(s) |
|-----------|-----------|--------|------------------|----------------|---------------|
| T-01 | Web API | Spoofing | Stolen or forged authentication token used to access API | AC-6 | Enforce least privilege identities; use managed identities and MFA |
| T-02 | Web API | Elevation of Privilege | Over-permissioned service identity allows unauthorized access | AC-6 | Implement role-based access control (RBAC) and separation of duties |
| T-03 | Web API | Denial of Service | Excessive requests overwhelm API | SC-8 | Rate-limit API requests; enforce HTTPS; monitor traffic |
| T-04 | Web API | Repudiation | User actions cannot be traced due to insufficient logging | AU-2 | Enable centralized audit logging; retain immutable logs |
| T-05 | Data in Transit | Information Disclosure | Data intercepted during transmission | SC-8 | Enforce TLS 1.2+; validate certificates |
| T-06 | Document Storage | Information Disclosure | Unauthorized access to stored documents | SC-28, AC-6 | Encrypt documents at rest; enforce least privilege access |
| T-07 | Document Storage | Tampering | Stored documents modified without authorization | SC-28 | Encrypt at rest; audit access and modifications |
| T-08 | Logging System | Repudiation | Logs altered or deleted to hide activity | AU-2 | Store logs in immutable storage; monitor for tampering |
