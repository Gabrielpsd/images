import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#https://yandex.com
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}

def createsURL(terms:str)-> str:
    return f"https://www.google.com/search?q={terms}&udm=2"
    #return f"https://yandex.com/images/search?text={terms}&itype=jpeg"

def gettinDataFromBrowser(url: str):  
    
    #Navigate to Google Images
    driver.get(url=url)
    
    
    # Going into search bar and input the search query
    """ search_box = driver.find_element(By.NAME,"q")
    search_box.send_keys(terms)
    search_box.submit()
     """
    #setting a waiting to the submit
    driver.implicitly_wait(10)
    
    # Find all <a> elements with href containing "/imgres" - images result links
    #links = driver.find_elements(By.XPATH, "//a[contains(@href,'imgres')]")
    
    #print(driver.page_source)
    
    #print the links
    """  for link in links:
        print(link.get_attribute('href')) """
        
    html = driver.page_source
        
    print(html)
    
    driver.quit()
    
    return html
    
def inputData()-> str:
    """ this function gets the terms to be searched and formates to the "q" google url parameter

    Returns:
        str: search term to be used in "q" parameter
    """
    terms = input("Digite o(s) termo(s) a ser buscado:").split(' ')
    
    terms = [term for term in terms if term != '']

    #print(terms) depuration
    
    SearchString = '+'.join(str(term) for term in terms)
    
    #print(SearchString) depuration  
    return SearchString


def treatingContent(HTMLContent: bytes):
    content = BeautifulSoup(HTMLContent,"html.parser")

    print(content)
    
    for result in content.find_all("div",attrs={"class":"ContentImage"}):
        link = result.descendants
        
        print(link)
        
        for a in link:
            print(a)
            
        print(result)
    
def main() -> None:
    """main function
    """
    
    term:str 
    
    term = inputData()
    url = createsURL(terms=term)
    gettinDataFromBrowser(url=url)
    
if __name__ == "__main__":
    main()