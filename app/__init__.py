from flask import Flask, request, jsonify
from flask_restx import Resource, Api, fields

app = Flask(__name__)
api = Api(app)

# Local storage for todos
todos = {}

# Model for the API documentation
todo_model = api.model('Todo', {
    'id': fields.String(required=True, description='The todo identifier'),
    'title': fields.String(required=True, description='The title of the todo'),
    'description': fields.String(required=False, description='The description of the todo')
})

ns = api.namespace('todos', description='Todo operations')

@ns.route('/')
class TodoList(Resource):
    @ns.marshal_list_with(todo_model)
    def get(self):
        """List all todos"""
        return list(todos.values()), 200

    @ns.expect(todo_model)
    @ns.marshal_with(todo_model, code=201)
    def post(self):
        """Create a new todo"""
        data = request.json
        todo_id = data['id']
        if todo_id in todos:
            return {"message": "Todo with this ID already exists."}, 400
        
        todos[todo_id] = {
            'id': todo_id,
            'title': data['title'],
            'description': data.get('description', '')
        }
        return todos[todo_id], 201

@ns.route('/<string:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The todo identifier')
class TodoResource(Resource):
    @ns.marshal_with(todo_model)
    def get(self, id):
        """Fetch a todo given its identifier"""
        if id in todos:
            return todos[id], 200
        return {"message": "Todo not found"}, 404

    @ns.expect(todo_model)
    @ns.marshal_with(todo_model)
    def put(self, id):
        """Update a todo given its identifier"""
        if id not in todos:
            return {"message": "Todo not found"}, 404
        
        data = request.json
        todos[id] = {
            'id': id,
            'title': data['title'],
            'description': data.get('description', '')
        }
        return todos[id], 200

    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        """Delete a todo given its identifier"""
        if id not in todos:
            return {"message": "Todo not found"}, 404
        
        del todos[id]
        return '', 204

api.add_namespace(ns)