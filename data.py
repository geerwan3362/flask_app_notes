from app import db,User,app
with app.app_context():
    user = User(username = "geerwan",password = "1234")
    db.session.add(user)
    db.session.commit()
    print("User created successfully!")