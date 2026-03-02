import urllib.request

slugs = [
    "bitbucket", "confluence", "jira", "elastic", "elasticsearch", "fortify", "microfocus", "opentext", 
    "gitlab", "grafana", "vault", "keycloak", "kroki", "mattermost", "minio", 
    "nexus", "sonatype", "rancher", "sonarqube", "twistlock", "paloaltonetworks", "uptimekuma"
]

for s in slugs:
    url = f"https://cdn.simpleicons.org/{s}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(req)
        print(f"[OK] {s}")
    except:
        print(f"[FAIL] {s}")
