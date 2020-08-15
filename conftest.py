import pytest

pytest_plugins = ["fixtures.fixture_prepare", "fixtures.fixture_testdata"]


def pytest_addoption(parser):
    parser.addoption(
        "--cdn-test-url",
        action="store",
        help="enable integration tests against this CDN",
    )
    parser.addoption(
        "--pub-endporint-url",
        action="store",
        help="enable integration tests against this Pub",
    )
    parser.addoption(
        "--errata-endporint-url",
        action="store",
        help="enable integration tests against this Errata",
    )


@pytest.fixture(scope="session")
def cdn_test_url(request):
    url = request.config.getoption("--cdn-test-url")
    if url:
        return url
    else:
        return "https://default.cdn.com"


@pytest.fixture(scope="session")
def pub_endporint_url(request):
    url = request.config.getoption("--pub-endporint-url")
    if url:
        return url
    else:
        return "http://default.pub.com/pub/"


@pytest.fixture(scope="session")
def errata_endporint_url(request):
    url = request.config.getoption("--errata-endporint-url")
    if url:
        return url
    else:
        return "http://default.errata.com/errata/"

