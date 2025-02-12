import pandas as pd

# Get data from MongoDB
cursor = mongo_collection.find({}, {"_id": 0})  # Exclude _id for tabular output
df = pd.DataFrame(list(cursor))

# Display the extracted table
import ace_tools as tools
tools.display_dataframe_to_user(name="MongoDB Extracted Table", dataframe=df)
