from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
def page_list():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>/')
def page_candidate(candidate_id):
    candidate = utils.get_candidate(candidate_id)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>/')
def page_search(candidate_name):
    needed_candidates = utils.get_candidates_by_name(candidate_name)
    number_of_candidates = len(needed_candidates)
    return render_template('search.html', needed_candidates=needed_candidates,
                           number_of_candidates=number_of_candidates)


@app.route('/skill/<skill_name>/')
def page_skill(skill_name):
    needed_candidates = utils.get_candidates_by_skill(skill_name)
    number_of_candidates = len(needed_candidates)
    return render_template('skill.html', needed_candidates=needed_candidates,
                           number_of_candidates=number_of_candidates, skill_name=skill_name)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
