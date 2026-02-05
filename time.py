from datetime import datetime
def greet():
    current_time=datetime.now().hour
    if current_time>5 and current_time <=12:
        print("Good Morning 🌞")
    elif current_time >12 and current_time<=17:
        print("Good Afternoon 😃")
    else:
        print("Good Night 💤")
    

greet() 