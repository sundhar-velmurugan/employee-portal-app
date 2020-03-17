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
Edit | Super Admin (if Primary user), Admin, Manager, Staff, Self | Manager, Staff, Self | Staff, Self | Self
Remove | Super Admin (if Primary user), Admin, Manager, Staff | Manager, Staff | - | -
Change User Scope | Super Admin (if Primary user), Admin, Manager, Staff | Manager, Staff | - | -

## Api:
### Public API:
Method | URL | Description
--- | --- | ---
POST | /api/login | User Login
GET | /api/users | Get public details of all users (limit upto 100)
GET | /api/user/:id | Get public user details (if not authenticated)

### Protected API:
Method | URL | Description
--- | --- | ---
POST | /api/add | Add user
GET | /api/user/:id | Get entire user details (if authorized)
DELETE | /api/user/:id | Remove user
PATCH | /api/user/:id | Edit user details, Change user scope
PATCH | /api/pwd/:id | Password change