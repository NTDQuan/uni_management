from database.initSession import session
from university_management.src.model.Model import Major

def get_all_major():
    result = session.query(Major).all()
    major_list = []
    for row in result:
        major_list.append(row.major_name)
    return major_list

def get_major_id(major_name):
    print("Get major id...")
    result = session.query(Major).filter(Major.major_name == major_name).first()
    print(result.major_id)
    return result.major_id
