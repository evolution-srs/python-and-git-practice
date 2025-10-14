//...Initialize the employees array object. Initialize it with key value pairs
const employees = [
      { id: 1, name: 'John Doe', age: 30, department: 'IT', salary: 50000 },
      { id: 2, name: 'Alice Smith', age: 28, department: 'HR', salary: 45000 },
      { id: 3, name: 'Bob Johnson', age: 35, department: 'Finance', salary: 60000 },
      //... More employee records can be added here
    ];

//... Create the displayEmployees() function to display employees details
// Function to display all employees
function displayEmployees() {
    const totalEmployees = employees
        .map(employee => `<p>${employee.id}: ${employee.name} - ${employee.department} - $${employee.salary}</p>`)
        .join('');
    document.getElementById('employeesDetails').innerHTML = totalEmployees;
}

//... Create the calculateTotalSalaries() function to calculate employees' total salaries. 
function calculateTotalSalaries() {
      const totalSalaries = employees.reduce((acc, employee) => acc + employee.salary, 0);
      alert(`Total Salaries: $${totalSalaries}`);
    }

//...Create displayHREmployees() function to display employees details based on department such as the
//  HR department.
function displayHREmployees() {
     const hrEmployees = employees.filter(employee => employee.department === 'HR');
      const hrEmployeesDisplay = hrEmployees.map((employee, index) => `<p>${employee.id}: ${employee.name}: ${employee.name} - ${employee.department} - $${employee.salary}</p>`).join('');
      document.getElementById('employeesDetails').innerHTML = hrEmployeesDisplay;
}
//... Create findEmployeeById() function to display employees' details based on ID
function findEmployeeById(employeeId) {
      const foundEmployee = employees.find(employee => employee.id === employeeId);
      if (foundEmployee) {
      document.getElementById('employeesDetails').innerHTML =`<p>${foundEmployee.id}: ${foundEmployee.name}: ${foundEmployee.name} - ${foundEmployee.department} - $${foundEmployee.salary}</p>`;
      }
      else{
        document.getElementById('employeesDetails').innerHTML = 'no employee has been found with this ID';
       }
   }

//... Add one more key Specialization to the Array object
const employees = [
  { id: 1, name: 'John Doe', age: 30, department: 'IT', salary: 50000 },
  { id: 2, name: 'Alice Smith', age: 28, department: 'HR', salary: 45000 },
  { id: 3, name: 'Bob Johnson', age: 35, department: 'Finance', salary: 60000 },
];

// 1. Define the specializations array
const specializations = ['JavaScript', 'Python', 'Java'];

// 2. Use map() to create a new array with the added key
const employeesWithSpecialization = employees.map((employee) => {
  // Use the spread operator (...) to copy all existing properties
  // Then, add the new 'Specialization' property
  return {
    ...employee,
    Specialization: specializations
  };
});

console.log(employeesWithSpecialization);


//... create a function to display the details of employees who have specialization 
// 1. Function to handle the button click
function searchBySpecialization(targetSpecialization) {
    // Use the filter() method to create a new array 
    // containing only the employees that match the criteria.
    const specializedEmployees = employees.filter(employee => {
        // The criterion: check if the employee's Specialization array 
        // includes the target specialization.
        // The includes() method is essential here.
        return employee.Specialization.includes(targetSpecialization);
    });

    // 2. Display the results
    console.log(`Employees specialized in ${targetSpecialization}:`);
    
    if (specializedEmployees.length > 0) {
        specializedEmployees.forEach(employee => {
            console.log(`- ID: ${employee.id}, Name: ${employee.name}, Department: ${employee.department}`);
        });
    } else {
        console.log("No employees found with that specialization.");
    }
}
