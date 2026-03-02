import urllib.request
import os

url = "https://upload.wikimedia.org/wikipedia/commons/a/a2/SonarQube_Logo.svg"
out_path = "static/images/icons/sonarqube.svg"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        with open(out_path, 'wb') as f:
            f.write(response.read())
    print("[OK] sonarqube.svg")
except Exception as e:
    print(f"[FAIL] sonarqube.svg: {e}")
