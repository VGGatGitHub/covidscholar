import urllib.request, json

url = "https://connect.biorxiv.org/relate/collection_json.php?grp=181"

with urllib.request.urlopen(url) as response:
  count = 0
  results = json.loads(response.read().decode('utf-8'))
  papers = results["rels"]
  for paper in papers:
    if count >= 1000:
      break

    doc = {
      'authors': paper['rel_authors'],
      'link': paper['rel_link'],
      'doi': paper['rel_doi'],
      'title': paper['rel_title'],
      'abstract': paper['rel_abs'],
      'date': paper['rel_date'],
      'site': paper['rel_site']
    }
    
    with open(doc['doi'].replace('/', '-') + '.json', 'w') as fp:
      json.dump(doc, fp)
    count = count + 1
