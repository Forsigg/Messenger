import uuid

from pathlib import Path
from typing import Any, AsyncIterable, Dict, Iterable

from aiohttp import web
from aiohttp_swagger import *

import aiohttp_jinja2
import jinja2

import json

from data.users_data.datausersmanager import DataUsersManager
from user_data import User


routes = web.RouteTableDef()


# async def __to_list(iterable: AsyncIterable[Any]) -> Iterable[Any]:
#     return [item async for item in iterable]

@routes.get('/')
async def root(_request: web.Request) -> web.Response:
    raise web.HTTPFound(location='/users')

@routes.get('/users')
@aiohttp_jinja2.template('users.jinja2')
async def get_users(request: web.Request) -> web.json_response:
    db = DataUsersManager()
    data = {'name': 'User manager',
            'users': db.get_all()}

    return web.json_response(json.dumps(data))

@routes.post('/users/{main_user}')
async def auth(request: web.Request) -> web.Response:
    storage = DataUsersManager()

    data = dict(await request.post())
    user = User(**data)
    await storage.add_one(user)

    return web.HTTPFound(location=f'/users')

if __name__ == '__main__':
    templates_directory =Path(__file__).parent.joinpath('server_templates')

    app = web.Application()

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(templates_directory)))
    app.add_routes(routes)

    web.run_app(app, host='localhost', port=8080)
