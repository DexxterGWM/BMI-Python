## https://www.wikihow.com/Calculate-Your-Body-Mass-Index-(BMI)
## https://github.com/hevalhazalkurt/codewars_python_solutions/blob/master/8kyuKatas/Calculate_BMI.md

'''
    < 18.5 - Underweight
    < 25.0 - Normal (between 18.5 and 24.9)
    < 30.0 - Overweight (between 25 and 29.9)
    > 29.9 - Obese
'''

def BMI(self):
    # bmi = self.weight / self.height ** 2
    bmi = self.weight / (pow(self.height, 2))

    return f'''{bmi:.2f}: {
        ['Underweight', 'Normal', 'Overweight', 'Obese'][(bmi > 29.9) + (bmi > 24.9) + (bmi > 18.4)]
    }'''

def Entry(self):
    try:
        system('cls' if name == 'nt' else 'clear')

        self.weight = float(input('\n Weight = '))
        self.height = input(' Height = ')

        try:
            self.height = int(self.height) / 100
        except ValueError:
            self.height = float(self.height)

        return True

    except Exception as err:
        input(f'\n [-] {type(err).__name__}: {err}.')

from os import system, name

obj = type('Obj', (object, ), {'BMI': BMI, 'Entry': Entry})
start = obj()

try:
    while not start.Entry():
        if start.Entry(): break

    print(f'''\n {
        start.BMI()
    }''')

except KeyboardInterrupt: print()