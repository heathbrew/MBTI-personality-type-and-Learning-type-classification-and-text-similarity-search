from flask import Flask, request, render_template, redirect

server = Flask(__name__)

from helper import send_gptnew

@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'chat_2.html', question="NULL", res="Question can't be empty!",temperature="NULL")
        question = request.form['question']
        temperature = float(request.form['temperature'])
        print("======================================")
        print("Receive the question:", question)
        print("Receive the temperature:",temperature)
        res = send_gptnew(question.lower().title(),temperature)
        print("Q: \n", question)
        print("A: \n", res)

        return render_template('chat_2.html', question=question, res=str(res), temperature=temperature)
    return render_template('chat_2.html', question=0)

if __name__ == '__main__':
    server.run(debug=True)
