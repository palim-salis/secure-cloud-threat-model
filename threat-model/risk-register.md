# Risk Register

This risk register prioritizes identified security threats based on
their potential impact and likelihood.
## Identified Risks

| Risk ID | Related Threat ID | Risk Description | Likelihood | Impact | Risk Level | Owner |
|--------|-------------------|------------------|------------|--------|------------|-------|
| R-01 | T-01 | Unauthorized access to API using stolen credentials | Medium | High | High | Security Team |
| R-02 | T-02 | Privilege escalation due to excessive permissions | Medium | High | High | Security Team |
| R-03 | T-06 | Exposure of sensitive documents in storage | Medium | High | High | Security Team |
| R-04 | T-04 | Inability to investigate incidents due to insufficient logging | Low | Medium | Medium | Security Team |
| R-05 | T-05 | Interception of data during transmission | Low | High | Medium | Security Team |
| R-06 | T-03 | API service disruption from excessive requests | Medium | Medium | Medium | Platform Team |

## Risk Scoring Approach

Risk levels are determined using qualitative assessments
of likelihood and impact (High, Medium, Low).

This approach supports early-stage design decisions
without requiring precise quantitative data.
## Next Steps

High-risk items will be addressed through the implementation
of security controls aligned with NIST SP 800-53.
