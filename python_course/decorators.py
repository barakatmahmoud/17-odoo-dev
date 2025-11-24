###
#
#
# Decorators
#
#
###

# def my_decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello")
#
# say_hello()


# is_logged_in = True
#
# def require_login(func):
#     def wrapper(*args, **kwargs):
#         if not is_logged_in:
#             print("Access denied")
#             return
#         return func(*args, **kwargs)
#     return wrapper
#
# @require_login
# def view_dashboard():
#     print("Dashboard content")
#
# view_dashboard()