import urllib.request
import json

url = "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/_data/simple-icons.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        
    icons = data['icons']
    queries = [
        "Bitbucket", "Confluence", "Jira", "Elastic", "Fortify", "GitLab", 
        "Grafana", "Vault", "Keycloak", "Kroki", "Mattermost", "Minio", 
        "Nexus", "Sonatype", "Rancher", "SonarQube", "Twistlock", "Prisma", "Uptime Kuma"
    ]
    
    for q in queries:
        matches = [i['title'] for i in icons if q.lower() in i['title'].lower()]
        print(f"Query '{q}': {matches}")
except Exception as e:
    print(f"Error: {e}")
