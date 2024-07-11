class Employee:

	no_of_employees = 0

	def __init__(self, employeeId, employeeName, employeeAge, employeeBod, employeePosition):
		self.employeeId = employeeId
		self.employeeName = employeeName
		self.employeeAge = employeeAge
		self.employeeBod = employeeBod
		self.employeePosition = employeePosition



	def __str__(self,employeeId):
		return f"{self.employeeName} is a {employeePosition} "






class Order:


	def __init__(self, orderID, orderItems):
		self.orderID = orderID
		self.orderItems = orderItems




class Customer:


	def __init__(self, customerId, customerName):
		self.customerId = customerId
		self.customerName = customerName




customer1 = Customer(11212121, "John Wick")
employee1 = Employee(2021134,"Larry Wock",24,"2000/02/2", "Assistant Manager")
employee1 = Employee(2021134,"Jerry Orman",27,"1997/02/2", "Cashier")


print(customer1.customerId)
print(customer1.customerName)

print(employee1.employeeId)
print(employee1.employeeName)