grösse=(input("Deine Grösse ist(m):"))
gewicht=(input("Dein Gewicht ist:(kg gerundet)"))



grösse2=float(grösse)*float(grösse)

bmi=int(gewicht)/float(grösse2)
print("Dein BMI ist:  " +str(bmi))