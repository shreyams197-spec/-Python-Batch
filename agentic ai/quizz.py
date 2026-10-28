
from flask import Flask, request, render_template_string

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of India?",
        "answer": "delhi"
    },
    {
        "question": "What is the capital of Telangana?",
        "answer": "hyderabad"
    }
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>GK Quiz</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            margin: 0;
            padding: 40px 15px;
        }

        .container {
            background: white;
            max-width: 550px;
            margin: auto;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 20px #33333340;
        }

        h1 {
            text-align: center;
            color: #5145a5;
        }

        .question {
            background: #f4f4ff;
            padding: 18px;
            margin: 20px 0;
            border-radius: 10px;
        }

        input {
            width: 95%;
            padding: 12px;
            margin-top: 12px;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 16px;
        }

        button {
            width: 100%;
            padding: 13px;
            background: #5145a5;
            color: white;
            border: none;
            border-radius: 7px;
            font-size: 17px;
            cursor: pointer;
        }

        button:hover {
            background: #382c80;
        }

        .correct {
            color: green;
            font-weight: bold;
        }

        .wrong {
            color: red;
            font-weight: bold;
        }

        .score {
            text-align: center;
            font-size: 20px;
            color: #5145a5;
            font-weight: bold;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>🌍 Python Quiz</h1>
        <p>Answer the following questions!</p>

        <form method="POST">
            {% for q in questions %}
            <div class="question">
                <h3>{{ loop.index }}. {{ q.question }}</h3>

                <input type="text"
                       name="answer{{ loop.index0 }}"
                       placeholder="Enter your answer"
                       value="{{ answers[loop.index0] }}"
                       required>

                {% if submitted %}
                    {% if results[loop.index0] %}
                        <p class="correct">Correct answer! ✓</p>
                    {% else %}
                        <p class="wrong">
                            Wrong answer! Correct answer:
                            {{ q.answer.title() }}
                        </p>
                    {% endif %}
                {% endif %}
            </div>
            {% endfor %}

            <button type="submit">Submit Answers</button>
        </form>

        {% if submitted %}
            <p class="score">
                Your Score: {{ score }} / {{ questions|length }}
            </p>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def quiz():
    submitted = request.method == "POST"
    answers = []
    results = []
    score = 0

    for i, q in enumerate(questions):
        answer = request.form.get(f"answer{i}", "").strip().lower()
        answers.append(answer)

        if submitted:
            correct = answer == q["answer"]
            results.append(correct)

            if correct:
                score += 1
        else:
            results.append(False)

    return render_template_string(
        HTML,
        questions=questions,
        answers=answers,
        results=results,
        submitted=submitted,
        score=score
    )


if __name__ == "__main__":
    app.run(debug=True)
