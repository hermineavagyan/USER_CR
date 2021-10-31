from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__(self,data):
            self.id = data['id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.age = data['age']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
            self.dojo = None
            
    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data) # Returns an integer
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        ninja_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(ninja_from_db[0]) 
    
    @classmethod
    def get_one_with_dojo(cls, data):
        query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE ninjas.id = %(id)s;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        ninja_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        ninja_instance = cls(ninja_from_db[0])
        print(patient_from_db) # Show the list of dictionaries
        
        dojo_data = {
            "id": ninja_from_db[0]['dojos.id'],
            "name": ninja_from_db[0]['dojos.name'],
            "created_at": ninja_from_db[0]['dojos.created_at'],
            "updated_at": ninja_from_db[0]['dojos.updated_at'],
        }
        ninja_instance.doctor = dojo.Dojo(dojo_data) # cls(data) makes an instance of a class
        return ninja_instance # Return ninja with the dojo
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = [] 
        for ninja in ninjas_from_db:
            ninjas.append(cls(ninja)) 
        return ninjas
    
    @classmethod
    def get_all_with_dojo(cls):
        query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id;"
        ninjas_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        
        ninja_instances = [] # List of instances of the ninja class
        for this_ninja in ninjas_from_db: # Loop through all patients
            this_ninja_instance = cls(this_ninja) # Create instance of Car class
            # Get dojo for this ninja
            dojo_data = {
                "id": this_ninja['dojos.id'],
                "name": this_ninja['dojos.name'],
                "created_at": this_ninja['dojos.created_at'],
                "updated_at": this_ninja['dojos.updated_at'],
            }
            this_dojo = dojo.Dojo(dojo_data) # Create an instance of the Dojo class
            this_ninja_instance.dojo = this_dojo # This links the dojo object to this specific patient
            ninja_instances.append(this_ninja_instance) # Append the ninja with the dojo linked to it
        return ninja_instances # Return all the ninjas with the dojo linked accordingly
    
    @classmethod
    def edit_one(cls, data):
        # NEED FOREIGN KEY doctor_id!
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s,age = %(age)s, dojo_id = %(dojo_id)s WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(dojos_and_ninjas_schema).query_db(query, data)
