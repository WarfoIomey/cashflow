import pytest
from django.conf import settings
from pytest_lazyfixture import lazy_fixture as lf


pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    'url_reverse, check_object',
    (
        (
            lf('url_reverse_status'),
            lf('three_status'),
        ),
        (
            lf('url_reverse_type'),
            lf('three_type'),
        ),
    ),
)
def test_status_count(
    url_reverse,
    check_object,
    author_client,
) -> None:
    """Тест на корректность количества отображаемых статусов."""
    response = author_client.get(url_reverse)
    object_list = response.context['object_list']
    status_count: int = object_list.count()
    assert status_count == settings.PAGINATIONS

