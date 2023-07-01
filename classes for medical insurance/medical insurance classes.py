class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker
    
    
    def estimated_insurance_cost(self):
        estimated_cost = 250*self.age - 128*self.sex + 370*self.bmi +425*self.num_of_children+ 24000*self.smoker -12500
        print( self.name + "'s estimated insurance cost is "+ str(estimated_cost) +" dollars")
    
    
    def age_update(self,new_age):
        self.age = new_age
        print(self.name + " is now " + str(new_age) + " years old.")
        self.estimated_insurance_cost()
    
    
    def num_of_children_update(self,new_num_children):
        self.num_of_children=new_num_children
        if new_num_children==1:
            print(self.name + " has " + str(new_num_children) + " child.")
        elif new_num_children>1:
            print(self.name + " has " + str(new_num_children) + " children.")
        self.estimated_insurance_cost()



    def patient_profile(self):
        
        patients_profile = {}
        
        patients_profile["Name"] = self.name
        patients_profile["Age"] = self.age
        patients_profile["Gender"] = self.sex
        patients_profile["Number of Children"] = self.num_of_children
        patients_profile["Smoker status"] = self.smoker
        patients_profile["Bmi"] = self.bmi
        
        return patients_profile
        #self.patients_dictionary["insurance cost"] = self.patient_insurance_cost




patient1 = Patient('John Doe', 25, 1, 22.2, 0, 0)
print(patient1.name)
patient1.estimated_insurance_cost()
patient1.age_update(26)
patient1.num_of_children_update(1)
print(patient1.patient_profile())
