import csv

# Load threat-to-control mappings
# CSV format: Threat ID, Component, STRIDE, Threat Description, NIST Controls
filename = 'threat_control_mapping.csv'

coverage_issues = []

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        threat_id = row['Threat ID']
        controls = row['NIST Controls'].strip()
        if not controls:
            coverage_issues.append(threat_id)

if coverage_issues:
    print("⚠️ The following threats are missing NIST control mappings:")
    for tid in coverage_issues:
        print(f" - {tid}")
else:
    print("✅ All threats have at least one NIST control mapped!")
