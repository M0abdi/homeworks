

class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.is_online = True
    
    def send_message(self, message, chat):
        if self.is_online:
            print(f"{self.name} sent: {message}")
            chat.receive_message(self, message)
        else:
            print(f"{self.name} is offline!")

# Bot 
class Bot:
    def __init__(self, name):
        self.name = name
        self.is_online = True
    
    def send_message(self, message, chat):
        print(f"Bot {self.name} sent: {message}")
        chat.receive_message(self, message)
    
    def process_command(self, command):
        if command == "/time":
            return "It's 10:30 AM"
        elif command == "/weather":
            return "The weather is sunny"
        else:
            return "I don't understand this command"

# Chat 
class Chat:
    def __init__(self, name):
        self.name = name
        self.messages = []
        self.members = []
    
    def add_member(self, person):
        self.members.append(person)
        print(f"{person.name} joined {self.name}")
    
    def receive_message(self, sender, message):
        self.messages.append((sender.name, message))
        print(f"Message saved in {self.name}")
    
    def show_messages(self):
        print(f"\n--- Messages in {self.name} ---")
        for sender, message in self.messages:
            print(f"{sender}: {message}")

# Private Chat 
class PrivateChat(Chat):
    def __init__(self, user1, user2):
        name = f"Private Chat: {user1.name} & {user2.name}"
        super().__init__(name)
        self.user1 = user1
        self.user2 = user2
        self.add_member(user1)
        self.add_member(user2)

# Group 
class Group(Chat):
    def __init__(self, name, admin):
        super().__init__(name)
        self.admin = admin
        self.add_member(admin)
        print(f"Group {name} created by {admin.name}")

# Message 
class Message:
    def __init__(self, text, sender):
        self.text = text
        self.sender = sender
        self.time = "Just now"
    
    def show(self):
        print(f"{self.sender.name}: {self.text} ({self.time})")

# Text Message 
class TextMessage(Message):
    def __init__(self, text, sender):
        super().__init__(text, sender)
        self.type = "Text"
    
    def get_length(self):
        return len(self.text)

# Photo Message 
class PhotoMessage(Message):
    def __init__(self, sender, caption=""):
        super().__init__("Photo", sender)
        self.type = "Photo"
        self.caption = caption
    
    def show(self):
        print(f"{self.sender.name} sent a photo: {self.caption}")

# Notification 
class Notification:
    def __init__(self, user, message):
        self.user = user
        self.message = message
    
    def send(self):
        print(f" Notification for {self.user.name}: {self.message}")




# Running the app
print("=== Telegram Program ===\n")

# Create users
ali = User("Ali", "89773450089")
melika = User("melika", "89123510543")
weather_bot = Bot("WeatherBot")

# Create chats
private_chat = PrivateChat(ali, melika)
group = Group("Friends", ali)

# Add members to group
group.add_member(melika)
group.add_member(weather_bot)

print("\n\n--- Sending Messages ---")

# Send messages in private chat
ali.send_message("Hello melika! How are you?", private_chat)
melika.send_message("Hi Ali! I'm good, thank you", private_chat)

# Send messages in group
ali.send_message("Hello everyone!", group)

# Bot sends message
weather_bot.send_message("Today's weather is rainy", group)

# Create different types of messages
text_msg = TextMessage("This is a text message", ali)
photo_msg = PhotoMessage(melika, "Photo of nature")

print("\n\n--- Showing Messages ---")
text_msg.show()
photo_msg.show()

# Notification
notif = Notification(melika, "New message from Ali")
notif.send()

print("\n--- Chat History ---")
private_chat.show_messages()
group.show_messages()

print("\n--- Testing Bot ---")
result = weather_bot.process_command("/time")
print(f"Bot said: {result}")

print("\n=== Program Ended ===")
