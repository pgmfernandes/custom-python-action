import os

github_repository = os.environ.get("GITHUB_REPOSITORY")
print(github_repository)
github_repository = "test-" + github_repository
print(f"::set-output name=dockerfiles::{github_repository}")