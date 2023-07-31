from github import Github
from github.GithubException import GithubException

# token should have repo and delete_repo scopes for source and target repos
token = "GH_PAT_TOKEN"

# source and target repositories
source_repo_name = "<username>/<source repository name>"
target_repo_names = ["<username>/<target repository name 1>", "<username>/<target repository name 2>"]

g = Github(token)
source_repo = g.get_repo(source_repo_name)
labels = source_repo.get_labels()

for target_repo_name in target_repo_names:
    target_repo = g.get_repo(target_repo_name)
    for label in labels:
        try:
            target_repo.create_label(name=label.name, color=label.color, description=label.description)
            print(f'Copied label {label.name} to {target_repo_name}')
        except GithubException as e:
            if e.status == 422:  # error status indicating the label already exists
                print(f'Label {label.name} already exists in {target_repo_name}. Skipping...')
            else:
                print(f'Failed to copy label {label.name} to {target_repo_name}: {e}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
