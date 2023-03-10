"""module mongodb_crud_utils. Simple utilities
for querying MongoDB

"""
import datetime
from typing import List
from mir_persistence_layer_utils.dbs.mongodb_session import MongoDBSession


class CreateEntityBaseCRUDAPI(object):
    """Create queries in the DB

    """

    @staticmethod
    def do_insert_one(data: dict, db_session: MongoDBSession, collection_name: str):
        data['created_at'] = datetime.datetime.utcnow()
        data['updated_at'] = datetime.datetime.utcnow()
        result = db_session.db[collection_name].insert_one(data)
        return result

    @staticmethod
    def do_insert_many(data: List[dict], db_session: MongoDBSession, collection_name: str):

        for item in data:
            item['created_at'] = datetime.datetime.utcnow()
            item['updated_at'] = datetime.datetime.utcnow()

        return db_session.db[collection_name].insert_many(data)


class ReadEntityBaseCRUDAPI(object):
    """Read queries in the DB

    """

    @staticmethod
    def do_find(criteria: dict, db_session: MongoDBSession,
                projection: dict,
                collection_name: str):
        result = db_session.db[collection_name].find(criteria, projection=projection)
        return result

    @staticmethod
    def do_find_one(criteria: dict, db_session: MongoDBSession,
                    projection: dict, collection_name: str):
        result = db_session.db[collection_name].find_one(criteria, projection=projection)
        return result


class UpdateEntityCRUDAPI(object):
    """Update queries in the DB

    """
    @staticmethod
    def do_update_one(criteria: dict, update_data: dict,
                      db_session: MongoDBSession,
                      collection_name: str,
                      upsert: bool = False):

        update_data['updated_at'] = datetime.datetime.utcnow()
        result = db_session.db[collection_name].update_one(criteria, {"$set": update_data},
                                                           upsert=upsert)
        return result


class DeleteEntityCRUDAPI(object):
    """Delete queries in the DB

    """
    @staticmethod
    def do_delete_one(criteria: dict, db_session: MongoDBSession,
                      collection_name: str):
        result = db_session.db[collection_name].delete_one(criteria)
        return result

    @staticmethod
    def do_delete(criteria: dict, db_session: MongoDBSession, collection_name: str):
        return db_session.db[collection_name].delete_many(criteria)
