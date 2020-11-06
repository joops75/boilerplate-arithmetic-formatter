import re

def arithmetic_arranger(problems, calc = False):
  if len(problems) > 5:
    return "Error: Too many problems."

  # set up answer row arrays
  arranged_problems = [[],[],[],[]]

  for problem in problems:
    good_match = re.match("^\s*(\d{1,4})\s+([+-])\s+(\d{1,4})\s*$", problem)

    bad_match = re.match("^\s*(\S+)\s+(\S+)\s+(\S+)\s*$", problem)

    if good_match:
      num1 = good_match[1]
      op = good_match[2]
      num2 = good_match[3]
      
      # find max row length
      max_row_length = max(len(num1) + 2, len(num2) + 2)

      # format each row
      row1 = num1.rjust(max_row_length)

      row2 = op + ' ' + num2.rjust(max_row_length - 2)

      row3 = '-' * max_row_length

      tot = eval(num1 + op + num2)
      row4 = str(tot).rjust(max_row_length)

      # push rows onto answer row arrays
      arranged_problems[0].append(row1)
      arranged_problems[1].append(row2)
      arranged_problems[2].append(row3)
      arranged_problems[3].append(row4)
  
    elif bad_match:
      if re.search("[^+-]", bad_match[2]):
        return "Error: Operator must be '+' or '-'."

      elif re.search("\D", bad_match[1]) or re.search("\D", bad_match[3]):
        return "Error: Numbers must only contain digits."

      elif re.search("\d{5,}", bad_match[1]) or re.search("\d{5,}", bad_match[3]):
        return "Error: Numbers cannot be more than four digits."

      else:
        return "Error: Incorrect format."

    else:
      return "Error: Incorrect format."

  # remove answer row if not required
  if (not(calc)):
    arranged_problems.pop()
  
  # convert answer row arrays to strings with spacing
  for i in range(0, len(arranged_problems)):
    arranged_problems[i] = '    '.join(arranged_problems[i])

  # return joined answer array
  return '\n'.join(arranged_problems)