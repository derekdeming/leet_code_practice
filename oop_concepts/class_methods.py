class Youtube: 
    def __init__(self, username, subscribers = 0, subscriptions=0): 
        self.username = username 
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user): 
        user.subscribers += 1
        self.subscriptions += 1 

    
user1 = Youtube('Derk')
user2 = Youtube('Frank')

user1.subscribe(user2)

print(f'user1 subscribers: {user1.subscribers}')
print(f'user1 subscriptions: {user1.subscriptions}')


print(f'user2 subscribers: {user2.subscribers}')
print(f'user2 subscriptions: {user2.subscriptions}')