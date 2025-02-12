from pymongo import MongoClient
import sqlalchemy

# SQL Connection (Example: PostgreSQL)
sql_engine = sqlalchemy.create_engine("postgresql://user:password@localhost:5432/yourdb")

# MongoDB Connection
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["your_mongo_db"]
mongo_collection = mongo_db["onboarding"]

# Get SQL Table Columns
def get_sql_schema(table_name):
    query = f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}';"
    with sql_engine.connect() as conn:
        result = conn.execute(query).fetchall()
    return {row[0]: row[1] for row in result}

# Get MongoDB Schema Sample
def get_mongo_schema():
    sample_doc = mongo_collection.find_one()
    return {key: type(value).__name__ for key, value in sample_doc.items()}

# Compare Schemas
sql_schema = get_sql_schema("clients")
mongo_schema = get_mongo_schema()

print("SQL Schema:", sql_schema)
print("MongoDB Schema:", mongo_schema)
