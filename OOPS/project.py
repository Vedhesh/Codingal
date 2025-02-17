decimal = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
prompt = int(input('>'))
returned = ''
for i in range(len(decimal)):
    m=prompt//decimal[i]
    for j in range(m):
        returned += roman[i]
    prompt=prompt%decimal[i]
print(f">{returned}")