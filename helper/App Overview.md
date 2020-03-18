## **App idea:** Employee records portal
### 4 types of users:
1. Super Admin
2. Admin
3. Manager
4. Staff

### Permissions:
Operation/ User Role | Super Admin | Admin | Manager | Staff
--- | --- | --- | --- | ---
Add | Super Admin (if Primary user), Admin, Manager, Staff | Manager, Staff | - | -
Edit Details | Super Admin (if Primary user), Admin, Manager, Staff, Self | Manager, Staff, Self | Self | Self
Remove | Super Admin (if Primary user), Admin, Manager, Staff | Manager, Staff | - | -
Change User Scope | Super Admin (if Primary user), Admin, Manager, Staff | Manager, Staff | - | -
Change Password | Self | Self | Self | Self
View Basic Details | Everyone | Everyone | Everyone | Everyone
View Full Details | Self | Self | Self | Self

## Api:
### Public API:
Method | URL | Description
--- | --- | ---
POST | /api/login | User Login
GET | /api/users | Get public details of all users (limit upto 100)

### Protected API:
Method | URL | Description
--- | --- | ---
POST | /api/add | Add user
GET | /api/user/:id | Get user details (for other users)
GET | /api/user/:id | Get entire user details (for self)
DELETE | /api/user/:id | Remove user
PATCH | /api/user/:id | Edit user details, Change user scope
PATCH | /api/pwd/:id | Password change
