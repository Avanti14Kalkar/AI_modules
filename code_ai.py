import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("Gemini_api_key"))
model = genai.GenerativeModel('gemini-2.5-flash')
print("Enter the code below...(type: exit or quit to exit)")

while True:
    code = input('''Enter a code:''')
    if code.lower() == 'exit' or code.lower() == 'quit':
        break

    # promt to explain the code
    promt = f'''Explain the following code in simple and clear language step by step {code}'''

    try:
        response = model.generate_content(promt)
        explain = response.text
        print('\n Code Explaination \n')
        print(explain)

    except Exception as e:
        print('Error:', e)