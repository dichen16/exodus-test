import pytest
import logging
from client.utils import check_installed_pkg


@pytest.mark.run(order=1)
def test_package_installed():
    # assert check_installed_pkg("rhsm-tools") == True
    pass


@pytest.mark.run(order=1)
def test_pub_ready(pub_endporint_url):
    logging.info("[Prerequisites] pub url is %s", pub_endporint_url)


@pytest.mark.run(order=1)
def test_pulp_ready():
    pass


@pytest.mark.run(order=1)
def test_cdn_ready(cdn_test_url):
    logging.info("[Prerequisites] cdn url is %s", cdn_test_url)
