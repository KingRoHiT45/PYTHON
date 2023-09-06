def get_data_from_mongo():
<<<<<<< HEAD
    print("hello!")
=======

    from pymongo.mongo_client import MongoClient
    import pandas as pd

    uri = "mongodb+srv://shubham36deshpande:shubham123@mycluster.ukw4sv9.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri)

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    database = client["mydatabse"]
    collection = database["advertising_json"]
    data = [i for i in collection.find()]
    # print(data)
    df = pd.DataFrame(data)
    print(df.columns)
    df.rename(columns={'_id':'id', 
            'Daily Time Spent on Site':'daily_time_spent_on_site', 
            'Area Income':'income', 
            'Daily Internet Usage':'daily_internet_usage',
            'Ad Topic Line':'topic',
            'Clicked on Ad':'clicked'}, inplace=True)
    print(df)
    df.to_csv('/opt/airflow/advertising1.csv', index=False)
>>>>>>> a7b6f8f18a4cb9f94c545234a1ce0dc6fffd1f8c
get_data_from_mongo()