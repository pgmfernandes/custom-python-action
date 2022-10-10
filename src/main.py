import os
import sys

from src.controller import ConfigRepositoryController

GH_TOKEN_STR = "GH_TOKEN"
GITHUB_REPOSITORY_STR = "GITHUB_REPOSITORY"


def init():
    auth = os.environ[GH_TOKEN_STR]
    github_repository = os.environ[GITHUB_REPOSITORY_STR]
    c = ConfigRepositoryController(github_auth=auth, github_reposiroty=github_repository)
    c.execute_configuration()

# if __name__ == "__main__":
#     os.environ[GH_TOKEN_STR] = sys.argv[1]
#     os.environ[GITHUB_REPOSITORY_STR] = "pgmfernandes/using-custom-python-action"
#     init()
