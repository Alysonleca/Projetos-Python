teste = "amz"
if teste == "java":
    print('ok then')
elif teste == "bingo":
    print('thats that')
else:
    print("biruleibe")


teste2 = [1,1,3,4]

for numbs in teste2:
    #check for even
    if numbs % 2 ==0:
        print(numbs)

teste3 = [1,1,1,1,1]

contagem = 0

for nums in teste3:
    contagem = contagem + nums
    print(contagem)
