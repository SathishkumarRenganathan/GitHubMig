# Custom exception
class InvalidAgeError(Exception):
  def __init__(self, arg):
    self.msg = arg

def vote_eligibility(age):
  if age < 18:
    raise InvalidAgeError("Person not eligible to vote, age is " + str(age))
  else:
    print('Person can vote, age is', age)

# calling function
try:
  vote_eligibility(22)
  vote_eligibility(14)
except InvalidAgeError as error:
    print(error)