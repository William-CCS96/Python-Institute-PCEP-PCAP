from turtle import pos


position=[1,"X","X","X","X","X","X","X","X","X"]
def empate_fun():
    for i in position[1:10]:
        if i=="X" or i=="O":
            empate="Si"
            continue
        else: 
            empate="No"
            break
    return empate

print(empate_fun())