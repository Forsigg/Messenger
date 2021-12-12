import uuid

from pathlib import Path
from typing import Any, AsyncIterable, Dict, Iterable

from aiohttp import web
from aiohttp_swagger import *

import aiohttp_jinja2
import jinja2

import json

from data.users_data.datausersmanager import DataUsersManager
from data.messages import MessageManager


routes = web.RouteTableDef()


@routes.get('/')
async def root(_request: web.Request) -> web.Response:
    raise web.HTTPFound(location='/users')

@routes.get('/users')
async def get_users(_request: web.Request) -> web.json_response:
    db = DataUsersManager()
    users = [user[0] for user in db.get_all()]

    json_users = json.dumps(users)

    return web.json_response(json_users)

@routes.get('/users/{user}')
async def auth(_request: web.Request) -> web.Response:
    db = DataUsersManager()

    if db.get_one(_request.match_info['user']):
        return web.json_response(json.dumps(_request.match_info['user']))
    else:
        raise web.HTTPNotFound()


@routes.get('/users/{user_in}/{user_out}')
async def get_messages(_request: web.Request) -> web.json_response:
    db = MessageManager(_request.match_info['user_in'], _request.match_info['user_out'])
    messages = json.dumps(db.get_all())

    return web.json_response(messages)

@routes.post('/users/{user_in}/{user_out}/{text}')
async def send_message(_request: web.Request) -> web.json_response:
    db = MessageManager(_request.match_info['user_in'], _request.match_info['user_out'])

    message = dict(await _request.post())
    db.send_message(**message)

    return web.HTTPFound(location=r'/users/{user_in}/{user_out}')



if __name__ == '__main__':
    templates_directory =Path(__file__).parent.joinpath('server_templates')

    app = web.Application()

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(templates_directory)))
    app.add_routes(routes)

    web.run_app(app, host='localhost', port=8080)
