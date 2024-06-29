TEST = ['Bot testing',"k☆'s server"]
TEST_TEST = [['Bot testing','test','test'],["tk☆'s server",'test', 'test']]
import os

try:
  index = TEST.index("k☆'s server")
  print(index)
  TEST.pop(index)
except ValueError:
  print("Test")
  pass

try:
  index = TEST.index("k☆'s server")
  print(index)
  TEST.pop(index)
except ValueError:
  print("Test")
  pass

try:
  for roles in TEST_TEST:
    if roles[0] == "k☆'s server":
      TEST_TEST.remove(roles)
  print(TEST_TEST)
except ValueError:
  print("Test")
  pass

os.remove(f'test_reaction_roles.txt')

