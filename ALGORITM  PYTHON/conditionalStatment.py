age = 70
is_member = True # Saya asumsikan ini maksudnya is_member (bukan is_number)

if age >= 60:
    if is_member:
        print("30% Senior discount")
    else:
        print("20% senior discount")
else:
    print("Not eligible for a senior")


number=2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case 4:
        print("Other number")


  
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


    def sapa_teman(nama):
  print("Hai",nama);
 
sapa_teman("Lisa")
sapa_teman("Sari")
sapa_teman("Putri")