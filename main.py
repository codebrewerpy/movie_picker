import time
import requests
import random
from bs4 import BeautifulSoup
import gradio

url = "https://www.imdb.com/chart/top/"

def main(hi):
    responce = requests.get(url) # create request
    html = responce.text # extract html from the site

    soup = BeautifulSoup(html, "html.parser")
    movietags = soup.select("td.titleColumn")
    inner_movietag = soup.select("td.titleColumn a")
    ratings = soup.select("td.posterColumn span[name=ir]")


    movie0 = movietags[0].text.split()

    # actors = inner_movietag[0]["title"]
    # print(actors)

    def movie_year(movie):
        movie_split = movie.text.split()
        year = movie_split[-1]
        return year

    # def movie_name(movie):
    #     movie_split = movie.text.split()
    #     name = movie_split[1:len(movie_split)-1]
    #     name2 = [name[i] for i in range(len(name))]
    #     return print(name2)


    year = [movie_year(movie) for movie in movietags] # using list comprehension
    title = [inner_movietag[moviename].string for moviename in range(len(inner_movietag))]
    actors = [inner_movietag[actor]["title"] for actor in range(len(inner_movietag))]
    rating = [round(float(ratings[i]["data-value"]),1) for i in range(len((ratings)))]

    #print(round(float(ratings[0]["data-value"]),1))
    #print(rating)

    movies_nr = len(title)
    indx = random.randrange(movies_nr)

    # while True:
    #     # print("Picking up movie for you....")
    #     # time.sleep(2)
    #     # print("please wait again....")
    #     # time.sleep(3)
    #     # print("دقائق الانتظار املأها بالاستغفار....")
    #     # for i in range(3):
    #     #     print("loading.....")
    #     #     time.sleep(2)
    #     indx = random.randrange(movies_nr)
    #     print(f"Your Movie tonight is: ({title[indx]}) from year {year[indx]}\nEnjooooy ;)")
    #     user = input("Do you need more movies?? (y/n)")
    #     if user != "y":
    #         break
    #return print(f"Your Movie tonight is: ({title[indx]}) from year {year[indx]}\nEnjooooy ;)")
    return title[indx], year[indx]
if __name__ == "__main__":
    #main()
    demo = gradio.Interface(fn=main, inputs="text", outputs="text", title="Your Movie Tonight")

    demo.launch(share=False)

