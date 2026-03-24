from datetime import datetime
from app.extensions import db, ma 

class Todo(db.Model):
    
    __tablename__ = "todos"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    
    def __repr__(self):
        return f'<Todo {self.id} : {self.title}'
    
class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todo 
        load_instance = True
        
    id = ma.auto_field(dump_only=True)
    created_at = ma.auto_field(dump_only=True) 
    updated_at = ma.auto_field(dump_only=True)
    
todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)