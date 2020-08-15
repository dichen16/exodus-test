import pytest
import logging

from client.pub import PubClient
from client.errata import ErrataHelper


@pytest.fixture(scope="session")
def testdata_pub(pub_endporint_url):
    logging.debug("[---] testdata_pub is called")
    return PubClient(pub_endporint_url, "user", "password")


@pytest.fixture(scope="session")
def testdata_errata(errata_endporint_url):
    logging.debug("[---] testdata_errata is called")
    return ErrataHelper.from_endpoint_url(endpoint_url=errata_endporint_url)
