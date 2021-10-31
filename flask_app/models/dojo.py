# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
# model the class after the users table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in dojos_from_db:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        dojo_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(dojo_from_db[0])
    
    @classmethod
    def get_one_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        #Grab a list of dictionaries where each dictioaryis a row from db
        dojo_from_db_with_ninjas = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        dojo_instance = cls(dojo_from_db_with_ninjas[0])
        for this_ninja in dojo_from_db_with_ninjas:
            ninja_data = {
                "id": this_ninja['ninjas.id'],
                "first_name": this_ninja['first_name'],
                "last_name": this_ninja['last_name'],
                "age": this_ninja['age'],
                "created_at": this_ninja['ninjas.created_at'],
                "updated_at": this_ninja['ninjas.updated_at'],
            }
            dojo_instance.ninjas.append(ninja.Ninja(ninja_data))
        return dojo_instance
    
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO dojos ( name,created_at, updated_at ) VALUES (%(name)s, NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s, WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)