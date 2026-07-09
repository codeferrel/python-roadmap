def hitung_luas_segitiga(alas,tinggi):
    luas=(alas*tinggi)/2
    return luas

var1 = hitung_luas_segitiga(5,7)
print("Luas Segetiga adalah :",var1)


def tambah(var2 =5, var3 =2):
    return var2+var3

print(tambah())
print(tambah(1))
print(tambah(1,2))
print(tambah(5,6))



def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil
 
print( pangkat(3) )     
print( pangkat(5) )     
print( pangkat(10) )     
print( pangkat(3,3) )   
print( pangkat(5,4) )    
print( pangkat(6,6) )    

#Finding the maximum value
def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1)) 