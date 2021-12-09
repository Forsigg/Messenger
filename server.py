import uuid

from pathlib import Path
from typing import Any, AsyncIterable, Dict, Iterable

from aiohttp import web
from aiohttp_swagger import *

import aiohttp_jinja2
import jinja2

from data.users_data.datausersmanager import DataUsersManager
from data.users_data.abstract_datamanager import AbstractDataManager
from user_data import User


routes = web.RouteTableDef()


# async def __to_list(iterable: AsyncIterable[Any]) -> Iterable[Any]:
#     return [item async for item in iterable]

@routes.get('/')
async def root(_request: web.Request) -> web.Response:
    raise web.HTTPFound(location='/users')

@routes.get('/users')
@aiohttp_jinja2.template('users.jinja2')
async def get_users(request: web.Request) -> Dict[str, Any]:
    db = DataUsersManager()

    return{
        'name': 'Users Manager',
        'users':  db.get_all()
    }

@routes.post('/users')
async def add_user(request: web.Request) -> web.Response:
    storage: DataUsersManager = request.app['storage']

    data = dict(await request.post())
    user = User(**data)
    await storage.add_one(user)

    return web.HTTPFound(location=f'/users')

if __name__ == '__main__':
    templates_directory =Path(__file__).parent.joinpath('server_templates')

    app = web.Application()
    db = DataUsersManager()
    app['storage'] = db.connect()

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(templates_directory)))
    app.add_routes(routes)

    web.run_app(app, port=8080)
