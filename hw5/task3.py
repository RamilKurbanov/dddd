names = ["Alice", "Bob", "Charlie"]
bet = [1000, 1500, 800]
bonus = ["10.25%", "12.5%", "8.75%"]

result = {name: bet_amount * float(bonus_percentage.strip('%')) / 100 for name, bet_amount, bonus_percentage in zip(names, bet, bonus)}

print(result)