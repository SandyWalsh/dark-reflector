# Copyright 2011 Dark Secret Software Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.import datetime

import pyactiveresource.activeresource as AR
from flask import Flask
from launchpadlib.launchpad import Launchpad as LP


app = Flask(__name__)

use_redmine = False
try:
    import config
    use_redmine = True
except ImportError, e:
    pass

if use_redmine:
    class Issue(AR.ActiveResource):
        _site = config.redmine_site
        _user = config.redmine_user
        _password = config.redmine_password


    @app.route('/redmine/<int:ticket_id>')
    def redmine_ticket(ticket_id=None):
        return Issue.find(ticket_id).description


@app.route('/launchpad/<int:ticket_id>')
def launchpadticket(ticket_id=None):
    launchpad = LP.login_anonymously("dark-reflector", "production")
    return launchpad.bugs[1].title


if __name__ == '__main__':
    app.debug = True
    app.run()
