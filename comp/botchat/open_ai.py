import openai

openai.api_key = "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"

def generate_summary(comprehension, sum_l):
    model_engine = "text-davinci-003"
    prompt = f"Please summarize the following:\n{comprehension}\n in {sum_l} words"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.5,
        max_tokens=500,
        n=1,
        stop=None,
        timeout=30,
        )
    summary = response.choices[0].text.strip()
    return summary

def generate_toc(comprehension):
    model_engine = "text-davinci-003"
    prompt = f"Please generate a table of contents for the following:\n{comprehension}"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.5,
        max_tokens=500,
        n=1,
        stop=None,
        timeout=30,
        )
    toc = response.choices[0].text.strip()
    return toc

def generate_questions(comprehension, no_ques):
    model_engine = "text-davinci-003"
    prompt = f"Please generate {no_ques} questions and answers based on the following:\n{comprehension}"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000,
        n=1,
        stop=None,
        timeout=30,
        )
    questions = response.choices[0].text.strip()
    return questions