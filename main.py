class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.track = list(tracks)
        self.score = float(score)

    
    def change_name(self, new_name):
        self.change_name = new_name
        print("student name changed to", new_name)

    def change_age(self, new_age):
        self.change_age = new_age
        print("student age changed to", new_age)

    def add_track(self, new_track):
        self.add_track = new_track
        print("student new track is", new_track)

    def get_score(self):
        return self.score
    


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()