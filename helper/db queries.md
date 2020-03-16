### Create database:
```
CREATE DATABASE flask;
```
### Create Employee Details Table:
```
CREATE TABLE EmployeeDetails (id INT UNSIGNED AUTO_INCREMENT, first_name VARCHAR(20), last_name VARCHAR(20) NOT NULL, title VARCHAR(30) NOT NULL, phone_number VARCHAR(15), date_of_birth DATE NOT NULL, email VARCHAR(255) UNIQUE NOT NULL, creation_time DATETIME DEFAULT CURRENT_TIMESTAMP, modification_time DATETIME ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY (id));
```
### Create Employee Login Table:
```
CREATE TABLE EmployeeLogin (id INT UNSIGNED UNIQUE NOT NULL, username VARCHAR(20), password BINARY(60) NOT NULL, PRIMARY KEY (username), user_type VARCHAR(10) NOT NULL, FOREIGN KEY (id) REFERENCES EmployeeDetails (id), CHECK(user_type in ('admin', 'manager', 'staff')));
```
### Create Admin Info Table:
```
CREATE TABLE AdminInfo (id INT UNSIGNED UNIQUE NOT NULL, is_super BOOL DEFAULT false, is_primary BOOL DEFAULT false, FOREIGN KEY (id) REFERENCES EmployeeDetails (id));
```
### Create Manager Info Table:
```
CREATE TABLE ManagerInfo (id INT UNSIGNED UNIQUE NOT NULL, added_by INT UNSIGNED NOT NULL, reporting_to INT UNSIGNED, FOREIGN KEY (id) REFERENCES EmployeeDetails (id), FOREIGN KEY(added_by) REFERENCES AdminInfo (id), FOREIGN KEY (reporting_to) REFERENCES AdminInfo (id));
```
### Create Staff Info Table:
```
CREATE TABLE StaffInfo (id INT UNSIGNED UNIQUE NOT NULL, added_by INT UNSIGNED NOT NULL, reporting_to INT UNSIGNED, FOREIGN KEY (id) REFERENCES EmployeeDetails (id), FOREIGN KEY(added_by) REFERENCES AdminInfo (id), FOREIGN KEY (reporting_to) REFERENCES ManagerInfo (id));
```

### Drop all tables:
```
DROP TABLE StaffInfo;
DROP TABLE ManagerInfo;
DROP TABLE AdminInfo;
DROP TABLE EmployeeLogin;
DROP TABLE EmployeeDetails;
```