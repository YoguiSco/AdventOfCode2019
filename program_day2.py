list_input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0]

test_list_input = [1,12,2,3,1,1,2,3,99,1,3,4,3,1,5,0,3,2,10,1,2,99]


def findOpCode(m_list, m_index):
  print(str(m_list))
  for i in range(len(m_list)):
    if ( m_list[i] == 1 ):
      return "in_progress", m_list[i], m_list[i+1], m_list[i+2], m_list[i+3]
    elif ( m_list[i] == 2 ):
      return "in_progress", m_list[i], m_list[i+1], m_list[i+2], m_list[i+3]
    elif ( m_list[i] == 99):
      return "halt", i, 0,0,0

def addition(m_list_add, m_value_index_1, m_value_index_2, m_result_index):
  print("addition")
  m_list_add[m_result_index] = m_list_add[m_value_index_1] + m_list_add[m_value_index_2]

def multiplication(m_list_add, m_value_index_1, m_value_index_2, m_result_index):
  print("multiplication")
  m_list_add[m_result_index] = m_list_add[m_value_index_1] * m_list_add[m_value_index_2]

list_output = list_input.copy()
state = "in_progress"
new_index_start = 0

while(state != "halt"):
  state, optcode, value_index_1, value_index_2, result_index = findOpCode(list_output[new_index_start:], new_index_start)
  if optcode == 1:
    addition(list_output,value_index_1,value_index_2,result_index)
    new_index_start = new_index_start + 4
  elif optcode == 2:
    multiplication(list_output,value_index_1,value_index_2,result_index)
    new_index_start = new_index_start + 4
  elif optcode == 99:
    print("END OF PROG")
    break

print("list input:" + str(list_input))
print("list output:" + str(list_output))


#################################PART TWO

list_input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0]


def findOpCode(m_list, m_index):
  for i in range(len(m_list)):
    if ( m_list[i] == 1 ):
      return "in_progress", m_list[i], m_list[i+1], m_list[i+2], m_list[i+3]
    elif ( m_list[i] == 2 ):
      return "in_progress", m_list[i], m_list[i+1], m_list[i+2], m_list[i+3]
    elif ( m_list[i] == 99):
      return "halt", i, 0,0,0

def addition(m_list_add, m_value_index_1, m_value_index_2, m_result_index):
  m_list_add[m_result_index] = m_list_add[m_value_index_1] + m_list_add[m_value_index_2]

def multiplication(m_list_add, m_value_index_1, m_value_index_2, m_result_index):
  m_list_add[m_result_index] = m_list_add[m_value_index_1] * m_list_add[m_value_index_2]




noun = 0
verb = 0
while( noun < 100 ):
  while (verb < 100 ):
    list_output = list_input.copy()
    state = "in_progress"
    new_index_start = 0
    list_output[1] = noun
    list_output[2] = verb
    while(state != "halt"):
      state, optcode, value_index_1, value_index_2, result_index = findOpCode(list_output[new_index_start:], new_index_start)
      if optcode == 1:
        addition(list_output,value_index_1,value_index_2,result_index)
        new_index_start = new_index_start + 4
      elif optcode == 2:
        multiplication(list_output,value_index_1,value_index_2,result_index)
        new_index_start = new_index_start + 4
      elif optcode == 99:
        print("END OF PROG")
        break
    print(list_output[0])
    if list_output[0] == 19690720:
      print("yes noun is " + str(noun) + " and verb is " + str(verb))
      noun = 100
      verb = 100
      break
    else:
      verb = verb + 1
  noun = noun + 1
  verb = 0
