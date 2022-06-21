import pymongo
# cluster url
connectionString = "mongodb+srv://Rajeev:EnterPassword@cluster0.rrevs.mongodb.net/test"

#create function for insert document
def insertDocument():
    studentInfo = {
        "name": "Sumesh",
        "section": 2,
        "maths_marks": 60,
        "sst_marks": 70
    }
    student_id = collection.insert_one(studentInfo).inserted_id
    print(f"Student with id {student_id} has been created")

# #function for read doucment
def readDocuments():
    # Inserting a Document
    # Reading a Collection
    # Using find function
    myStudents = collection.find({"section": 1, "name": "Rajeev"})
    # print(myStudents)
    for student in myStudents:
        print(student)
    # Using findOne function
    myStudent = collection.find_one({"section": 1})
    print(myStudent)

#function for update the document
def updateDocuments():
    # $inc it means increment
    # collection.update_one({"section": 1}, {'$inc': {'section': 100}})
    collection.update_many({}, {'$inc': {'section': 100}})

#for delete document
def deleteDocuments():
    # r = collection.delete_one({"section": 101})
    # # deleted_count this is used for check how much document is deleted
    # print(r.deleted_count)
    r = collection.delete_many({"section":101})
    print(r.deleted_count)



if __name__ == '__main__':
    client = pymongo.MongoClient(connectionString)
    # Creating a Database for a School
    db = client['wisdom-academy']

    # Creating a Collection
    collection = db.class1

    # CRUD: Create, Read, Update, Delete
    # 1. Create
    # insertDocument()

    # 2. Read(find)
    # readDocuments()

    # 3. Update
    # updateDocuments()

    # 4. Delete
    deleteDocuments()