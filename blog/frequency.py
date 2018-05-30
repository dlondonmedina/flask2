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
   max = 0
   max_word = None
   words = text.split()
   for word in words:
      tmp = word.count(text)
      if tmp > max:
         max = tmp
         max_word = word
         
   return {'word': maxword, 'freq': max}
   


@bp.route('/', methods=('GET', 'POST'))
def frequency():
   if request.method == 'POST':
      title = request.form('title')
      body = request.form['body']
      error = None
      
      output = get_frequency(body)

      return render_template('frequency/scored.html', title=title, output=output)
   
   return render_template('frequency/index.html')