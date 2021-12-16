grösse=(input("Deine Grösse ist(m):")) #Gib ein wie gross du bist
gewicht=(input("Dein Gewicht ist:(kg gerundet)")) # Gibi ein wie schwer du bist



grösse2=float(grösse)*float(grösse) #rechnet grösse mal grösse

bmi=int(gewicht)/float(grösse2) # Es rechnet das gewicht mal die grösse^2
print("Dein BMI ist:  " +str(bmi)) # Ausgabe 
