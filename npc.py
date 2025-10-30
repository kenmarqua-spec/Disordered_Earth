import random
import json
from datetime import datetime

class NPC:
    def __init__(self, name, age=18, job=None, trust=50):
        self.name = name
        self.age = age
        self.job = job
        self.trust = trust
        self.knowledge = []
        self.family = []
        self.memory = []
        self.birthday = datetime.now().strftime("%Y-%m-%d")

    def learn(self, recipe):
        if recipe not in self.knowledge:
            self.knowledge.append(recipe)
            self.memory.append(f"Learned {recipe}")
            return f"{self.name} learned how to make {recipe}."
        return f"{self.name} already knows {recipe}."

    def teach(self, other, recipe):
        if recipe in self.knowledge and recipe not in other.knowledge:
            other.knowledge.append(recipe)
            self.memory.append(f"Taught {other.name} {recipe}")
            other.memory.append(f"Learned {recipe} from {self.name}")
            return f"{self.name} taught {other.name} how to make {recipe}."
        return f"{self.name} couldn’t teach {recipe}."

    def work(self):
        self.trust += random.randint(1, 5)
        self.memory.append(f"Worked as a {self.job}")
        return f"{self.name} worked today as a {self.job}."

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "job": self.job,
            "trust": self.trust,
            "knowledge": self.knowledge,
            "family": self.family,
            "memory": self.memory
        }

def generate_population(count=5):
    names = ["Ari", "Lena", "Kai", "Noah", "Mila", "Rin", "Theo"]
    jobs = ["hunter", "farmer", "builder", "teacher", "miner"]
    return [NPC(random.choice(names), random.randint(16, 40), random.choice(jobs)) for _ in range(count)]

if __name__ == "__main__":
    population = generate_population()
    print(json.dumps([npc.to_dict() for npc in population], indent=2))