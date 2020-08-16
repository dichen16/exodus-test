import pytest
import logging
from client.rhsm_tools import create_missing_repo

import json


@pytest.fixture(scope="function")
def prepare_single_build(testdata_errata):
    logging.debug("[---] prepare_single_build is called")
    adv = "TOM-2020:0816"

    logging.debug(
        "[Dry run] use errata %s get adv required repos and create them",
        str(testdata_errata),
    )
    # repo_list = testdata_errata.get_repos(adv)
    # create_missing_repo(repo_list)

    yield {"target": "target_to_pulp2", "file_list": [adv]}

    logging.debug("Teardown")


@pytest.fixture(scope="function")
def prepare_published_repos(testdata_errata):
    logging.debug("[---] prepare_published_repos is called")
    adv = "TOM-1966:0824"

    logging.debug(
        "[Dry run] use errata %s get adv required repos and create them",
        str(testdata_errata),
    )
    # repo_list = testdata_errata.get_repos(adv)
    # create_missing_repo(repo_list)

    yield {"target": "target_to_pulp2", "file_list": [adv]}

    logging.debug("Teardown")

