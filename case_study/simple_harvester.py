from internetarchive import search_items
import json, requests, time

query = 'genre:Shahnama+Shah+Tahmasp'
items = search_items(query, fields=['identifier', 'title', 'creator', 'date'])
print(f'Found {items.num_found} items. Fetching metadata and IIIF manifests...')
data = []
for item in items:  # Limit to first 8 for demo
    item_id = item['identifier']
    print(f'Processing {item_id}...')
    # Fetch full metadata
    meta = requests.get(f'https://archive.org/metadata/{item_id}').json()
    # Fetch IIIF manifest
    manifest = requests.get(f'https://iiif.archive.org/iiif/{item_id}/manifest.json').json()
    combined = {'item_id': item_id, 'metadata': meta, 'iiif_manifest': manifest}
    data.append(combined)
    time.sleep(0.5)  # Be polite

# Save as JSONL to GitHub (or GDrive → GitHub sync)
with open('C:\\Users\\Floyd\\Orchestrating-DCHD\\case_study\\data\\raw\\items.json', 'w') as f:
    for d in data: f.write(json.dumps(d) + '\n')