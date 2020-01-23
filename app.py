from flask import Flask, request, render_template
from stories import story_dict

app = Flask(__name__)


@app.route('/')
def story_menu():
    """Renders html form based on story instance."""

    return render_template('story-menu.html', story_dict=story_dict)


@app.route('/<story>', methods=['POST'])
def generate(story):
    """Accepts form input from user."""
    answers = request.form  # makes dict from user inputs
    story_text = story_dict[story].generate(answers)
    return render_template('your-story.html', story_text=story_text)
    # renders string returned by helper func


@app.route('/stories/<story>')
def make_input_vals(story):
    """Renders html form based on story instance."""
    inputs = story_dict[story].prompts  # story instance words list
    return render_template('homepage.html', inputs=inputs, story=story)
