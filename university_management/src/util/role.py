

def role(role_id):
    match role_id:
        case 1:
            return "ADMIN"
        case 2:
            return "LECTURER"
        case 3:
            return "STUDENT"