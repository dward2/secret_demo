from pymodm import connect, MongoModel, fields
import os

m_pswd = os.environ.get("MONGODB")
m_id = os.environ.get("MONGODB_ID")


connect("mongodb+srv://{}:{}@bme547.ba348.mongodb.net/".format(m_id, m_pswd) + 
            "AMongo?retryWrites=true&w=majority&appName=BME547")


class Patient(MongoModel):
    id = fields.IntegerField()
    name = fields.CharField()


def add_patient(mrn, name):
    new_patient = Patient(id=mrn, name=name)
    answer = new_patient.save()
    print(answer)
    return answer


if __name__ == "__main__":
    add_patient(101, "David")

