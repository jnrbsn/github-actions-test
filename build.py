from datetime import datetime
import os

from github import Github
import jinja2


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
template = jinja_env.get_template('index.html.jinja')
content = template.render(timestamp=datetime.utcnow().isoformat())

gh = Github(os.environ['GITHUB_TOKEN'])
repo = gh.get_repo(os.environ['GITHUB_REPOSITORY'])
f = repo.get_contents('index.html', ref='gh-pages')
result = repo.update_file(
    f.path,
    message='Update index.html on gh-pages branch',
    content=content,
    sha=f.sha,
    branch='gh-pages',
)
print(result)
