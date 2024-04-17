import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def drive_task():
    
    options = Options()
    options.add_argument("user-data-dir=C:/Users/Administrator/Desktop/svuotacestino")  # salvo tutti i dati di login in una cartella (sessioni ecc)
    driver = webdriver.Chrome(options=options)   
    driver.get("https://drive.google.com/drive/trash/0ANlRpiiozeorUk9PVA")  # Apre il cestino di Google Drive sosatituire se cambia (TODO:da fare in automatico)

    
    input("Scrivi ok quando è tutto a posto (login fatto e nella pagina giusta del cestino): ")

    while True:
        try:
            empty_trash_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".VfPpkd-vQzf8d")) # Trova il pulsante "Svuota cestino"
            )
            empty_trash_button.click()
            time.sleep(5)
            
            confirm_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".VfPpkd-d-Qu-k8QpJ > .VfPpkd-vQzf8d")) # Trova il pulsante "elimina definitivamente"
            )
            confirm_button.click()

            time.sleep(30)
            driver.refresh() #aggiorno la pagina perchè google elimina solo 256 elementi alla volta. se ce ne sono 50000 devo rifarlo 195 volte manualmente (impossibile)
        except Exception as e:
            print("Il cestino è vuoto, attendo 1 ora")
            time.sleep(3600)

if __name__ == "__main__":
    drive_task()

