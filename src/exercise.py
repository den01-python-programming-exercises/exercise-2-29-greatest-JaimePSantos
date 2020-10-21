def greatest(number1, number2, number3):
    # write your code here
    if(number1>number2):
      if(number1>number3):
        return number1
      else:
        return number3
    elif(number2 > number1):
      if(number2>number3):
        return number2
      else:
        return number3
        
def main():
    answer = greatest(2, 7, 9)
    print("Greatest: " + str(answer))

if __name__ == '__main__':
    main()
