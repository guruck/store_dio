# import warnings
from typing import List
from datetime import datetime
from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import pymongo
from store_dio.db.mongo_db import db_client
from store_dio.models.product import ProductModel
from store_dio.schemas.product import (
    ProductIn,
    ProductOut,
    ProductUpdate,
    ProductUpdateOut,
)
from store_dio.core.exceptions import NotFoundException


class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())
        res = await self.collection.insert_one(product_model.model_dump())
        outobj = product_model.model_dump()
        outobj["puuid"] = str(res.inserted_id)

        return ProductOut(**outobj)

    async def get(self, puuid: str) -> ProductOut:
        # warnings.warn(UserWarning("api v1, should use functions from v2"))
        pid = ObjectId(puuid)
        result = await self.collection.find_one({"_id": pid})

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {puuid}")
        objid = result.pop("_id")
        result["puuid"] = str(objid)

        return ProductOut(**result)

    async def getByFilterPriceBetween(
        self, pricemin: float, pricemax: float
    ) -> List[ProductOut]:
        # warnings.warn(UserWarning("api v1, should use functions from v2"))
        result: List[ProductOut] = []
        filter_query = {"price": {"$gte": pricemin, "$lt": pricemax}}
        async for item in self.collection.find(filter_query):
            objid = item.pop("_id")
            item["puuid"] = str(objid)
            result.append(ProductOut(**item))

        if not result:
            raise NotFoundException(message="Product not found with filter")

        return result

    async def query(self) -> List[ProductOut]:
        result: List[ProductOut] = []
        async for item in self.collection.find():
            objid = item.pop("_id")
            item["puuid"] = str(objid)
            result.append(ProductOut(**item))

        return result

    async def update(self, puuid: str, body: ProductUpdate) -> ProductUpdateOut:
        pid = ObjectId(puuid)
        body.updated_at = datetime.now()
        result = await self.collection.find_one_and_update(
            filter={"_id": pid},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )
        if not result:
            raise NotFoundException(message=f"Product not found with filter: {puuid}")

        objid = result.pop("_id")
        result["puuid"] = str(objid)
        return ProductUpdateOut(**result)

    async def delete(self, puuid: str) -> bool:
        pid = ObjectId(puuid)
        product = await self.collection.find_one({"_id": pid})
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {pid}")

        result = await self.collection.delete_one({"_id": pid})

        return True if result.deleted_count > 0 else False


product_usecase = ProductUsecase()
