class Student:
	def __init__(self,name,age,gender):
		self.name=name
		self.age=age
		self.gender=gender
	def __str__(self):
		return"Hello,{}".format(self.name)
	def details(self):
		return "Name:{},Age:{},Gender:{}\
		".format(self.name,self.age,self.gender)
class Registration(Student):
			#method overloading
	def __init__(self,reg_no,name,age,gender,start_date):
			#A call to the superclasses method,in this case __init__
		Student.__init__(self,name,age,gender)
		self.__reg_no=reg_no
		self.__start_date=start_date
			#method overriding
	def details(self):
		return"Reg_no :{},Name:{},Age:{},\
		Gender:{}Start Date:{}".format(\
		self.__reg_no,self.name,self.age,\
		self.gender,self.__start_date)
	def designation(self):
		pass
		