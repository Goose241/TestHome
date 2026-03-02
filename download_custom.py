import urllib.request
import os

custom_icons = {
    "kroki": "https://raw.githubusercontent.com/yuzutech/kroki.io/master/assets/logo.svg",
    "sonarqube": "https://raw.githubusercontent.com/log-z/Website-Logos/main/sonarqube.svg"
}

out_dir = "static/images/icons"
os.makedirs(out_dir, exist_ok=True)

for name, url in custom_icons.items():
    out_path = os.path.join(out_dir, f"{name}.svg")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(out_path, 'wb') as f:
                f.write(response.read())
        print(f"[OK] {name}.svg")
    except Exception as e:
        print(f"[FAIL] {name}.svg: {e}")
