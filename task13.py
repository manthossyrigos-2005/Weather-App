user_input = int(input("Enter a positive integer: "))
if user_input < 0:
    print("Illegal input")
    exit()
apotelesmata = []
for i in range(1,11):
    results = user_input * i
    print(f"{results} = {user_input} * {i}")
    apotelesmata.append(results)

    megisto = max(apotelesmata)
    print(f"The maximum number is :{megisto}")


