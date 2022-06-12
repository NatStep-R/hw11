import json
path = "candidates.json"


def load_candidates_from_json():
    """возвращает список всех кандидатов"""
    with open(path, 'r', encoding='utf=8') as file:
        candidates = json.load(file)
        return candidates


def get_candidate(candidate_id):
    """возвращает кандидата по айди"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate.get("id") == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает список кандидатов по имени"""
    candidates = load_candidates_from_json()
    needed_candidates = []
    for candidate in candidates:
        if candidate_name.lower() in candidate.get("name").lower():
            needed_candidates.append(candidate)

    return needed_candidates


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidates = load_candidates_from_json()
    skill_name = skill_name.lower()
    needed_candidates = []
    for candidate in candidates:
        skills = candidate.get("skills").lower().split(", ")
        if skill_name in skills:
            needed_candidates.append(candidate)

    return needed_candidates
