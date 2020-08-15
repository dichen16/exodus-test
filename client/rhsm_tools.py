import subprocess
import logging


def create_missing_repo(repos):
    logging.debug(
        "[Dry run] Execute rhsm-pulp-manager-v2 to prepare required pulp repo %s",
        str(repos),
    )

    cmd = (
        "rhsm-pulp-manager-v2 --eng-server prod --pulp-server test1"
        "--create-missing-repos --use-cached-pp"
        "--no-tps --repo XXXXXXXXXX"
    )

    """
    res = subprocess.run(cmd, shell=True, capture_output=True)
    if res.returncode:
        return False
    return True
    """

    return True

