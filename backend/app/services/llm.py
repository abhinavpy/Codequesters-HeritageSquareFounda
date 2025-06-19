import litellm

def ask_litellm(prompt, model="gemini-pro"):
    response = litellm.completion(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']