# Problem: https://www.hackerrank.com/challenges/python-mutations/problem
# Score: 10

def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    return "".join(string_list)

