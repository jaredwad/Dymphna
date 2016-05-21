from Data.DataAccess.TwitterDataAccessObject import TwitterDataAccessObject

dao = TwitterDataAccessObject()

userIDs = [
    1259825000
    , 11348282
    , 27851454
    , 302666251
]

for id in userIDs:
    dao.get_user_statuses(id, True)

