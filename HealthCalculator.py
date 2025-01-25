#Kanav Azad
#11/29/2022
#Purpose: use while loops and functions to give the user their BMI and Karvonen Formula values based on input

def bodyMassIndex(height, weight):
  weight = weight * 0.454
  height = height * 0.0254
  height = pow(height, 2)
  bmi = weight/height
  return bmi


def karvonenFormula(age, heartRate, intensity):
  maxHeartRate = (((220 - age) - heartRate) * intensity) + heartRate
  maxHeartRate = round(maxHeartRate)
  return maxHeartRate


def main():

  print("Please enter the following information ...")
  weight = int(input("Enter weight (lbs): "))
  height = int(input("Enter height (in): "))
  age = int(input("Enter your current age: "))
  heartRate = int(input("Enter your resting heart rate: "))

  bmi = bodyMassIndex(height, weight)
 

  if (bmi < 18.5):
    health = "Underweight"
  elif (bmi >+ 18.5 and bmi < 25):
    health = "Normal Weight"
  elif (bmi >= 25 and bmi < 30):
    health = "Overweight"
  else:
    health = "Obese"

  print("\n\nResults ...")  
  
  print("\nBMI: {:.3f}" .format(bmi) + " -- " + health)

  print("\nExercise Intensity Heart Rates: ")
  print("Intensity \t\t Max Heart Rate")
  
  intensity = 0.5
  while intensity < 1:
    maxHeartRate = karvonenFormula(age, heartRate, intensity)
    print("{:.2f}" .format(intensity) + " \t\t\t " + str(maxHeartRate))
    
    intensity += 0.05


main()