print('#Python progrm to find Greatest value#')
print('======================================')

n=int(input("Number of list elemet :"))
print()

x=[]
for i in range(n):
 print('Angka ke -',i+1,':',end='')
 x.append(int(input()))

 print()

max_num=x[0]
for i in range(1,n):
 if(x[i] > max_num):
  max_num=x[i]


print('Angka terbesar adalah ',max_num)
