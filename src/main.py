import os
from cyberconfig import *

auth = os.environ['GH_TOKEN']
config_manager = CyberManager(github_auth=auth)
github_repository = os.environ['GITHUB_REPOSITORY']
config = config_manager.get_config(repo_name=github_repository)
print(config)

print(f"\n\n\nGithub_repository{github_repository}")
github_repository = "test-" + github_repository
print(f"::set-output name=dockerfiles::{github_repository}")