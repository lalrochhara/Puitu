#  OpenGM - Powerful  Telegram group managment bot
#  Copyright (C) 2017 - 2019 Paul Larsen
#  Copyright (C) 2019 - 2023 Nicky Lalrochhara
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from flask import Flask
from flask_restplus import Api
from puitu.restapi.resources.basic import basic_api
from puitu.restapi.resources.chats import chats_api
import puitu.restapi.resources.management as management
import puitu.restapi.resources.modules.admin as admin

app = Flask("Puitu Telegram Bot")
api = Api(app, version="2.0 Development Preview 1", title="Puitu Telegram Bot")

api.add_namespace(basic_api)
api.add_namespace(chats_api)
api.add_namespace(management.api)
api.add_namespace(admin.api)