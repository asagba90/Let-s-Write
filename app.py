from flask import Flask, render_template, request, jsonify, make_response
import config
import blog


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        if 'form1' in request.form:
            prompt = request.form['blogTopic']
            blogT = blog.generateBlogTopics(prompt)
            blogTopicIdeas = blogT.replace('\n', '<br>')


        if 'form2' in request.form:
            prompt = request.form['blogSection']
            blogT = blog.generateBlogSections(prompt)
            blogSectionIdeas = blogT.replace('\n', '<br>')

        if 'form3' in request.form:
            prompt = request.form['blogExpander']
            blogT = blog.blogSectionExpander(prompt)
            blogExpanded = blogT.replace('\n', '<br>')


    return render_template('index.html', **locals())

@app.route('/getAnswer', methods=['GET', "POST"])
def get_aswers():
    req = request.get_json()
    question = req['prompt']
    generated = blog.answerQuestion(question)
    
    res = make_response(jsonify({"answer": generated}), 200)
    return res




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True) 
