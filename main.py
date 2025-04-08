from fetch_data import fetch_cves
from database import create_db, insert_cve

create_db()

data = fetch_cves()
for item in data['vulnerabilities']:
    cve = item['cve']
    cve_id = cve['id']
    description = cve['descriptions'][0]['value']
    last_modified = item.get('lastModified', 'N/A')

    print("Saving:", cve_id)
    insert_cve(cve_id, description, last_modified)

print("CVEs saved successfully!")
