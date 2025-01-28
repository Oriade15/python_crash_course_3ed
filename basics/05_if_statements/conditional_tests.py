print("Conditional Tests")

weather = 'sunny'
print("\nWeather")
print(f"• Is today's weather rainy? \n\tAnswer: {weather == 'rainy'}")
print(f"• Is today's weather sunny? \n\tAnswer: {weather == 'sunny'}")

username = 'Windows'
print("\nUsername")
print(f"• Does the username 'windows' exist? \n\tAnswer: {username.lower() == 'windows'}")
print(f"• Does the username 'mac' exist? \n\tAnswer: {username.lower() == 'mac'}")

lucky_number = 34
print("\nLucky number")
print(f"• Is my lucky number greater than 10? \n\tAnswer: {lucky_number > 10}")
print(f"• Is my lucky number less than 30? \n\tAnswer: {lucky_number < 30}")
print(f"• Is my lucky number greater than or equal to 32? \n\tAnswer: {lucky_number >= 32}")
print(f"• Is my lucky number less than or equal to 35? \n\tAnswer: {lucky_number <= 35}")
print(f"• Is my lucky number not equal to 33? \n\tAnswer: {lucky_number != 33}")
print(f"• Is my lucky number equal to 34? \n\tAnswer: {lucky_number == 34}")

cgpa = 4.99
print("\nWhat did you graduate with?")
print(f"• Second class upper? \n\tAnswer: {cgpa >= 3.5 and cgpa < 4.5}")
print(f"• First class? \n\tAnswer: {cgpa >= 4.5}")

code_editor = 'vscode'
code_editor_name="VS Code"
print(f"• Is my code editor VS Code? \n\tAnswer: {code_editor == 'vscode' or code_editor_name == 'VS Code'}")
print(f"• Is my code editor Rider? \n\tAnswer: {code_editor == 'rider' or code_editor_name == 'Rider'}")

is_customer_starred = True
print("\nWeather")
print(f"• Is this customer starred? \n\tAnswer: {is_customer_starred == False}")
print(f"• Is this customer starred? \n\tAnswer: {is_customer_starred == True}")

web_browsers = ['Microsoft Edge', 'Google Chrome', 'Opera', 'Mozilla Firefox', 'Brave', 'Safari']
print("\nWeather")
print(f"• Is Visual Studio a web browser? \n\tAnswer: {'Visual Studio' in web_browsers}")
print(f"• Google Chrome is not a web browser. \n\tAnswer: {'Google Chrome' not in web_browsers}")
