from http import HTTPStatus

import pytest
from pytest_lazyfixture import lazy_fixture as lf


pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    'reverse_url, parametrized_client, expected_status',
    (
        (
            lf('url_reverse_edit_subcategory'),
            lf('another_author_client'),
            HTTPStatus.NOT_FOUND
        ),
        (
            lf('url_reverse_delete_subcategory'),
            lf('another_author_client'),
            HTTPStatus.NOT_FOUND
        ),
        (
            lf('url_reverse_edit_subcategory'),
            lf('author_client'),
            HTTPStatus.OK
        ),
        (
            lf('url_reverse_delete_subcategory'),
            lf('author_client'),
            HTTPStatus.OK
        ),
        (
            lf('url_reverse_detail_subcategory'),
            lf('author_client'),
            HTTPStatus.OK
        ),
        (
            lf('url_reverse_authorization'),
            lf('client'),
            HTTPStatus.OK
        ),
    ),
)
def test_availability(
    reverse_url: str,
    parametrized_client,
    expected_status,
) -> None:
    """Тесты на доступность."""
    response = parametrized_client.get(reverse_url)
    assert response.status_code == expected_status

