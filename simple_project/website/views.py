from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if len(note) < 1:
            flash("Note is too short.", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")
    
    return render_template("index.html", user=current_user)

@views.route("/delete-note", methods=["POST"])
def delete_note():
    data = json.loads(request.data)
    noteId = data["noteId"]
    del_note = Note.query.get(noteId)
    if del_note:
        if del_note.user_id == current_user.id:
            db.session.delete(del_note)
            db.session.commit()
    
    return jsonify({})