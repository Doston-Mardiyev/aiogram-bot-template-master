from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        phone_number varchar(255) NULL,
        ariza varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE 
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username,  telegram_id):
        sql = "INSERT INTO users (full_name, username,  telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_phone_number(self, phone_number, telegram_id):
        sql = "UPDATE Users SET phone_number=$2 WHERE telegram_id=$4"
        return await self.execute(sql, phone_number, telegram_id, execute=True)

    async def update_ariza(self, ariza, telegram_id):
        sql = "UPDATE Users SET ariza=$3 WHERE telegram_id=$4"
        return await self.execute(sql, ariza, telegram_id, execute=True)


    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    



    ### ==================Mahsulotlar uchun jadval (table) yaratamiz============================
    async def create_table_products(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Products (
        id SERIAL PRIMARY KEY,
        
        -- Mahsulot kategoriyasi
        category_name VARCHAR(50) NOT NULL,

        
        -- Mahsulot haqida malumot
        service_name VARCHAR(50) NOT NULL,
        photo varchar(255) NULL,
        description VARCHAR(3000) NULL
        );
        """
        await self.execute(sql, execute=True)

    async def add_product(
        self,
        category_name,
        service_name,
        photo=None,
        description="",
    ):
        sql = "INSERT INTO Products ( category_name, service_name, photo,  description) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(
            sql,
            category_name,
            service_name,
            photo,
            description,
            fetchrow=True,
        )

    # async def get_categories(self):
    #     sql = "SELECT DISTINCT category_name, category_code FROM Products"
    #     return await self.execute(sql, fetch=True)

    
    # async def count_products(self, category_code, subcategory_code=None):
    #     if subcategory_code:
    #         sql = f"SELECT COUNT(*) FROM Products WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
    #     else:
    #         sql = f"SELECT COUNT(*) FROM Products WHERE category_code='{category_code}'"
    #     return await self.execute(sql, fetchval=True)

    # async def get_products(self, category_code, subcategory_code):
    #     sql = f"SELECT * FROM Products WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
    #     return await self.execute(sql, fetch=True)

    # async def get_product(self, product_id):
    #     sql = f"SELECT * FROM Products WHERE id={product_id}"
    #     return await self.execute(sql, fetchrow=True)

    async def drop_products(self):
        await self.execute("DROP TABLE Products", execute=True)