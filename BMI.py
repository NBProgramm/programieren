grösse=(input("Deine Grösse ist(m):")) # Der Computer fragt sie  wie gross sie sind
gewicht=(input("Dein Gewicht ist:(kg gerundet)")) # Der Computer fragt sie wie  Schwer sie sind



grösse2=float(grösse)*float(grösse) # Das Programm rechnet die grösse^2
bmi=int(gewicht)/float(grösse2) # Der Computer rechnet das gewicht mal die grösse^2. Das ist die vormel für das berechnen des BMI
print("Dein BMI ist:  " +str(bmi)) # Ausgabe 
