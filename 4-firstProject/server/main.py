# -*- codign: utf-8 -*-

# Libraries
from flask import Flask, render_template, request, flash, redirect
from contactModel import Contact
# Init 
app = Flask(__name__)
app.secret_key = 'holapianola'
app.debug = True
# Routes
@app.route(r'/', methods=['GET'])
def contactBook():
    contacts = Contact.query().fetch()
    return render_template('book.html',contacts=contacts)

@app.route(r'/add', methods=['GET', 'POST'])
def addContact():
    if request.form:
        contact = Contact(
                            name=request.form.get('name'),
                            number=request.form.get('number'),
                            email=request.form.get('email')
                        )
        print(request.form.get('name'))
        print(request.form.get('number'))
        print(request.form.get('email'))
        contact.put()
        flash('Se anadio el contacto')
    return render_template('add-contact.html')

@app.route(r'/contacts/<uid>',methods=['GET'])
def contactDetails(uid):
    contact = Contact.get_by_id(int(uid))
    if not contact:
        return redirect('/', code=301)
    return render_template('detail.html',contact=contact)

@app.route(r'/delete', methods=['POST'])
def deleteContact():
    contact = Contact.get_by_id(int(request.form.get('uid')))
    contact.key.delete()
    return redirect('/contacts/{}'.format(contact.key.id()))


if __name__ == "__main__":
    app.run()
    
