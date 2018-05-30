from flask import (
   Blueprint, flash, g, redirect, render_template, request, url_for 
)
from werkzeug.exceptions import abort

bp = Blueprint('frequency', __name__)

def get_most_frequent(text):
   punct = "!?'\",.:;"
   punct2 = "-_"

   for mark in punct:
      text = text.replace(mark, '')
   
   for mark in punct2:
      text = text.replace(mark, ' ')
   print(text)

   max = 0
   max_word = None
   words = text.split()
   for word in words:
      tmp = text.count(word)
      if tmp > max:
         max = tmp
         max_word = word.title()
         
   return {'word': max_word, 'freq': max}
   

@bp.route('/frequency', methods=('GET', 'POST'))
def index():
   if request.method == 'POST':
      title = request.form['title']
      body = request.form['body']
      error = None
      
      output = get_most_frequent(body)

      return render_template('frequency/scored.html', title=title, output=output)
   
   return render_template('frequency/index.html')