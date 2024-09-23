# import firebase_admin
# from firebase_admin import credentials, db
# from dotenv import load_dotenv
# load_dotenv("./.env")
# import os

# print("Resetting the database...")

# # Firebaseのサービスアカウントキーのパス
# SERVICE_ACCOUNT_KEY_PATH = os.getenv("FB_SERVICE_ACCOUNT_KEY_PATH")

# # Firebase Admin SDKの初期化
# try:
#     cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
#     firebase_admin.initialize_app(cred, {
#         'databaseURL': os.getenv("FB_DATABASE_URL")
#     })
# except ValueError as e:
#     print(f"Error initializing Firebase Admin SDK: {e}")
#     raise

# # データベースのリセット
# def reset_database():
#     ref = db.reference('/')
#     ref.set()
# if __name__ == "__main__":
#     reset_database()

# # db.reference('/') を返す関数
# def get_db(path='/'):
#     return db.reference(path)