# NIST SP 800-53 Control Selection

This project applies a targeted subset of NIST SP 800-53 controls
to address high-priority risks identified during threat modeling.

Rather than implementing all controls, this approach focuses on
controls that provide the greatest risk reduction for the system
architecture and threat profile.
## Selected Controls

| Control ID | Control Name | Control Family |
|-----------|--------------|----------------|
| AC-6 | Least Privilege | Access Control |
| AU-2 | Event Logging | Audit & Accountability |
| SC-8 | Transmission Confidentiality and Integrity | System & Communications Protection |
| SC-28 | Protection of Information at Rest | System & Communications Protection |
#### AC-6: Least Privilege

AC-6 was selected to mitigate risks related to unauthorized access
and privilege escalation. Over-permissioned identities increase
the impact of compromised credentials or services.

This control directly addresses high-risk items identified in
the risk register related to elevation of privilege and
unauthorized access.
#### AU-2: Event Logging

AU-2 supports detection and investigation of security incidents
by ensuring that security-relevant events are identified and logged.

This control was selected to address risks associated with
repudiation and insufficient auditability identified during
threat modeling.
#### SC-8: Transmission Confidentiality and Integrity

SC-8 protects sensitive data from interception or modification
during transmission across untrusted networks.

This control addresses information disclosure threats related
to data in transit across public boundaries.
#### SC-28: Protection of Information at Rest

SC-28 ensures that stored data is protected from unauthorized
disclosure or modification through encryption and access controls.

This control mitigates high-impact risks related to exposure
of sensitive documents in storage.
## Summary

The selected controls collectively address the highest-risk
threats identified during threat modeling and support a
secure-by-default system design.

