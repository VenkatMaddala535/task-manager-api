from flask import Blueprint, jsonify, request

from .database import db
from .models import Task

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify({
        "message": "Task Manager API",
        "status": "running"
    })


@main.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@main.route("/tasks", methods=["GET"])
def get_tasks():

    tasks = Task.query.all()

    return jsonify([task.to_dict() for task in tasks])


@main.route("/tasks", methods=["POST"])
def create_task():

    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({
            "error": "Title is required"
        }), 400

    task = Task(
        title=data["title"],
        description=data.get("description", "")
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201