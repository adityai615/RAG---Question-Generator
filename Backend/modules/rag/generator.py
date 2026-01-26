import google.generativeai as genai
import os

class QuestionGenerator:
    def __init__(self):
        """
        Initialize Gemini model using API Key.
        Use Gemini 1.5 Pro for BEST accuracy,
        Gemini 1.5 Flash for speed + lower cost.
        """
        genai.configure(api_key=os.getenv("AIzaSyAnvvE2Si0jbHtD0uVOERY2ndYPdl7nOo8"))

        # BEST accuracy:
        self.model = genai.GenerativeModel("gemini-1.5-pro")

        # If you want faster & cheaper:
        # self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_new_question(self, retrieved_questions: list, num_questions: int = 5):
        """
        Generate highly accurate, unique, non-repetitive academic questions
        using Gemini RAG-style prompting.
        """

        prompt = f"""
You are an expert academic exam question generator specializing in creating
**unique, original, and conceptually deep** questions.

Below are reference Previous-Year Questions (PYQs) for topic context:
```
{retrieved_questions}
```

You must generate **{num_questions} brand new exam-level questions**.

### STRICT RULES:
- Do NOT copy text from reference questions.
- Do NOT rephrase or restructure. **BE FULLY ORIGINAL.**
- Maintain same difficulty level and subject domain.
- Questions must be conceptually rich, accurate, and exam-ready.
- Prefer numerical, application-based, or deeper conceptual questions.
- Output must be in a clean numbered list format.

### Output Format (VERY IMPORTANT):
1. Question 1...
2. Question 2...
...
{num_questions}. Question {num_questions}...

Now generate the new questions.
        """

        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.75,  # balanced creativity + accuracy
                "top_p": 0.9,
                "top_k": 40,
                "max_output_tokens": 1024
            }
        )

        return response.text
