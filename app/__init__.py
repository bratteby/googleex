# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import logging
import os.path
from flask import Flask, jsonify, request

from .ExempelClass import ExempelClass

def create_app():
    app = Flask(__name__)

    MODEL_PATH = os.path.join(sys.path[0],"app","testmodel.h5")
    r = Recommender(MODEL_PATH)

    @app.route('/')
    def hello():
        """Return a friendly HTTP greeting."""
        return 'Hello World!'

    @app.route('/postrec')
    def postrec():
        res = r.get_recommendations(["13591"])
        return jsonify(res)

    @app.errorhandler(500)
    def server_error(e):
        logging.exception('An error occurred during a request.')
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    return app

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    #app = create_app()
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
