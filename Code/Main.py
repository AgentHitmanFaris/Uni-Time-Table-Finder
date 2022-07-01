#update 01/7/22
from bs4 import BeautifulSoup
import requests
from requests import exceptions

def main():
    link = ('http://bpa.ums.edu.my/kuliah/finder.html')
    i = 1
    source = requests.get(link)
    source.raise_for_status()
    print("Sucessfully connected to " + link)
    print(source)
    soup = BeautifulSoup(source.text,'html.parser')
    lines = soup.find_all('resource',dept="0" ,faculty="0",)
    print("Search result for " + link)
    print(len(lines))
    #print(soup)
    gety = 40
    print("Sucessfully execute the program") 
    print("Total search results: ", len(lines))
    for ini in lines:
        aa="initial id="
        init = aa + gety
        a=soup.find_all('init')
        print(init)
        gety += 1    

while True:
    try:
        main()
        if input("\nRepeat the program? (Y/N): ").strip().upper() != 'Y':
           break;

    except Exception as e:
        print("Error connecting to the link")
        if input("\nRepeat the program? (Y/N): ").strip().upper() != 'Y':
            break;
    

