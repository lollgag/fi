#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

// Structure to represent employee information
struct Employee {
    int employeeID;
    string name;
    string designation;
    double salary;
};

// Function to add employee information to the data file
void addEmployee(const Employee& emp) {
    ofstream dataFile("employeeData.txt", ios::app);
    if (!dataFile.is_open()) {
        cerr << "Unable to open data file." << endl;
        return;
    }

    // Append employee record to data file
    dataFile << emp.employeeID << " " << emp.name << " " << emp.designation << " " << emp.salary << endl;

    // Close data file
    dataFile.close();

    cout << "Employee information added successfully." << endl;
}

// Function to delete employee information from the data file
void deleteEmployee(int employeeID) {
    ifstream dataFile("employeeData.txt");
    ofstream tempFile("temp.txt");
    if (!dataFile.is_open() || !tempFile.is_open()) {
        cerr << "Unable to open data file." << endl;
        return;
    }

    Employee emp;
    bool found = false;
    while (dataFile >> emp.employeeID >> emp.name >> emp.designation >> emp.salary) {
        if (emp.employeeID != employeeID) {
            tempFile << emp.employeeID << " " << emp.name << " " << emp.designation << " " << emp.salary << endl;
        } else {
            found = true;
        }
    }

    dataFile.close();
    tempFile.close();

    if (found) {
        remove("employeeData.txt");
        rename("temp.txt", "employeeData.txt");
        cout << "Employee with ID " << employeeID << " deleted successfully." << endl;
    } else {
        cout << "Employee with ID " << employeeID << " not found." << endl;
    }
}

// Function to display information of a particular employee
void displayEmployee(int employeeID) {
    ifstream dataFile("employeeData.txt");
    if (!dataFile.is_open()) {
        cerr << "Unable to open data file." << endl;
        return;
    }

    Employee emp;
    bool found = false;
    while (dataFile >> emp.employeeID >> emp.name >> emp.designation >> emp.salary) {
        if (emp.employeeID == employeeID) {
            cout << "Employee ID: " << emp.employeeID << endl;
            cout << "Name: " << emp.name << endl;
            cout << "Designation: " << emp.designation << endl;
            cout << "Salary: $" << fixed << setprecision(2) << emp.salary << endl;
            found = true;
            break;
        }
    }

    dataFile.close();

    if (!found) {
        cout << "Employee with ID " << employeeID << " not found." << endl;
    }
}

int main() {
    int choice, employeeID;
    Employee emp;

    while (true) {
        cout << "1. Add employee\n2. Delete employee\n3. Display employee\n4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter Employee ID: ";
                cin >> emp.employeeID;
                cout << "Enter Name: ";
                cin.ignore(); // Ignore newline character left in the buffer
                getline(cin, emp.name);
                cout << "Enter Designation: ";
                getline(cin, emp.designation);
                cout << "Enter Salary: ";
                cin >> emp.salary;
                addEmployee(emp);
                break;
            case 2:
                cout << "Enter Employee ID to delete: ";
                cin >> employeeID;
                deleteEmployee(employeeID);
                break;
            case 3:
                cout << "Enter Employee ID to display: ";
                cin >> employeeID;
                displayEmployee(employeeID);
                break;
            case 4:
                cout << "Exiting program." << endl;
                exit(0);
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
