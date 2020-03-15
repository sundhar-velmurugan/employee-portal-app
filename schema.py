from marshmallow import Schema, fields, validate

class AddUser(Schema):
  user_type = fields.String(validate=validate.OneOf(["admin", "manager", "staff"]))
  first_name = fields.String(validate=validate.Length(max=20))
  last_name = fields.String(required = True, validate=validate.Length(max=20))
  Title = fields.String(required = True, validate=validate.Length(max=30))
  phone_number = fields.String(validate=validate.Length(max=15))
  date_of_birth = fields.Date(required = True) # ISO Format: YYYY-MM-DD
  email = fields.Email(required = True)
  username = fields.String(required = True, validate=validate.Length(max=20))
