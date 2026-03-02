import os
import urllib.request

slugs = [
    "bitbucket", "confluence", "jira", "elastic", "opentext", 
    "gitlab", "grafana", "vault", "keycloak", "kroki", "mattermost", "minio", 
    "sonatype", "rancher", "sonarqube", "paloaltonetworks", "uptimekuma"
]

out_dir = "static/images/icons"
os.makedirs(out_dir, exist_ok=True)

for s in slugs:
    url = f"https://cdn.simpleicons.org/{s}"
    out_path = os.path.join(out_dir, f"{s}.svg")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(out_path, 'wb') as f:
                f.write(response.read())
        print(f"[OK] {s}.svg saved")
    except Exception as e:
        print(f"[FAIL] {s}: {e}")
