import os

services = [
    ("Atlassian Bitbucket", "bitbucket.svg", "https://bitbucket.org/"),
    ("Atlassian Confluence", "confluence.svg", "https://www.atlassian.com/software/confluence"),
    ("Atlassian Jira", "jira.svg", "https://www.atlassian.com/software/jira"),
    ("Elastic Stack", "elastic.svg", "https://www.elastic.co/"),
    ("Fortify SSC", "opentext.svg", "https://www.microfocus.com/en-us/cyberres/application-security/fortify"),
    ("GitLab", "gitlab.svg", "https://about.gitlab.com/"),
    ("Grafana", "grafana.svg", "https://grafana.com/"),
    ("HashiCorp Vault", "vault.svg", "https://www.vaultproject.io/"),
    ("Keycloak", "keycloak.svg", "https://www.keycloak.org/"),
    ("Kroki", "kroki.svg", "https://kroki.io/"),
    ("Mattermost", "mattermost.svg", "https://mattermost.com/"),
    ("Minio", "minio.svg", "https://min.io/"),
    ("Nexus Repository", "sonatype.svg", "https://www.sonatype.com/products/nexus-repository"),
    ("Nexus IQ Server", "sonatype.svg", "https://www.sonatype.com/products/nexus-lifecycle"),
    ("Rancher Manager", "rancher.svg", "https://rancher.com/"),
    ("SonarQube", "sonarqube.svg", "https://www.sonarqube.org/"),
    ("Twistlock", "paloaltonetworks.svg", "https://www.paloaltonetworks.com/prisma/cloud"),
    ("Uptime Kuma", "uptimekuma.svg", "https://uptime.kuma.pet/")
]

def generate_services():
    content = """---
title: "Services"
date: 2023-10-27T10:00:00+00:00
draft: false
description: "Our core services and integrations."
layout: "wide"
---

<div class="grid grid-cols-1 md:grid-cols-2 gap-8 w-full">
"""
    for name, icon, url in services:
        content += f"""
  <!-- {name} -->
  <a href="{url}" target="_blank" rel="noopener" class="flex items-center p-6 bg-white dark:bg-zinc-800 rounded-xl shadow hover:shadow-lg transition duration-200 border border-zinc-200 dark:border-zinc-700 w-full hover:-translate-y-1">
    <div class="flex-shrink-0 w-20 h-20 mr-6 bg-white rounded-full flex items-center justify-center border border-zinc-200 dark:border-zinc-700 shadow-sm">
      <img src="/images/icons/{icon}" class="w-12 h-12" alt="{name}" />
    </div>
    <div class="flex-1 min-w-0">
      <div class="text-2xl font-bold text-zinc-900 dark:text-white truncate">{name}</div>
    </div>
  </a>
"""
    content += "</div>\n"
    with open('content/services.md', 'w', encoding='utf-8') as f:
        f.write(content)

def generate_issues():
    content = """---
title: "Issues"
date: 2023-10-27T10:00:00+00:00
draft: false
description: "Service tracking, GitLab projects, and incident reporting."
layout: "wide"
---

<div class="grid grid-cols-1 xl:grid-cols-2 gap-8 w-full">
"""
    for name, icon, url in services:
        slug = name.lower().replace(" ", "-")
        gl_project = f"https://gitlab.com/your-group/{slug}"
        gl_issue = f"{gl_project}/-/issues/new"
        
        content += f"""
  <!-- {name} -->
  <div class="flex flex-col p-6 bg-white dark:bg-zinc-800 rounded-xl shadow-md border border-zinc-200 dark:border-zinc-700 w-full hover:-translate-y-1 transition duration-200">
    
    <div class="flex items-center mb-6">
      <div class="flex-shrink-0 w-20 h-20 mr-6 bg-white rounded-full flex items-center justify-center border border-zinc-200 dark:border-zinc-700 shadow-sm">
        <img src="/images/icons/{icon}" class="w-12 h-12" alt="{name}" />
      </div>
      <div class="flex-1 min-w-0">
        <div class="text-2xl font-bold text-zinc-900 dark:text-white truncate">{name}</div>
      </div>
    </div>
    
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mt-auto">
        <a href="{url}" target="_blank" rel="noopener" class="flex h-12 items-center justify-center text-center text-sm px-3 bg-zinc-100 dark:bg-zinc-700 hover:bg-zinc-200 dark:hover:bg-zinc-600 text-zinc-800 dark:text-zinc-100 rounded-lg transition font-bold leading-tight truncate">Website</a>
        
        <a href="{gl_project}" target="_blank" rel="noopener" class="flex h-12 items-center justify-center text-center text-sm px-3 bg-primary-100 dark:bg-primary-900/60 hover:bg-primary-200 dark:hover:bg-primary-800 text-primary-800 dark:text-primary-100 rounded-lg transition border border-primary-200 dark:border-primary-700 font-bold leading-tight truncate">GitLab Project</a>
        
        <a href="{gl_issue}" target="_blank" rel="noopener" class="flex h-12 items-center justify-center text-center text-sm px-3 bg-red-100 dark:bg-red-900/40 hover:bg-red-200 dark:hover:bg-red-800 text-red-800 dark:text-red-200 rounded-lg transition border border-red-200 dark:border-red-900 font-bold leading-tight truncate">Create Incident</a>
    </div>
    
  </div>
"""
    content += "</div>\n"
    with open('content/issues.md', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    generate_services()
    generate_issues()
    print("Regenerated efficiently with custom wide layout.")
