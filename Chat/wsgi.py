from app import create


app = create()

if __name__ == '__main__':
    app.sk.run(app,host='0.0.0.0',port=5001)
