from flask import Blueprint, render_template, request, redirect, url_for, flash
from wtforms import StringField, SubmitField, SelectField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

from ..models import Attendance

bp_name = "attendances"

bp = Blueprint(bp_name, __name__)
from ..webapp import db
import app

properties = {
    "entity_name": "attendance",
    "collection_name": "Attendances",
    "list_fields": ["id","title", "Student", "enrollment", "presence", "lesson", "rating", "description", "created_at", "updated_at"],
}


class _to:
    def __to(method):
        return lambda **kwargs: url_for(f"{bp_name}.{method}", **kwargs)

    index = __to("index")
    show = __to("show")
    edit = __to("edit")
    delete = __to("delete")


class _j:
    index = f"{bp_name}/index.jinja2"
    edit = f"{bp_name}/edit.jinja2"
    show = f"{bp_name}/show.jinja2"
    new = f"{bp_name}/new.jinja2"
    create = f"{bp_name}/create.jinja2"
    search_tmdb = f"{bp_name}/search_tmdb.jinja2"


@bp.route("/", methods=["GET"])
def index():
    """
    Index page.
    :return: The response.
    """
    attendances = Attendance.query.all()
    return render_template(_j.index, entities=attendances, **properties)


class EditForm(FlaskForm):
    #title = StringField("title", validators=[InputRequired()])
    title = StringField("title")
    rating = StringField("rating")
    description = StringField("description")
    
    #from ..models import Lesson
    #lesson_id = SelectField("lesson", choices=Lesson.query.all() )
    lesson_id = StringField("lesson", validators=[InputRequired()])
    student_id = StringField("student", validators=[InputRequired()])
    enrollment = StringField("enrollment")
    presence = SelectField("presence", choices=[(True, 'Present'), (False, 'Absent'), (False, 'Excused (needs send docs)')], coerce=bool)
    
    
    # with app.webapp.app_context():
    #     lesson = Lesson.query.all()
    #     student = Student.query.all()
    # student = StringField("student")
    # lesson = StringField(f"lesson: Put{lesson.id} for {lesson.title}")
    
    submit = SubmitField("Submit")


@bp.route("/new", methods=["GET"])
def new():
    """
    Page to create new Entity
    :return: render create template
    """
    form = EditForm()
    return render_template(_j.new, form=form, **properties)


@bp.route("/", methods=["POST"])
def create():
    """
    Create new entity
    :return: redirect to view new entity
    """
    form = EditForm(formdata=request.form)
    if form.validate_on_submit():
        newattendance = Attendance()
        form.populate_obj(newattendance)
        db.session.add(newattendance)
        db.session.commit()
        flash(f"'{ newattendance.title}' created")
        return redirect(_to.show(id=newattendance.id))
    else:
        flash("Error in form validation", "danger")


@bp.route("/<int:id>/show", methods=["GET"])
def show(id):
    """
    Show page.
    :return: The response.
    """
    attendance = db.get_or_404(Attendance, id)
    return render_template(_j.show, entity=attendance, **properties)


@bp.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    """
    Edit page.
    :return: The response.
    """
    attendance = db.get_or_404(Attendance, id)
    userform = EditForm(formdata=request.form, obj=attendance)
    return render_template(_j.edit, form=userform, **properties)


@bp.route("/<int:id>/edit", methods=["POST", "UPDATE"])
@bp.route("/<int:id>", methods=["UPDATE"])
def update(id):
    """
    Save Edited Entity
    :return: redirect to show entity
    """
    attendance = db.get_or_404(Attendance, id)
    form = EditForm(formdata=request.form, obj=attendance)
    if form.validate_on_submit():
        form.populate_obj(attendance)
        db.session.commit()
        flash(f"'{ attendance.title}' updated")
        return redirect(_to.show(id=id))
    else:
        flash("Error in form validation", "danger")


@bp.route("/<int:id>/delete", methods=["POST", "DELETE"])
def destroy(id):
    """
    Delete Entity
    :return: redirect to list
    """
    attendance = db.get_or_404(Attendance, id)
    db.session.delete(attendance)
    db.session.commit()
    flash(f"'{ attendance.title}' deleted")
    return redirect(_to.index())
