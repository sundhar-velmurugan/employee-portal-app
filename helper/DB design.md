### Employee Details
Column | Data Type | Constraints 
--- | --- | ---
Id | INT UNSIGNED | AUTO_INCREMENT, PRIMARY KEY
First Name | VARCHAR(20) | 
Last Name | VARCHAR(20) | NOT NULL
Title | VARCHAR(30) | NOT NULL
Phone number | VARCHAR(15) |
Date of Birth | DATE | NOT NULL
Email | VARCHAR(255) | NOT NULL
Creation Time | DATETIME | DEFAULT CURRENT_TIMESTAMP
Modification Time | DATETIME | ON UPDATE CURRENT_TIMESTAMP

### Staff Info
Column | Data Type | Constraints 
--- | --- | ---
Id | INT UNSIGNED | FOREIGN KEY – Employee Details(Id), NOT NULL, UNIQUE
Added By | INT UNSIGNED | FOREIGN KEY – Admin Table(Id), NOT NULL
Reporting To | INT UNSIGNED | FOREIGN KEY – Manager Table(Id)

### Manager Info
Column | Data Type | Constraints 
--- | --- | ---
Id | INT UNSIGNED | FOREIGN KEY – Employee Details(Id), NOT NULL, UNIQUE
Added By | INT UNSIGNED | FOREIGN KEY – Admin Table(Id), NOT NULL
Reporting To | INT UNSIGNED | FOREIGN KEY – Admin Table(Id)

### Admin Info
Column | Data Type | Constraints 
--- | --- | ---
Id | INT UNSIGNED | FOREIGN KEY – Employee Details(Id), NOT NULL, UNIQUE
Super User | BOOL | DEFAULT false
Primary User | BOOL | DEFAULT false

### Employee Login
Column | Data Type | Constraints 
--- | --- | ---
Id | INT UNSIGNED | FOREIGN KEY – Employee Details(Id), UNIQUE
Username | VARCHAR(20) | PRIMARY KEY
Password | BINARY(60) | NOT NULL

Reason for choosing BINARY(60) as data type for password:
- **For (60):** Using 2a format in bcrypt needs 60 bytes
- **For BINARY:** CHAR is not binary safe. At worst case ‘a’ is treated as ‘A’ during equality operation
