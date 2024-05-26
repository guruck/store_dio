from pydantic import ValidationError

import pytest
from store_dio.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_success():
    data = product_data()
    # product = ProductIn(**data)
    product = ProductIn.model_validate(data)

    assert product.name == "Iphone 14 Pro Max"
    # assert isinstance(product.puuid, UUID)


def test_schemas_return_raise():
    data = {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": 8500.00,
    }

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": data,
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }