from typing import List

import pytest
from store_dio.core.exceptions import NotFoundException
from store_dio.schemas.product import ProductOut, ProductUpdateOut
from store_dio.usecases.product import product_usecase

from tests.logger import logger


async def test_usecases_create_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)
    logger.info(result)
    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_success(product_inserted):

    result = await product_usecase.get(puuid=product_inserted.puuid)
    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(puuid="0000f282e20b276900aa8b00")

    assert (
        err.value.message == "Product not found with filter: 0000f282e20b276900aa8b00"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


async def test_usecases_getByFilterPriceBetween_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.getByFilterPriceBetween(pricemin=50.000, pricemax=80.000)

    assert err.value.message == "Product not found with filter"


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_getByFilterPriceBetween_should_return_success():
    result = await product_usecase.getByFilterPriceBetween(
        pricemin=5.000, pricemax=8.000
    )

    assert isinstance(result, List)
    assert len(result) > 1


async def test_usecases_update_should_return_success(product_up, product_inserted):
    product_up.price = "7.500"
    result = await product_usecase.update(puuid=product_inserted.puuid, body=product_up)
    assert result.created_at < result.updated_at
    assert isinstance(result, ProductUpdateOut)


async def test_usecases_update_should_return_not_found(product_up):
    with pytest.raises(NotFoundException) as err:
        await product_usecase.update(puuid="0000f282e20b276900aa8b00", body=product_up)

    assert (
        err.value.message == "Product not found with filter: 0000f282e20b276900aa8b00"
    )


async def test_usecases_delete_should_return_success(product_inserted):
    result = await product_usecase.delete(puuid=product_inserted.puuid)

    assert result is True


async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(puuid="0000f282e20b276900aa8b00")

    assert (
        err.value.message == "Product not found with filter: 0000f282e20b276900aa8b00"
    )
