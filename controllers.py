from app import app,db
from flask import render_template, jsonify,request
from models import *
import requests
from access_token import *
from sqlalchemy import func

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message" : "Hello World"})


@app.route('/jobs', methods=['GET'])
def all_jobs():
    all_jobs = Job.query.all() #select * from job
    return jsonify(all_jobs=[e.serialize() for e in all_jobs])

@app.route('/jobs/autocomplete', methods=['GET'])
def auto_complete():
    start = request.args.get('begins_with')
    middle = request.args.get('contains')
    ending = request.args.get('ends_with')
    matching_jobs = Job.query.filter(Job.title.ilike(start + "%" + middle + "%" + ending)).all()
    return jsonify(matching_jobs=[e.serialize() for e in matching_jobs])


@app.route('/skills/<int:id>/related_skills', methods=['GET'])
def related_skills(id):
    skill = Skill.query.filter_by(id=id).first()
    dict_to_send = {
  "input" : {
    "skill" : [skill.title]
  }
}
    res = requests.post('https://qa-apis.burning-glass.com/v3.2/similarity/skills',headers={'Authorization': access_key},json=dict_to_send)
    return jsonify(res.json())