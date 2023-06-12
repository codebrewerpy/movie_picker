import random
import requests
from bs4 import BeautifulSoup
import gradio as gr

url = "https://www.imdb.com/chart/top/"

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    movie_title = soup.select("td.titleColumn")
    movie0 = movie_title[0].text.split()
    print(movie0)

def greet(name):
    return "Hello " + name + "!"

def hi(hi):
    return "hi"

if __name__ == "__main__":
    #main()
    demo = gr.Interface(fn=hi, inputs="text", outputs="text", title="Mr. Chef")

    demo.launch(share=False)



    # demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    #
    # demo.launch()