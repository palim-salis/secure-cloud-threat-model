# STRIDE Threat Analysis

Threats were identified using the STRIDE methodology
(Spoofing, Tampering, Repudiation, Information Disclosure,
Denial of Service, Elevation of Privilege).

Each threat is mapped to a specific system component
identified in the data flow diagram.
## Identified Threats

| Threat ID | Component | STRIDE Category | Threat Description | Impact | Likelihood |
|----------|-----------|-----------------|-------------------|--------|------------|
| T-01 | Web API | Spoofing | Stolen or forged authentication token used to access API | High | Medium |
| T-02 | Web API | Elevation of Privilege | Over-permissioned service identity allows unauthorized access | High | Medium |
| T-03 | Web API | Denial of Service | Excessive requests overwhelm API | Medium | Medium |
| T-04 | Web API | Repudiation | User actions cannot be traced due to insufficient logging | Medium | Low |
| T-05 | Data in Transit | Information Disclosure | Data intercepted during transmission | High | Low |
| T-06 | Document Storage | Information Disclosure | Unauthorized access to stored documents | High | Medium |
| T-07 | Document Storage | Tampering | Stored documents modified without authorization | High | Low |
| T-08 | Logging System | Repudiation | Logs altered or deleted to hide activity | High | Low |


## Summary

The identified threats highlight risks related to unauthorized access,
insufficient logging, and data exposure. These threats inform the
selection and implementation of security controls aligned with
NIST SP 800-53.
