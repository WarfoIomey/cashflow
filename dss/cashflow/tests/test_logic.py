from http import HTTPStatus

import pytest
from django.contrib.auth import get_user
from pytest_django.asserts import assertFormError, assertRedirects
from pytest_lazyfixture import lazy_fixture as lf

from cashflow.models import Category, Type, Record, Status, Subcategory

FORM_DATA = {
    'title': 'Название',
    'description': 'Новое описание',
}
ONE_OBJECT: int = 1
pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    'reverse_url, authorization_ulr, model',
    (
        (
            lf('url_reverse_create_type'),
            lf('url_reverse_authorization'),
            Type
        ),
        (
            lf('url_reverse_create_status'),
            lf('url_reverse_authorization'),
            Status
        ),
        (
            lf('url_reverse_create_category'),
            lf('url_reverse_authorization'),
            Category
        ),
        (
            lf('url_reverse_create_subcategory'),
            lf('url_reverse_authorization'),
            Subcategory
        ),
    ),
)
def tests_anonymous_user_cant_create(
    client,
    reverse_url,
    authorization_ulr,
    model,
) -> None:
    """Тест на создание статусов, типов, категорий и подкатегорий анонимном."""
    later_count: int = model.objects.count()
    if model == Category or model == Subcategory:
        FORM_DATA['slug'] = 'test'
    response = client.post(reverse_url, data=FORM_DATA)
    assertRedirects(
        response,
        f'{authorization_ulr}?next={reverse_url}'
    )
    count: int = model.objects.count()
    assert count == later_count


@pytest.mark.parametrize(
    'reverse_url, reverse_url_complete, model',
    (
        (
            lf('url_reverse_create_status'),
            lf('url_reverse_status'),
            Status
        ),
        (
            lf('url_reverse_create_type'),
            lf('url_reverse_type'),
            Type
        ),
        (
            lf('url_reverse_create_category'),
            lf('url_reverse_detail_type'),
            Category
        ),
        (
            lf('url_reverse_create_subcategory'),
            lf('url_reverse_detail_category'),
            Subcategory
        ),
    ),
)
def tests_user_can_create(
    author_client,
    reverse_url,
    reverse_url_complete,
    model,
) -> None:
    """Тест создания статуса, типа, категории и подкатегорий залогиненому."""
    model.objects.all().delete()
    if model == Category or model == Subcategory:
        FORM_DATA['slug'] = 'test'
    response = author_client.post(reverse_url, data=FORM_DATA)
    assertRedirects(response, reverse_url_complete)
    count = model.objects.count()
    assert count == ONE_OBJECT
    object = model.objects.get()
    assert object.description == FORM_DATA['description']
    assert object.title == FORM_DATA['title']
    assert object.user == get_user(author_client)

@pytest.mark.parametrize(
    'reverse_url_detail, object',
    (
        (
            lf('url_reverse_detail_status'),
            lf('status')
        ),
        (
            lf('url_reverse_detail_type'),
            lf('type')
        ),
        (
            lf('url_reverse_detail_category'),
            lf('category')
        ),
        (
            lf('url_reverse_detail_subcategory'),
            lf('subcategory')
        ),
    ),
)
def test_user_cant_viewing_of_another_user(
    another_author_client,
    author_client,
    reverse_url_detail,
    object,
) -> None:
    """Тест просмотр чужих статусов, типов, категорий и подкатегорий."""
    response = another_author_client.get(
        reverse_url_detail
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize(
    'reverse_url_edit, reverse_url_complete, model, object',
    (
        (
            lf('url_reverse_edit_status'),
            lf('url_reverse_detail_status'),
            Status,
            lf('status')
        ),
        (
            lf('url_reverse_edit_type'),
            lf('url_reverse_detail_type'),
            Type,
            lf('type')
        ),
        (
            lf('url_reverse_edit_category'),
            lf('url_reverse_detail_category'),
            Category,
            lf('category')
        ),
        (
            lf('url_reverse_edit_subcategory'),
            lf('url_reverse_detail_subcategory'),
            Subcategory,
            lf('subcategory')
        ),
    ),
)
def test_author_can_edit(
    author_client,
    reverse_url_edit,
    reverse_url_complete,
    model,
    object,
) -> None:
    """Тест на изменения статуса, типа, категории и подкатегорий автором."""
    post_data = {
        'title': object.title,
        'description': FORM_DATA['description']
    }
    if model == Category or model == Subcategory:
        post_data['slug'] = object.slug
    response = author_client.post(reverse_url_edit, data=post_data)
    assertRedirects(response, reverse_url_complete)
    new_object = model.objects.get(id=object.id)
    assert new_object.description == FORM_DATA['description']
    assert new_object.user == object.user
    assert new_object.title == object.title


@pytest.mark.parametrize(
    'reverse_url_delete, reverse_url_complete, model',
    (
        (
            lf('url_reverse_delete_status'),
            lf('url_reverse_status'),
            Status,
        ),
        (
            lf('url_reverse_delete_type'),
            lf('url_reverse_type'),
            Type,
        ),
        (
            lf('url_reverse_delete_category'),
            lf('url_reverse_detail_type'),
            Category,
        ),
        (
            lf('url_reverse_delete_subcategory'),
            lf('url_reverse_detail_category'),
            Subcategory,
        ),
    ),
)
def test_author_can_delete(
    author_client,
    reverse_url_delete,
    reverse_url_complete,
    model,
) -> None:
    """Тест на удаление статуса, типа, категории и подкатегорий автором."""
    later_status_count = model.objects.count()
    response = author_client.delete(reverse_url_delete)
    assertRedirects(response, reverse_url_complete)
    status_count: int = model.objects.count()
    assert status_count == later_status_count - ONE_OBJECT


@pytest.mark.parametrize(
    'reverse_url_delete, model',
    (
        (
            lf('url_reverse_delete_status'),
            Status,
        ),
        (
            lf('url_reverse_delete_type'),
            Type,
        ),
        (
            lf('url_reverse_delete_category'),
            Category,
        ),
        (
            lf('url_reverse_delete_subcategory'),
            Subcategory,
        ),
    ),
)
def test_user_cant_delete_of_another_user(
    another_author_client,
    reverse_url_delete,
    model,
) -> None:
    """Тест на удаление чужого статуса, типа, категории, подкатегории."""
    later_status_count = model.objects.count()
    response = another_author_client.delete(reverse_url_delete)
    assert response.status_code == HTTPStatus.NOT_FOUND
    status_count: int = model.objects.count()
    assert status_count == later_status_count


@pytest.mark.parametrize(
    'reverse_url_edit, model, object',
    (
        (
            lf('url_reverse_edit_status'),
            Status,
            lf('status')
        ),
        (
            lf('url_reverse_edit_type'),
            Type,
            lf('type')
        ),
        (
            lf('url_reverse_edit_category'),
            Category,
            lf('category')
        ),
        (
            lf('url_reverse_edit_subcategory'),
            Subcategory,
            lf('subcategory')
        ),
    ),
)
def test_user_cant_edit_of_another_user(
    another_author_client,
    reverse_url_edit,
    model,
    object,
) -> None:
    """Тест изменение чужих статусов, типов, категорий, подкатегорий."""
    post_data = {
        'title': object.title,
        'description': FORM_DATA['description']
    }
    if model == Category or model == Subcategory:
        post_data['slug'] = object.slug
    response = another_author_client.post(
        reverse_url_edit,
        data=post_data,
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    new_object = model.objects.get(id=object.id)
    assert new_object.title == object.title
    assert new_object.user == object.user
    assert new_object.description == object.description


def tests_user_can_create_record(
    author_client,
    url_reverse_create_record,
    url_reverse_list_record,
    subcategory,
) -> None:
    """Тест создания записи залогиненому."""
    comment: str = 'Тестовый комментарий'
    amount: int = 1000
    Record.objects.all().delete()
    response = author_client.post(
        url_reverse_create_record,
        data={
            'type': subcategory.category.type.id,
            'category': subcategory.category.id,
            'subcategory': subcategory.id,
            'comment': comment,
            'amount': amount,
        }
    )
    assertRedirects(response, url_reverse_list_record)
    count = Record.objects.count()
    assert count == ONE_OBJECT
    object = Record.objects.get()
    assert object.type == subcategory.category.type
    assert object.category == subcategory.category
    assert object.user == get_user(author_client)
    assert object.subcategory == subcategory
    assert object.comment == comment
    assert object.amount == amount


def test_user_cant_edit_record_of_another_user(
    another_author_client,
    url_reverse_edit_record,
    record
) -> None:
    """Тест изменение чужой записм."""
    post_data = {
        'comment': 'Измененный коммент',
        'amount': 500,
    }
    response = another_author_client.post(
        url_reverse_edit_record,
        data=post_data,
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    new_record = Record.objects.get(id=record.id)
    assert new_record.category == record.category
    assert new_record.subcategory == record.subcategory
    assert new_record.type == record.type
    assert new_record.user == record.user
    assert new_record.comment == record.comment
    assert new_record.amount == record.amount


def test_user_cant_delete_of_another_user_record(
    another_author_client,
    url_reverse_delete_record,
    record,
) -> None:
    """Тест на удаление чужой записи."""
    later_record_count = Record.objects.count()
    response = another_author_client.delete(url_reverse_delete_record)
    assert response.status_code == HTTPStatus.NOT_FOUND
    record_count: int = Record.objects.count()
    assert record_count == later_record_count
