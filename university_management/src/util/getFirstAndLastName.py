def getFirstAndLastName(fullName):
    """
    seperate first name and last name
    args:
        fullName(str)
    return
        ho(str)
        ten(str)
    """
    ho_ten = fullName.split()
    ho = " ".join(ho_ten[:-1])
    ten = ho_ten[-1]
    return ho, ten