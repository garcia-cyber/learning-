from  flask import  Flask , redirect,flash,session, url_for, render_template
import mysql.connector as mysql 

"""
################################## configuration de la page   
"""
learning = Flask(__name__)

"""

################################## page d'accueil  
 
"""
@learning.route('/')
@learning.route('/home')
def home():
    return render_template('front_end/index.html')


@learning.route('/about')
def about():
    return render_template('front_end/about-us.html')

@learning.route('/contact')
def contact():
    return render_template('front_end/contact.html')

















"""
################################## page de configuration d'affichage genre boucle    
"""

if __name__ == '__main__':
    learning.run(debug=True)

