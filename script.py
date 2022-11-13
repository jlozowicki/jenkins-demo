import os

branch = os.environ['GIT_BRANCH']

for i in range(10):
  print("Testing script run on the",branch,"branch!")