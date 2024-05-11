def getFirstAndLastName(fullName):
    ho_ten = fullName.split()
    ho = " ".join(ho_ten[:-1])
    ten = ho_ten[-1]
    return ho, ten