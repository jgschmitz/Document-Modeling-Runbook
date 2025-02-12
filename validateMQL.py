# SQL record count
sql_count_query = "SELECT COUNT(*) FROM clients;"
with sql_engine.connect() as conn:
    sql_count = conn.execute(sql_count_query).scalar()

# MongoDB record count
mongo_count = mongo_collection.count_documents({})

# Compare counts
print(f"SQL Record Count: {sql_count}")
print(f"MongoDB Record Count: {mongo_count}")

if sql_count == mongo_count:
    print("✅ Data consistency verified!")
else:
    print("⚠️ Data inconsistency detected!")
