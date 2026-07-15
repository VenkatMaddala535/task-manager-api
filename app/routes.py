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


# -------------------------
# GET ALL TASKS
# -------------------------
@main.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])


# -------------------------
# GET ONE TASK
# -------------------------
@main.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):

    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task.to_dict())


# -------------------------
# CREATE TASK
# -------------------------
@main.route("/tasks", methods=["POST"])
def create_task():

    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    task = Task(
        title=data["title"],
        description=data.get("description", "")
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201


# -------------------------
# UPDATE TASK
# -------------------------
@main.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):

    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.completed = data.get("completed", task.completed)

    db.session.commit()

    return jsonify(task.to_dict())


# -------------------------
# DELETE TASK
# -------------------------
@main.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):

    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Task deleted successfully"
    })