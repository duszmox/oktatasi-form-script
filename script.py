from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import json
import random
import sys
import time


survey_url = 'https://szuloikerdoiv34524.unipoll.hu/Survey.aspx?SurveyId=20000148'

def clickOnNext(xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

def randomOfArray(array):
    return array[random.randint(0, len(array) - 1)]
args = sys.argv
answer = ""
if len(args) > 1:
    if args[1].lower() not in ['i', 'n', 'igen', 'nem']:
        answer = input('Saját válaszokkal szeretnéd kitölteni? (i/n) ')
        while answer.lower() not in ['i', 'n', 'igen', 'nem']:
            answer = input('Saját válaszokkal szeretnéd kitölteni? (i/n) ')
    else:
        answer = args[1]
else:
    answer = input('Saját válaszokkal szeretnéd kitölteni? (i/n) ')
    while answer.lower() not in ['i', 'n', 'igen', 'nem']:
        answer = input('Saját válaszokkal szeretnéd kitölteni? (i/n) ')
with open('questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

if answer.lower() in ['i', 'igen']:
    answers = {}
    for question in questions:
        if question == list(questions.keys())[-1]:
            answer = input(question + ": \n")
            while len(answer) > 4000:
                print("Túl hosszú a válasz, maximum 4000 karakter lehet!")
                answer = input(question + ": \n")
            answers[question] = answer
        else:
            print(question)
            i = 1
            for option in questions[question]:
                print(str(i) + ". " + option)
                i += 1
            i -= 1
            answer = input('1-' + str(i) + '-ig válaszd ki a válaszod: ')
            while answer not in [str(x) for x in range(1, i+1)]:
                answer = input('1-' + str(i) + '-ig válaszd ki a válaszod: ')
            answers[question] = questions[question][list(
                questions[question].keys())[int(answer)-1]]

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    while True:
        driver.get(survey_url)
        clickOnNext("//button[@class='mat-ripple mat-tooltip-trigger start-btn']")
        time.sleep(1)
        int = 1
        for question in answers:
            if question == list(questions.keys())[-1]:
                driver.find_element(
                    By.XPATH, "//textarea[@class='answer-input']").send_keys(answers[question])
                clickOnNext("//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']")
            else:
                driver.find_element(
                    By.XPATH, "//label[@for=" + answers[question] + "]").click()
                if int % 2 == 0:
                    clickOnNext("//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']")
                int += 1
        clickOnNext("//button[@class='mat-ripple submit__button ng-tns-c117-0']")
        clickOnNext("//button[@class='mat-ripple dialog__button dialog__button--ok ng-star-inserted']")
        time.sleep(1)


else:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    while True:
        driver.get(survey_url)
        clickOnNext("//button[@class='mat-ripple mat-tooltip-trigger start-btn']")



        random_grade_id = randomOfArray(["20000204", "20000208", "20000212"])
        clickOnNext("//label[@for=" + random_grade_id + "]")

        random_maintainer_id = randomOfArray(["20000231", "20000235", "20000239", "20000243"])
        clickOnNext("//label[@for=" + random_maintainer_id + "]")
        clickOnNext("//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']")

        random_like_id = randomOfArray(["20000268", "20000272", "20000276", "20000280", "20000284"])
        clickOnNext("//label[@for=" + random_like_id + "]")


        random_problematic_id = randomOfArray(["20000303", "20000307",
                                                  "20000311", "20000315", "20000319"])  
        clickOnNext("//label[@for=" + random_problematic_id + "]")

        clickOnNext("//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']")


        random_home_work_id = randomOfArray(["20000344", "20000348",
                                                "20000352", "20000356", "20000360"])
        clickOnNext("//label[@for=" + random_home_work_id + "]")

        random_private_teacher_id = randomOfArray(["20000379", "20000383"])
        clickOnNext("//label[@for=" + random_private_teacher_id + "]")

        clickOnNext("//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']")

        random_improvement_helping_program_id = randomOfArray(["20000408", "20000412", "20000416"])
        clickOnNext("//label[@for=" + random_improvement_helping_program_id + "]")

        random_objectivity_id = randomOfArray(["20000435", "20000439",
                                            "20000443", "20000447", "20000451"])
        clickOnNext("//label[@for=" + random_objectivity_id + "]")

        clickOnNext("//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']")

        random_free_sport_id = randomOfArray(["20000476", "20000480", "20000484"])
        clickOnNext("//label[@for=" + random_free_sport_id + "]")

        random_art_id = randomOfArray(["20000503", "20000507", "20000511"])
        clickOnNext("//label[@for=" + random_art_id + "]")

        clickOnNext("//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']")

        students_involvment_id = "20000536"
        clickOnNext("//label[@for=" + students_involvment_id + "]")

        driver.find_element(
            By.XPATH, "//textarea[@class='answer-input']").send_keys("Nyílt levél Pintér Sándor miniszter Úrhoz! Tisztelt Uram! Nem tudom mikor járt utóljára iskolába, de néhány tanácsot fogadjon el, egy több mint 40 éve tanító tanártól. Azt mondja, hogy tanítani akkor lehet, ha rend van a tanteremben. Alapvetően ez igaz. A kérdés az, Ön mit ért rend alatt? Kérem fogadja el, hogy a rend nem az, hogy bekamerázzuk a tantermeket, a rend nem az, hogy iskola rendőrséget hozunk létre, a rend nem az, hogy nincs választási lehetőségünk, a rend nem az, hogy egyen tankönyvekből tanítuk. Nézzen körül a világban. Javaslom, hogy először Finnországba menjen. A rend az oktatásban az, hogy minden osztályt, minden csoportot a saját képességei szerint oktatunk. Mert bár egyszerűbb lenne, de nincs két egyforma tanuló, osztály, tanulócsoport. Nem lehet uniformizálni. Azt mondja, hogy a tanárokat egy-két pofonnal megregulázza! Ezt különösen sértőnek és felháborítónak tartom. Kikérem magamnak, hogy fenyegessen, hogy megpróbáljon megfélemlíteni minket! Jogunk van kifejezni az elégedetlenségünket, jogunk van a szabad oktatáshoz, jogunk van az emberi méltósághoz, jogunk van a sztrájkhoz! Magának nincs joga minket megfélemlíteni! Magának az a feladata, hogy a feltételeket biztosítsa! Megfelelően felszerelt iskolák, megfelelő tantervek és piacképes fizetés. Megfelelő tanárképzés. A tanárok lejáratásának megszüntetése. Maguk államilag elfogadottan lejáratnak minket. És ez felháborító! Gondolkozzon el azon, hogy hogyan segíthet és ne fenyegetőzzön! Mert úgy tünik már elfelejtette, de tanulni jó! Tisztelettel: Dolgos Eszter okleveles közgazdász tanár, adótanácsadó, IFRS szerinti mérlegképes könyvelő és több mint 40 éve elhivatott tanár")

        clickOnNext("//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']")

        clickOnNext("//button[@class='mat-ripple submit__button ng-tns-c117-0']")
        clickOnNext("//button[@class='mat-ripple dialog__button dialog__button--ok ng-star-inserted']")
        time.sleep(1)
