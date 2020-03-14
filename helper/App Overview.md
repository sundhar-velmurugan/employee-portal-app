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

### Protected API:
Method | URL | Description
--- | --- | ---
POST | /api/add | Add user
DELETE | /api/:id | Remove user
PATCH | /api/:id | Edit user details, Change user scope
