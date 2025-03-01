from openai import db

#id, userinput, openai response
class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userinput = db.Column(db.String(), unique = False, nullable = False)
    aiResponse = db.Column(db.String(), unique = False, nullable = True)

    def to_json(self):
        return{
            "id": self.id,
            "userInput": self.userInput,
            "aiResponse" : self.aiResponse
        }
