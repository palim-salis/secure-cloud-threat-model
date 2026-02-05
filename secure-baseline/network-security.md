# Network Security Baseline

## Principles
- Minimize attack surface
- Separate public and private traffic
- Secure communications (SC-8)

## Implementation
- Private endpoints for storage and internal services
- No public IPs on backend services
- Firewalls and NSGs restrict traffic to known sources
- API endpoints enforce HTTPS with TLS 1.2+
- Network segmentation between production and non-production environments
