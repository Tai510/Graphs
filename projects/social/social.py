import random 
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
class User:
    def __init__(self, name):
        self.name = name
class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
    # def get_friends(self, user_id):
    #     return self.friendships[user_id]       
    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
       # Add users
       # call addUser() until our number of users is num_users
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        # Create friendships
        # totalFriendships = avg_friendships * num_users
        # Generate a list of all possible friendships
        possible_friendships = []
         # Avoid dups by ensuring the first ID is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
              # Shuffle the list
            random.shuffle(possible_friendships)
        print(possible_friendships)
         # Slice off totalFriendships from the front, create friendships
        totalFriendships = avg_friendships * num_users // 2
        print(f"Friendships to create: {totalFriendships}\n")
        for i in range(totalFriendships):
            friendship = possible_friendships[i]
            self.add_friendship( friendship[0], friendship[1] )
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        #Do a BFT to visit each user in our extended social network
        #Create an empty queue
        q = Queue()
        visited = {}  # Note that this is a dictionary, not a set
       #Add a path to the starting node to the queue
        q.enqueue([user_id])
       # While the queueis not empty ...
        while q.size() > 0:
       # #Dequeue the first path from the queue
         path = q.dequeue()
         #grab last vertex path the path
        v = path[-1]
       # check if its been visited
       # if not mark it as visited
        if v not in visited:
       # when we reach an unvisited node, add the path to visited dictionary
         visited[v] = path
       # Add a path to each neighbor to the back of the queue
        for friendID in self.friendships[v]:
            #copy path
           path_copy = path.copy()
           #add friend to the path
           path_copy.append(friendID)
           q.enqueue(path_copy)
       # Return visited dictionary 
        return visited
if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)