import pytest
from django.test.client import Client
from django.conf import settings
from django.urls import reverse

from cashflow.models import Category, Type, Record, Status, Subcategory


@pytest.fixture
def author(django_user_model):
    """Текущий пользователь."""
    return django_user_model.objects.create(username='User')


@pytest.fixture
def another_author(django_user_model):
    """Другой пользователь."""
    return django_user_model.objects.create(username='Другой')


@pytest.fixture
def another_author_client(another_author):
    """Клиент другого пользователя."""
    client = Client()
    client.force_login(another_author)
    return client


@pytest.fixture
def author_client(author):
    """Клиент текущего пользователя."""
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def type(author):
    """Создание типа."""
    type = Type.objects.create(
        title='Заголовок',
        user=author,
        description='Описание типа',
    )
    return type


@pytest.fixture
def category(author, type):
    """Создание категории."""
    category = Category.objects.create(
        title='Заголовок',
        user=author,
        description='Описание категории',
        type=type,
        slug='test',
    )
    return category


@pytest.fixture
def subcategory(author, category):
    """Создание подкатегории."""
    subcategory = Subcategory.objects.create(
        title='Заголовок',
        user=author,
        description='Описание подкатегории',
        category=category,
        slug='test',
    )
    return subcategory


@pytest.fixture
def status(author):
    """Создание статуса."""
    status = Status.objects.create(
        title='Заголовок',
        user=author,
        description='Описание статуса',
    )
    return status


@pytest.fixture
def record(author, status, type, category, subcategory):
    """Создание записи."""
    status = Record.objects.create(
        user=author,
        status=status,
        type=type,
        category=category,
        subcategory=subcategory,
        comment='Тестовый комментарий',
        amount=1000
    )
    return status


@pytest.fixture
def three_status(author) -> None:
    """Создание трёх статусов."""
    all_status = [
        Status(
            title=f'Статус {index}',
            description='Просто описание.',
            user=author,
        )
        for index in range(settings.PAGINATIONS + 1)
    ]
    Status.objects.bulk_create(all_status)


@pytest.fixture
def three_type(author) -> None:
    """Создание трёх типов."""
    all_types = [
        Type(
            title=f'Тип {index}',
            description='Просто описание.',
            user=author,
        )
        for index in range(settings.PAGINATIONS + 1)
    ]
    Type.objects.bulk_create(all_types)


@pytest.fixture
def url_reverse_list_record() -> str:
    return reverse('cashflow:index')


@pytest.fixture
def url_reverse_create_record() -> str:
    return reverse('cashflow:create_record')


@pytest.fixture
def url_reverse_detail_record(record) -> str:
    return reverse('cashflow:record_detail', args=(record.id,))


@pytest.fixture
def url_reverse_edit_record(record) -> str:
    return reverse('cashflow:edit_record', args=(record.id,))


@pytest.fixture
def url_reverse_delete_record(record) -> str:
    return reverse('cashflow:delete_record', args=(record.id,))


@pytest.fixture
def url_reverse_authorization() -> str:
    """Ссылка на страницу авторизации."""
    return reverse(settings.LOGIN_URL)


@pytest.fixture
def url_reverse_create_subcategory(category) -> str:
    """Ссылка на страницу создания подкатегории."""
    return reverse(
        'cashflow:create_subcategory',
        args=(category.type.pk, category.slug)
    )


@pytest.fixture
def url_reverse_detail_subcategory(subcategory) -> str:
    """Ссылка на страницу подкатегории."""
    return reverse(
        'cashflow:subcategory_detail',
        args=(
            subcategory.category.type.pk,
            subcategory.category.slug,
            subcategory.slug
        )
    )


@pytest.fixture
def url_reverse_edit_subcategory(subcategory) -> str:
    """Ссылка на страницу редактирования подкатегории."""
    return reverse(
        'cashflow:edit_subcategory',
        args=(
            subcategory.category.type.pk,
            subcategory.category.slug,
            subcategory.slug
        )
    )


@pytest.fixture
def url_reverse_delete_subcategory(subcategory) -> str:
    """Ссылка на страницу уадления подкатегории."""
    return reverse(
        'cashflow:delete_subcategory',
        args=(
            subcategory.category.type.pk,
            subcategory.category.slug,
            subcategory.slug
        )
    )


@pytest.fixture
def url_reverse_type() -> str:
    """Ссылка на страницу с типами."""
    return reverse('cashflow:type')


@pytest.fixture
def url_reverse_create_type(type) -> str:
    """Ссылка на страницу создания типов."""
    return reverse('cashflow:create_type')


@pytest.fixture
def url_reverse_edit_type(type) -> str:
    """Ссылка на страницу редактирования типов."""
    return reverse('cashflow:edit_type', args=(type.pk,))


@pytest.fixture
def url_reverse_delete_type(type) -> str:
    """Ссылка на страницу удаления типов."""
    return reverse('cashflow:delete_type', args=(type.pk,))


@pytest.fixture
def url_reverse_detail_type(type) -> str:
    """Ссылка на страницу типа."""
    return reverse('cashflow:type_detail', args=(type.pk,))


@pytest.fixture
def url_reverse_create_category(type) -> str:
    """Ссылка на страницу создания категории."""
    return reverse('cashflow:create_category', args=(type.pk,))


@pytest.fixture
def url_reverse_edit_category(category) -> str:
    """Ссылка на страницу редактирования категории."""
    return reverse(
        'cashflow:edit_category',
        args=(category.type.pk, category.slug)
    )


@pytest.fixture
def url_reverse_detail_category(category) -> str:
    """Ссылка на страницу категории."""
    return reverse(
        'cashflow:category_detail',
        args=(category.type.pk, category.slug)
    )


@pytest.fixture
def url_reverse_delete_category(category) -> str:
    """Ссылка на страницу удаления категории."""
    return reverse(
        'cashflow:delete_category',
        args=(category.type.pk, category.slug)
    )


@pytest.fixture
def url_reverse_status() -> str:
    """Ссылка на страницу списка статусов."""
    return reverse('cashflow:status')


@pytest.fixture
def url_reverse_detail_status(status) -> str:
    """Ссылка на страницу статуса."""
    return reverse('cashflow:status_detail', args=(status.pk,))


@pytest.fixture
def url_reverse_create_status(status) -> str:
    """Ссылка на страницу создания статусов."""
    return reverse('cashflow:create_status')


@pytest.fixture
def url_reverse_edit_status(status) -> str:
    """Ссылка на страницу редактирование статуса."""
    return reverse('cashflow:edit_status', args=(status.pk,))


@pytest.fixture
def url_reverse_delete_status(status) -> str:
    """Ссылка на страницу удаления статуса."""
    return reverse('cashflow:delete_status', args=(status.pk,))
