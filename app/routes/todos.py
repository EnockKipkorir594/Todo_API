from flask import Blueprint, request, jsonify
from app.extensions import db 
from app.models import Todo, todo_schema, todos_schema
from marshmallow import ValidationError


todos_bp = Blueprint("todos", __name__, url_prefix="/todos")

@todos_bp.route("/", methods=['GET'])
def get_todos():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return todos_schema.jsonify(todos), 200


@todos_bp.route("/<int:todo_id>", methods=['GET'])
def get_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id, description="Todo not found")
    return todo_schema.jsonify(todo), 200

@todos_bp.route('/', methods=['POST'])
def create_todo():
    json_data = request.get_json()
    
    if not json_data:
        return jsonify({"Error": "No input data provided"})
    
    try:
        todo = todo_schema.load(json_data, session = db.session)
    except ValidationError as err:
        return jsonify({"Errors": err.messages}), 442
    
    db.session.add(todo)
    db.session.commit()
    return todo_schema.jsonify(todo), 201 

@todos_bp.route("/<int:todo_id>", methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id, description="Todo not found")
    json_data = request.get_json()
    if not json_data:
        return jsonify({"error":"No data input provided"})
    
    try :
        todo = todo_schema.load(json_data, instance=todo, partial=True, session=db.session)
        
    except ValidationError as err:
        return jsonify({"Erros": err.messages}), 442
    
    db.session.commit()
    return todo_schema.jsonify(todo), 200
    

@todos_bp.route("/<int:todo_id>", methods= ['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id, description="Todo not found")
    db.session.delete(todo)
    db.session.commit()
    
    return jsonify({"Message":f"Todo {todo_id} deleted successfully"}), 200

