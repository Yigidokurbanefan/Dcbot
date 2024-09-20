import google.generativeai as genai

genai.configure(api_key="AIzaSyBOzEBs2Kjacmyzm_-dnjGLiCAkJ5Bl4HM")
model = genai.GenerativeModel('gemini-pro')


def geminim(mesaj):
    response = model.generate_content(mesaj)
    with open("output.txt", "w", encoding = "utf-8") as file:  
        for chunk in response:
            file.write(chunk.text)

if __name__ == "__main__":
    """mesaj = input("Soru sor")
    response = model.generate_content(mesaj)
    for chunk in response:
        print(chunk.text)"""
