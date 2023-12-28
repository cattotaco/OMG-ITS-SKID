import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup
import random
from colorama import Fore, Style, init

init(autoreset=True)
def display_menu():
    menu = f"""
                                                                            
                                                                          
                                                                          
                                                                          
                                                                          
                                                                          
                                                       ___                
                                                     /'___)               
             ____    _     ___     __    ___    _ _ | (__   __            
            (_  ,) /'_`\ /' _ `\ /'__`\/',__) /'_` )| ,__)/'__`\          
             /'/_ ( (_) )| ( ) |(  ___/\__, \( (_| || |  (  ___/          
            (____)`\___/'(_) (_)`\____)(____/`\__,_)(_)  `\____)          
                                                                          
                                                                          
       _             _      _             _           _         _         
      ( )     _     ( )    ( )           ( )         ( )     _ ( )_       
  ___ | |/') (_)   _| |   _| |   __     _| |     ___ | |__  (_)| ,_)      
/',__)| , <  | | /'_` | /'_` | /'__`\ /'_` |   /',__)|  _ `\| || |        
\__, \| |\`\ | |( (_| |( (_| |(  ___/( (_| |   \__, \| | | || || |_       
(____/(_) (_)(_)`\__,_)`\__,_)`\____)`\__,_)   (____/(_) (_)(_)`\__)      
                                                                          
                                                                          
                     _                                                    
                    ( )                                                   
   __     _ _  _ __ | |_      _ _    __     __                            
 /'_ `\ /'_` )( '__)| '_`\  /'_` ) /'_ `\ /'__`\                          
( (_) |( (_| || |   | |_) )( (_| |( (_) |(  ___/                          
`\__  |`\__,_)(_)   (_,__/'`\__,_)`\__  |`\____)                          
( )_) |                           ( )_) |                                 
 \___/'                            \___/'                                 
                                                                          
                                                                          
 _   _   ___    __   _ __   ___     _ _   ___ ___     __                  
( ) ( )/',__) /'__`\( '__)/' _ `\ /'_` )/' _ ` _ `\ /'__`\                
| (_) |\__, \(  ___/| |   | ( ) |( (_| || ( ) ( ) |(  ___/                
`\___/'(____/`\____)(_)   (_) (_)`\__,_)(_) (_) (_)`\____)                
                                                                          
                                                                          
                    _      _                                              
                   ( )    ( )                                             
   __   _ __   _ _ | |_   | |_      __   _ __                             
 /'_ `\( '__)/'_` )| '_`\ | '_`\  /'__`\( '__)                            
( (_) || |  ( (_| || |_) )| |_) )(  ___/| |                               
`\__  |(_)  `\__,_)(_,__/'(_,__/'`\____)(_)                               
( )_) |                                                                   
 \___/'                                                                   
    """

    print(menu)

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def process_profile(session, random_profile_id):
    url = f'https://steamcommunity.com/profiles/{random_profile_id}'
    html = await fetch(session, url)

    soup = BeautifulSoup(html, 'html.parser')
    persona_name_div = soup.find('div', {'class': 'persona_name'})

    if persona_name_div:
        persona_name = persona_name_div.find('span', {'class': 'actual_persona_name'}).text
        print(f"Captured: {Fore.CYAN}{persona_name}{Style.RESET_ALL} | {Fore.GREEN}{random_profile_id}{Style.RESET_ALL}")

        with open('usernames.txt', 'a', encoding='utf-8') as file:
            file.write(f"{persona_name} | {random_profile_id}\n")

async def main():
    display_menu()

    async with aiohttp.ClientSession() as session:
        while True:
            tasks = []
            for _ in range(200):  # Adjust the number of parallel requests as needed
                random_profile_id = random.randint(76561199000000000, 76561199509572887)
                task = process_profile(session, random_profile_id)
                tasks.append(task)

            await asyncio.gather(*tasks)
            await asyncio.sleep(1)  # Adjust the sleep duration between iterations as needed

if __name__ == "__main__":
    asyncio.run(main())

