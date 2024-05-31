import requests
import os

# Tu token personal de acceso de GitHub
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
USERNAME = 'xxxDIDIERxxx'

def get_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    repos = response.json()
    return repos

def update_readme(repos):
    with open('README.md', 'r') as file:
        readme_content = file.read()

    repos_md = "\n".join(
        [f"* [{repo['name']}]({repo['html_url']})" for repo in repos]
    )

    updated_content = readme_content.replace("<!-- REPOS_START -->", f"<!-- REPOS_START -->\n{repos_md}\n<!-- REPOS_END -->")

    with open('README.md', 'w') as file:
        file.write(updated_content)

if __name__ == "__main__":
    repos = get_repositories(USERNAME)
    update_readme(repos)
