def par(broj):
    for i in range(broj + 1):
        if i % 2 == 0:
            yield f"parni broj je: {i}"
        else:
            yield f"neparni broj je: {i}"

for number in par(30):
    print(number)
    
