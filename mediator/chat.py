class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        s = f"{sender}: {message}"
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

    def privete_message(self, who, message):
        self.room.message(self.name, who, message)

    def say(self, message):
        self.room.broadcast(self.name, message)

    def str(self) -> str:
        return f'{self.name}'

class ChatRoom:
    def __init__(self) -> None:
        self.people = []

    def join(self, person):
        join_msg = f'join {person}'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def message(self, src, dst, msg):
        for p in self.people:
            if p.name == dst:
                p.receive(src, msg)


if __name__ == "__main__":
    room = ChatRoom()

    john = Person('John')
    jane = Person('Jane')

    room.join(john)
    room.join(jane)

    john.say("he room!")
    jane.say("o hey john")

    dog = Person('Dog')
    room.join(dog)
    dog.privete_message('Dog','private')