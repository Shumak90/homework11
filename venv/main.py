from flask import Flask, render_template
from bdms import candidates_json
from utils import *

app = Flask(__name__)


@app.route("/")
def hello():
    candidate_list = []
    candidates = load_candidates_from_json(candidates_json())
    for candidate in candidates:
        candidate_list.append(candidate["name"])

    return render_template("list.html", candidates = candidate_list)

@app.route("/candidate/<x>")
def candidate(x):
    name = get_candidate(x)["name"]
    position = get_candidate(x)["position"]
    picture = get_candidate(x)["picture"]
    skills = get_candidate(x)["skills"]
    return render_template("single.html", name = name, position = position, picture = picture, skills = skills)

@app.route("/search/<candidate_name>")
def candidate_name(candidate_name):
    candidate = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidate_list=candidate, flag=len(candidate))

@app.route("/skill/<skill_name>")
def skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill_name = skill_name, candidates = candidates, flag = len(candidates))

if __name__ == "__main__":
    app.run(debug=True)
