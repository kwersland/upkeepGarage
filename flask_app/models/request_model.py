# from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app import DATABASE
# from flask import flash #part of data validation
# import re #regex access

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


# class Request:
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.email = data['email']
#         self.phone = data['phone']
#         self.message = data['message']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']


# # create
#     @classmethod
#     def create(cls, data):
#         query = "INSERT INTO requests (first_name, last_name, email, phone, message) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(phone)s, %(message)s);"
#         results = connectToMySQL(DATABASE).query_db(query, data)
#         return results

# # get all requests
#     @classmethod
#     def get_requests(cls):
#         query = "SELECT * FROM requests;"
#         return connectToMySQL(DATABASE).query_db(query)


# # Get one by id
#     @classmethod
#     def get_one(cls, data):
#         query = "SELECT * FROM requests WHERE id = %(id)s;"
#         results = connectToMySQL(DATABASE).query_db(query, data)
#         if not results:
#             return False
#         return cls(results[0])


# # validations
#     @staticmethod
#     def validate(request_data):
#         is_valid = True
#         if len(request_data['first_name']) < 2:
#             flash("First name is required", "first_name")
#             is_valid = False
#         if len(request_data['last_name']) < 2:
#             flash("Last name is required", "last_name")
#             is_valid = False
#         if len(request_data['email']) < 1:
#             flash("Please provide email", "email")
#             is_valid = False
#         if len(request_data['phone']) < 1:
#             flash("Please provide phone number", "phone")
#             is_valid = False
#         if len(request_data['message']) < 5:
#             flash("Please tell us what you're interested in", "message")
#         elif not EMAIL_REGEX.match(request_data['email']):
#             flash("Invalid email", "reg")
#             is_valid = False
#         return is_valid