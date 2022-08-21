from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

items=[]
class ItemList(Resource):
    def get(self):
        return {'items':items}


class Item(Resource):
    def get(self,name):
        for item in items:
            if item['name'] == name:
                return item
        return {'name':None} , 404

    def post(self,name):
        data = request.get_json(silent=True)
        item = {'name':data['name'],'price':data['price']}
        item ={'name':name, 'price':10.0}
        items.append(item)
        return item, 201

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
app.run(port=5000,debug=True)