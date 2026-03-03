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
---

<div class="grid grid-cols-1 xl:grid-cols-2 gap-8 w-full max-w-full">
"""
    for name, icon, url in services:
        content += f"""
  <!-- {name} -->
  <a href="{url}" target="_blank" rel="noopener" class="flex items-center p-6 bg-white dark:bg-zinc-800 rounded-xl shadow-md hover:shadow-lg transition duration-200 border border-zinc-200 dark:border-zinc-700 w-full hover:-translate-y-1">
    <div class="flex-shrink-0 w-24 h-24 mr-6 bg-white rounded-full flex items-center justify-center border border-zinc-200 dark:border-zinc-700 shadow-sm">
      <img src="/images/icons/{icon}" class="w-14 h-14" alt="{name}" />
    </div>
    <div class="flex-1">
      <div class="text-2xl font-bold text-zinc-900 dark:text-white break-words">{name}</div>
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
---

<div class="grid grid-cols-1 gap-8 w-full max-w-full">
"""
    for name, icon, url in services:
        content += f"""
  <!-- {name} -->
  <div class="flex flex-col md:flex-row items-center p-6 bg-white dark:bg-zinc-800 rounded-xl shadow-md border border-zinc-200 dark:border-zinc-700 w-full relative">
    <div class="flex items-center flex-1 w-full mb-4 md:mb-0">
        <div class="flex-shrink-0 w-24 h-24 mr-6 bg-white rounded-full flex items-center justify-center border border-zinc-200 dark:border-zinc-700 shadow-sm">
          <img src="/images/icons/{icon}" class="w-14 h-14" alt="{name}" />
        </div>
        <div class="flex-1">
          <div class="text-2xl font-bold text-zinc-900 dark:text-white break-words">{name}</div>
        </div>
    </div>
    
    <div class="flex flex-col sm:flex-row gap-3 w-full md:w-auto mt-2 md:mt-0 lg:ml-auto">
        <a href="{url}" target="_blank" rel="noopener" class="flex-1 sm:flex-none justify-center text-center text-sm px-6 py-3 bg-zinc-100 dark:bg-zinc-700 hover:bg-zinc-200 dark:hover:bg-zinc-600 text-zinc-800 dark:text-zinc-100 rounded-lg transition font-medium whitespace-nowrap">Website</a>
        
        <a href="https://gitlab.com/" target="_blank" rel="noopener" class="flex-1 sm:flex-none justify-center text-center text-sm px-6 py-3 bg-primary-100 dark:bg-primary-900/60 hover:bg-primary-200 dark:hover:bg-primary-800 text-primary-800 dark:text-primary-100 rounded-lg transition border border-primary-200 dark:border-primary-700 whitespace-nowrap font-medium">GitLab Project</a>
        
        <a href="https://gitlab.com/" target="_blank" rel="noopener" class="flex-1 sm:flex-none justify-center text-center text-sm px-6 py-3 bg-red-100 dark:bg-red-900/40 hover:bg-red-200 dark:hover:bg-red-800 text-red-800 dark:text-red-200 rounded-lg transition border border-red-200 dark:border-red-900 whitespace-nowrap font-medium">Create Incident</a>
    </div>
  </div>
"""
    content += "</div>\n"
    with open('content/issues.md', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    generate_services()
    generate_issues()
    print("Regenerated both pages successfully.")
