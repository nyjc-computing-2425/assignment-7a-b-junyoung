# Defined dictionary
NUM_WORD = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

# Greedy algorithm implementation
def text_numeral(num):
  """
  Implements greedy algorithm to convert numbers to text

  Parameter
  ---------
  num: int
    the number to be converted to text

  Returns
  ---------
  text: str 
    text that is convereted from number

  Example:
  >>> text_numeral(15)
  'fifteen'
  >>> text_numeral(29)
  'twenty nine'
  """
  
  text = str()

  # Sorts the keys of the dictionary in descending order
  for n in sorted(NUM_WORD.keys(), reverse=True):
      count = num // n
      if count > 0:
          text += (NUM_WORD[n] + " ") * count
          num -= count * n

  return text.strip()