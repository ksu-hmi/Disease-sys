print('Disease Checker\n')
def Diarrhea():
    print('1.Dysentery\n','2.Food allergy\n','3.Viral infection\n','4.Bacterial Infection\n','5.Parasite infection\n','6.Intestinal disease\n','7.No more symptoms\n')
    print('Enter any symptoms:')
    list_symptom = []
    while 1:
        a=int(input())
        if a==7:
            break
        list_symptom.append(a)
    temp = []

    for x in list_symptom:
        if x not in temp:
            temp.append(x)

    list_symptom = temp
    k = len(list_symptom)
    p = float((k/6)*100)

    return p

def Malaria():
    print('1.Chills\n','2.Headache\n','3.Vomiting\n','4.Dysentery\n','5.Join Pain\n','6.Rapid breathing\n','7.Rapid heart rate\n','8.Cough\n','9.No more symptoms\n')
    print('Enter any symptoms:')
    list_symptom = []
    while 1:
        a = int(input())
        if a == 9:
            break
        list_symptom.append(a)
    temp = []

    for x in list_symptom:
        if x not in temp:
            temp.append(x)

    list_symptom = temp
    k = len(list_symptom)
    p = float((k / 8) * 100)

    return p

def Covid_19():
    print('1.Feve\n','2.Dry cough\n','3.Sore throat\n','4.Dysentery\n','5.Headache\n','6.Loose of smell or taste\n','7.Rash on skin\n','8.Shortness of breathing\n','9.Chest Pain\n','10.No more symptoms\n')
    print('Enter any symptoms:')
    list_symptom = []
    while 1:
        a = int(input())
        if a == 10:
            break
        list_symptom.append(a)
    temp = []

    for x in list_symptom:
        if x not in temp:
            temp.append(x)

    list_symptom = temp
    k = len(list_symptom)
    p = float((k / 9) * 100)

    return p

def Dengue():
    print('1.Baily pain\n','2.Vomiting\n','3.Bleeding from nose\n','4.Vomiting blood\n','5.Tired\n','6.No more symptoms\n')
    print('Enter any symptoms:')
    list_symptom = []
    while 1:
        a = int(input())
        if a == 6:
            break
        list_symptom.append(a)
    temp = []

    for x in list_symptom:
        if x not in temp:
            temp.append(x)

    list_symptom = temp
    k = len(list_symptom)
    p = float((k / 5) * 100)

    return p

def Chikungunia():
    print('1. Fever\n','2.Joint Pain\n','3.Headache\n','4.Muscle Pain\n','5.No more symptoms\n')
    print('Enter any symptoms:')
    list_symptom = []
    while 1:
        a = int(input())
        if a == 5:
            break
        list_symptom.append(a)
    temp = []

    for x in list_symptom:
        if x not in temp:
            temp.append(x)

    list_symptom = temp
    k = len(list_symptom)
    p = float((k / 4) * 100)

    return p

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Enter Patient Name: ")
    name = input()
    print("Enter Patient Age: ")
    age = input()
    print('1.Diarrhea\n', '2.Malaria\n', '3.Covid-19\n', '4.Dengue\n', '5.Chikungunia\n')
    print('Enter a disease number:')
    a = int(input())
    if a == 1:
        disease = "Diarrhea"
        print(disease)
        k = Diarrhea()
    if a == 2:
        disease = "Malaria"
        print(disease)
        k = Malaria()
    if a == 3:
        disease = "Covid-19"
        print(disease)
        k = Covid_19()
    if a == 4:
        disease = "Dengue"
        print(disease)
        k = Dengue()
    if a == 5:
        disease = "Chikungunia"
        print(disease)
        k = Chikungunia()

    print("Test Result")
    print("Patient name: ", name)
    print("Patient age: ", age)
    print("Disease name", disease)
    if k >= 60:
        print("Status: Positive")
    else:
        print("Status: Negative")

