from pathlib import Path

from aiohttp import web

import aiohttp_jinja2
import jinja2

import json

from data.users_data.datausersmanager import DataUsersManager
from data.messages import MessageManager
from data.messages import Message
from user_data import User

import server_config


routes = web.RouteTableDef()
db = DataUsersManager()


@routes.get('/')
async def root(_request: web.Request) -> web.Response:
    raise web.HTTPFound(location='/users')

@routes.get('/users')
async def get_users(_request: web.Request) -> web.json_response:
    users = [user[0] for user in db.get_all()]

    json_users = json.dumps(users)

    return web.json_response(json_users)

@routes.get('/users/{user}')
async def auth(_request: web.Request) -> web.Response:
    if db.get_one(_request.match_info['user']):
        return web.json_response(json.dumps(_request.match_info['user']))
    else:
        raise web.HTTPNotFound()


@routes.get('/users/{user}/auth')
async def is_right_password(_request: web.Request) -> web.Response:
    data_json = json.dumps(db.get_one(_request.match_info['user']))

    return web.json_response(data_json)



@routes.get('/users/{user_in}/{user_out}')
async def get_messages(_request: web.Request) -> web.json_response:
    db = MessageManager(_request.match_info['user_in'], _request.match_info['user_out'])
    messages = json.dumps(db.get_all())

    return web.json_response(messages)

@routes.post('/users/{user_in}/{user_out}/send')
async def send_message(_request: web.Request) -> web.json_response:
    db_messages = MessageManager(_request.match_info['user_in'], _request.match_info['user_out'])

    message = dict(await _request.post())
    data = Message(message['text'], message['author'], message['receiver'], message['date'])
    db_messages.send_message(data)

    raise web.HTTPFound(location=r'/users/{user_in}/{user_out}')

@routes.post('/users')
async def add_user(_request: web.Request) -> web.json_response:
    user = dict(await _request.post())
    data = User(user['login'], user['password'])
    db.add_one(data.login, data.password)

    raise web.HTTPFound(location='/users')




if __name__ == '__main__':
    templates_directory =Path(__file__).parent.joinpath('server_templates')

    app = web.Application()

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(templates_directory)))
    app.add_routes(routes)

    web.run_app(app, host=server_config.host, port=int(server_config.port))
