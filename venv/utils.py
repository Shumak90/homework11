from bdms import candidates_json

candidates = candidates_json()
def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    candidate_list = []
    for candidate in candidates:
        candidate_list.append(candidate)
    return candidate_list


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    for candidate in candidates:
        if int(candidate_id) == candidate["id"]:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidate_list = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidate_list.append(candidate["name"])
    return candidate_list


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidate_list = []
    for candidate in candidates:
        for skill in candidate["skills"].split(", "):
            if skill_name.lower() == skill.lower():
                candidate_list.append(candidate["name"])
    return candidate_list

