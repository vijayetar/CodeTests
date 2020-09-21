def integer_to_roman(num):
  values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
  roman_literals = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
  output_string = ""
  for val in values:
    while num >= val:
      num-=val
      output_string+=roman_literals[val]
  return output_string

if __name__ == "__main__":
    print(integer_to_roman(1194))