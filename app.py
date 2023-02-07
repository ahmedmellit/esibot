from flask import Flask, render_template, request
#from transformers import pipeline

#qa_model = pipeline("question-answering")
TEC = "TEC (Technique d'Expression et de Communication) is a French term that refers to techniques for effective communication and expression. It is a pedagogical approach that teaches individuals how to express themselves clearly and effectively in various communication contexts, including speaking, writing, and public speaking. This approach also aims to develop critical thinking skills, creativity, and emotional intelligence. The objective of TEC is to help people communicate with confidence, clarity, and impact, in order to achieve their personal and professional goals."
PM = "Project management is the process of planning, organizing, and controlling resources and procedures to achieve specific goals and meet project requirements. It includes defining project objectives, determining tasks and deadlines, and coordinating the efforts of team members to successfully complete the project within time and budget constraints."
IR = "Information retrieval (IR) is the process of accessing, searching and retrieving information from large collections of data or databases. It is the process of identifying relevant information from a collection of data, either structured or unstructured, and presenting it in a meaningful way. The goal of IR is to provide users with the information they need as quickly and accurately as possible. This can be accomplished through techniques such as indexing, searching, and ranking of documents, as well as the use of algorithms and natural language processing to understand the intent of the user. IR is widely used in fields such as library and information science, search engines, and digital libraries."
ECM = "ECM stands for Enterprise Content Management. It is a system for managing and organizing digital content within an organization. ECM includes processes for capturing, storing, organizing, and accessing content such as documents, images, videos, and audio files. The goal of ECM is to improve the efficiency and productivity of an organization by streamlining the way information is managed and accessed."
BI = "BI stands for Business Intelligence. It refers to the set of strategies, techniques, technologies, and processes used by organizations to gather, store, process, analyze, and present data in a meaningful way to help improve decision making and business performance. BI includes data warehousing, data analysis, data visualization, reporting, dashboards, and other tools and processes used to transform data into actionable insights and informed decision-making."
KM = "Knowledge Management (KM) is the systematic process of acquiring, creating, sharing, using, and preserving information and knowledge within an organization. It aims to maximize the value of an organization's collective knowledge and expertise by capturing, organizing, and leveraging it for the benefit of all stakeholders. KM includes a variety of practices, technologies, and processes for capturing, storing, retrieving, and sharing knowledge and information within an organization. It enables organizations to improve collaboration, decision-making, innovation, and overall performance by effectively managing their intellectual capital."
MANAGEMENT = "Management is the process of planning, organizing, directing, and controlling resources (such as human, financial, physical, and informational) to achieve organizational goals and objectives. It involves making decisions and taking action to achieve desired outcomes and involves leadership, decision-making, communication, problem-solving, and risk management. Management also includes managing people and teams, delegating tasks, monitoring performance, and evaluating results. The goal of management is to achieve efficient and effective utilization of resources to achieve desired results."
MARKETING = "Marketing is the process of identifying, anticipating and satisfying the needs and wants of a target market through the creation, promotion and distribution of products and services. It involves researching, promoting, selling and distributing a product or service. The goal of marketing is to build customer relationships, increase sales and drive long-term growth for a business."


## {'answer': 'İstanbul', 'end': 39, 'score': 0.953, 'start': 31}


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/tec', methods=["GET", "POST"])
def tec():

    if request.method == 'POST':
        query = request.form['question']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = "qa_model(question = query, context = TEC)['answer']"#

    return render_template('tec.html', **locals())



@app.route('/pm', methods=["GET", "POST"])
def pm():

    if request.method == 'POST':
        query = request.form['question']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = "qa_model(question = query, context = PM)['answer']"

    return render_template('pm.html', **locals())



@app.route('/management', methods=["GET", "POST"])
def management():

    if request.method == 'POST':
        query = request.form['question']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = "qa_model(question = query, context = MANAGEMENT)['answer']"

    return render_template('management.html', **locals())



@app.route('/km', methods=["GET", "POST"])
def km():

    if request.method == 'POST':
        query = request.form['question']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = "qa_model(question = query, context = KM)['answer']"

    return render_template('km.html', **locals())



@app.route('/ecm', methods=["GET", "POST"])
def ecm():

    if request.method == 'POST':
        query = request.form['question']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = "qa_model(question = query, context = ECM)['answer']"

    return render_template('ecm.html', **locals())


@app.route('/bi', methods=["GET", "POST"])
def bi():

    if request.method == 'POST':
        query = request.form['question']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = "qa_model(question = query, context = BI)['answer']"

    return render_template('bi.html', **locals())


@app.route('/marketing', methods=["GET", "POST"])
def marketing():

    if request.method == 'POST':
        query = request.form['question']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = "qa_model(question = query, context = MARKETING)['answer']"

    return render_template('marketing.html', **locals())


@app.route('/IR', methods=["GET", "POST"])
def IR():

    if request.method == 'POST':
        query = request.form['question']
        print(query)

        prompt = 'AI Suggestions for {} are:'.format(query)
        openAIAnswer = "qa_model(question = query, context = IR)['answer']"

    return render_template('IR.html', **locals())




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
