from flask import Flask, request, render_template
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class User:

    def get(self,):
        return {"name": "John"}

    def post(self):
        request_data = request.get_json()
        return {"name": request_data["name"], "data": request_data}

api.add_resource(User, '/user')

app.run(port=5000, debug=True)