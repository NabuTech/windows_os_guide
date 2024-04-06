class Task: 
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        return f"{self.name}: {self.content}"
    
class Topic:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        tasks_str = "\n".join([f" - {task}" for task in self.tasks])
        return f"{self.name}:\n{tasks_str}"
    
class Section:
    def __init__(self, name):
        self.name = name
        self.topics = []

    def add_topic(self, topic):
        self.topics.append(topic)

    def __str__(self):
        topics_str = "\n".join([f"{topic}" for topic in self.topics])
        return f"{self.name}:\n{topics_str}"
    
    def  to_dict(self):
        return {
            "name": self.name,
            "topics": [topic.to_dict() for topic in self.topics]
        }
