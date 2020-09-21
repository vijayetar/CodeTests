def roman_to_int(input_string):
  set_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
  sum = 0
  counter = 0
  next_num = 0
  current = 0
  for char in input_string:
    current = set_dict[char]
    if counter+1<len(input_string):
      next_num=set_dict[input_string[counter+1]]
      if next_num>set_dict[char]:
        current *= -1
    sum+= current
    counter += 1
  return sum


if __name__ == "__main__":
    print(roman_to_int('MCMXCIV'))