from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from book import Book
from author import Author
from app import app, db 
import yaml



#class book
    
@app.route('/book', methods=['POST', 'GET'])
def data():
    
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        bookid = body['bookid']
        bookname = body['bookname']
        authorname = body['authorname']
        #price = body['price']


        data = Book(id, bookname, authorname)
        db.session.add(data)
        db.session.commit()

        return jsonify({
            'status': 'Data is posted to PostgreSQL!',
            'bookid': bookid,
            'bookname': bookname,
            'authorname': authorname
            #'price': price

        })     
    
 
    # GET all data from database & sort by id
    if request.method == 'GET':
        # data = User.query.all()
        data = Book.query.order_by(Book.id).all()
        print(data)
        dataJson = []
        for i in range(len(data)):
           
            dataDict = {
                'bookid': str(data[i]).split('/')[0],
                'bookname': str(data[i]).split('/')[1],
                'authorname': str(data[i]).split('/')[2]
                #'price': str(data[i]).split('/')[3]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson)
    
@app.route('/<string:bookid>', methods=['GET', 'DELETE', 'PUT'])
def onedata(bookid):

    # GET a specific data by id
    if request.method == 'GET':
        data = Book.query.get(bookid)
        print(data)
        dataDict = {
            'bookid': str(data).split('/')[0],
            'bookname': str(data).split('/')[1],
            'authorname': str(data).split('/')[2]
            #'price': str(data[i]).split('/')[3]

        }
        return jsonify(dataDict)
        
    # DELETE a data
    if request.method == 'DELETE':
        delData = Book.query.filter_by(bookid=bookid).first()
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is deleted from PostgreSQL!'})


      # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        newId = body['bookid']
        newName = body['bookname']
        newAge = body['authorname']
       # newPrice = body['price']
        editData = Book.query.filter_by(bookid=bookid).first()
        editData.bookid = newId
        editData.bookname = newAge
        editData.authorname = newName 
       # editData.price = newPrice
        db.session.commit()
        return jsonify({'status': 'Data '+bookid+' is updated from PostgreSQL!'})


#-------------------------------------------------------------------------------------------------------------------------
#class author 


    
@app.route('/author', methods=['POST', 'GET'])
def data():
    
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        author_id = body['author_id']
        author_name = body['author_name']
        book_name = body['book_name']
        #price = body['price']


        data = Author(author_id, author_name, book_name)
        db.session.add(data)
        db.session.commit()

        return jsonify({
            'status': 'Data is posted to PostgreSQL!',
            'auhtor_id': author_id,
            'auhtor_name': author_name,
            'book_name': book_name
            #'price': price

        })     
    
 
    # GET all data from database & sort by id
    if request.method == 'GET':
        # data = User.query.all()
        data = Author.query.order_by(Author.id).all()
        print(data)
        dataJson = []
        for i in range(len(data)):
           
            dataDict = {
                'author_id': str(data[i]).split('/')[0],
                'author_name': str(data[i]).split('/')[1],
                'book_name': str(data[i]).split('/')[2]
                #'price': str(data[i]).split('/')[3]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson)
    
@app.route('/<string:author_id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(author_id):

    # GET a specific data by id
    if request.method == 'GET':
        data =Author.query.get(author_id)
        print(data)
        dataDict = {
            'author_id': str(data).split('/')[0],
            'author_name': str(data).split('/')[1],
            'book_name': str(data).split('/')[2]
            #'price': str(data[i]).split('/')[3]

        }
        return jsonify(dataDict)
        
    # DELETE a data
    if request.method == 'DELETE':
        delData = Author.query.filter_by(authorid=author_id).first()
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status': 'Data '+author_id+' is deleted from PostgreSQL!'})


      # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        newId = body['author_id']
        newName = body['auhtor_name']
        newAge = body['book_name']
       # newPrice = body['price']
        editData = Author.query.filter_by(author_id=author_id).first()
        editData.author_id = newId
        editData.author_name = newAge
        editData.book_name = newName 
       # editData.price = newPrice
        db.session.commit()
        return jsonify({'status': 'Data '+author_id+' is updated from PostgreSQL!'})


if __name__ == '__main__':
    app.debug = True
    app.run()



