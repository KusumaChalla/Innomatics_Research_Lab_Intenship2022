from flask import Flask, render_template, request
import re
app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def regexp_fun():
    if request.method == 'POST':
        regexp = request.form['input1']
        string_input = request.form['input2']
        count = 0
        stri = ""
        for match in re.finditer(regexp, string_input):
            count += 1
            #print("match", count, match.group(), "start index", match.start(), "End index", match.end())
            stri = stri + "match " + str(count) + " " + match.group() + " start index " + str(
                match.start()) + " End index " + str(match.end())+"||"
        return render_template('page1.html',count=count,stri = stri,regexp1= regexp,stro = string_input)

    else:
        count =None
        return render_template('page1.html',count = count)


if __name__ == '__main__':
    app.run(debug=True)