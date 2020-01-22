from flask import Flask, request, render_template
import stories

app = Flask(__name__)

@app.route('/')
def makeInputVals():
  """Renders html form based on story instance."""
  inputs = stories.story.prompts # story instance words list
  return render_template('homepage.html', inputs = inputs)

@app.route('/story', methods=['POST'])
def generate():
  """Accepts form input from user."""
  answers = request.form # makes dict from user inputs
  story_text = stories.story.generate(answers)
  return render_template('yourstory.html', story_text=story_text) 
  # renders string returned by helper func

