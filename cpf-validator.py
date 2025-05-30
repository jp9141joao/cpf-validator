# Function to validate CPF number
def Validator(CPF):
    # Convert the input CPF to a string to access each digit
    StringCPF = str(CPF)

    # CPF must be exactly 11 digits
    if len(StringCPF) != 11:
        print('Invalid CPF!')
        return

    # Extract the two verification digits from the CPF
    ValidatorX = int(StringCPF[9])
    ValidatorY = int(StringCPF[10])

    # First sum for calculating the first verification digit
    Sum1 = 0
    Counter = 0

    # Loop to multiply each of the first 9 digits by weights from 10 to 2
    for i in range(10, 1, -1):
        NumbCPF = int(StringCPF[Counter])
        Sum1 += NumbCPF * i
        Counter += 1

    # Calculate the first verification digit
    CheckDigitX = 11 - (Sum1 % 11)

    # Reset sum and counter for the second verification digit
    Sum2 = 0
    Counter = 0

    # Loop to multiply each of the first 10 digits by weights from 11 to 2
    for i in range(11, 1, -1):
        NumbCPF = int(StringCPF[Counter])
        Sum2 += NumbCPF * i
        Counter += 1

    # Calculate the second verification digit
    CheckDigitY = 11 - (Sum2 % 11)

    # Check if both calculated verification digits match the provided ones
    if CheckDigitX == ValidatorX and CheckDigitY == ValidatorY:
        print('Valid CPF!')
    else:
        print('Invalid CPF!')

# Prompt user for CPF input
CPF = int(input('Enter your CPF: '))

# Call the validator function
Validator(CPF)
