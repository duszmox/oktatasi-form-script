from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import sys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


survey_url = 'https://szuloikerdoiv34524.unipoll.hu/Survey.aspx?SurveyId=20000148'

# get arguments from command line
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
questions = {
    "Kérjük, jelölje meg, mely évfolyamon tanul a gyermeke.": {
        "1-4 évfolyamon": "20000204",
        "5-8 évfolyamon": "20000208",
        "9-12 évfolyamon": "20000212",
    },
    "Kérjük, válassza ki gyermeke iskolája fenntartójának típusát!": {
        "tankerületi központ": "20000231",
        "egyházi jogi személy": "20000235",
        "felsőoktatási intézmény": "20000239",
        "egyéb": "20000243",
    },
    "Szeret-e iskolába járni gyermeke? (1-5-ig terjedő skálán)": {
        "1": "20000268",
        "2": "20000272",
        "3": "20000276",
        "4": "20000280",
        "5": "20000284",
    },
    "Van-e gyermeke osztályában olyan tanuló, aki magatartásával zavarja az osztálytársait, vagy egyéb, súlyos magatartási problémái vannak?": {
        "Nincs": "20000303",
        "1-2": "20000307",
        "2-4": "20000311",
        "5 vagy annál több": "20000315",
        "nem tudom": "20000319",
    },
    "Kérjük, jelölje, gyermeke átlagosan mennyi időt tölt a házi feladat elkészítésével naponta?": {
        "nincs házi feladat": "20000344",
        "kevesebb, mint egy órát": "20000348",
        "1-2 óra között időt": "20000352",
        "2-3 óra közötti időt": "20000356",
        "3 óránál többet": "20000360",
    },
    "Jár-e magántanárhoz valamilyen tárgyból a gyermeke annak érdekében, hogy az iskolai követelményeket megfelelően tudja teljesíteni?": {
        "igen": "20000379",
        "nem": "20000383",
    },
    "Gyermeke iskolájában szerveznek-e kellő számú, a tanulók fejlődését segítő tanórán kívüli programot?": {
        "igen": "20000408",
        "nem": "20000412",
        "nem tudom": "20000416",
    },
    "Ön szerint gyermekének iskolai teljesítményét mennyire objektíven, azaz a teljesítményének és a képességeinek megfelelően mérik a pedagógusok? (1-5-ig terjedő skálán)": {
        "1": "20000435",
        "2": "20000439",
        "3": "20000443",
        "4": "20000447",
        "5": "20000451",
    },
    "Kérjük, jelölje, hogy van-e lehetőség gyermeke iskolájában tanórán kívüli, ingyenes sportolásra (szakkör, diáksport, tömegsport vagy egyéb program keretében) délutánonként?": {
        "igen": "20000476",
        "nem": "20000480",
        "nem tudom": "20000484",
    },
    "Kérjük, jelölje, hogy van-e lehetőség gyermeke iskolájában tanórán kívüli, ingyenes művészeti képzésre(szakkör vagy egyéb foglalkozások keretében) délutánonként?": {
        "igen": "20000503",
        "nem": "20000507",
        "nem tudom": "20000511",
    },
    "Kérjük, jelölje, hogy egyetért-e Ön azzal, hogy a pedagógusok a tanulókat is bevonják a bérezésükkel kapcsolatos demonstrációkba?": {
        "igen": "20000536",
        "nem": "20000540",
        "nem tudom": "20000544",
    },
    "Amennyiben további javaslata, véleménye lenne, kérjük, azt itt fogalmazza meg röviden! (Max. 4000 karakter)": "//textarea[@class='answer-input']"
}

if answer.lower() in ['i', 'igen']:
    # ask every question and makethem choose by entering the corresponding numbers
    answers = {}
    for question in questions:
        # get last question
        if question == list(questions.keys())[-1]:
            # if it's the last question, ask for the answer
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
            # check if answer is in range
            while answer not in [str(x) for x in range(1, i+1)]:
                answer = input('1-' + str(i) + '-ig válaszd ki a válaszod: ')
            answers[question] = questions[question][list(
                questions[question].keys())[int(answer)-1]]

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    while True:
        driver.get(survey_url)
        time.sleep(1)
        driver.find_element(
            By.XPATH, "// button[@class='mat-ripple mat-tooltip-trigger start-btn']").click()
        time.sleep(1)
        int = 1
        for question in answers:
            if question == list(questions.keys())[-1]:
                driver.find_element(
                    By.XPATH, "//textarea[@class='answer-input']").send_keys(answers[question])
                time.sleep(1)
                driver.find_element(
                    By.XPATH, "//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']").click()
            else:
                driver.find_element(
                    By.XPATH, "//label[@for=" + answers[question] + "]").click()
                if int % 2 == 0:
                    time.sleep(1)
                    driver.find_element(
                        By.XPATH, "//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']").click()
                int += 1

        driver.find_element(
            By.XPATH, "//button[@class='mat-ripple submit__button ng-tns-c117-0']").click()
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//button[@class='mat-ripple dialog__button dialog__button--ok ng-star-inserted']").click()
        time.sleep(1)


else:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    while True:
        driver.get(survey_url)
        time.sleep(1)
        driver.find_element(
            By.XPATH, "// button[@class='mat-ripple mat-tooltip-trigger start-btn']").click()
        time.sleep(1)

        grade_ids = ["20000204", "20000208", "20000212"]
        random_grade_id = random.choice(grade_ids)
        driver.find_element(
            By.XPATH, "//label[@for=" + random_grade_id + "]").click()

        maintainer_ids = ["20000231", "20000235", "20000239", "20000243"]
        random_maintainer_id = random.choice(maintainer_ids)
        driver.find_element(
            By.XPATH, "//label[@for=" + random_maintainer_id + "]").click()
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']").click()

        like_ids = ["20000268", "20000272", "20000276", "20000280", "20000284"]
        random_like_id = random.choice(like_ids)
        driver.find_element(
            By.XPATH, "//label[@for=" + random_like_id + "]").click()

        problematic_ids = ["20000303", "20000307",
                           "20000311", "20000315", "20000319"]
        random_problematic_id = random.choice(problematic_ids)
        driver.find_element(
            By.XPATH, "//label[@for=" + random_problematic_id + "]").click()

        time.sleep(1)
        driver.find_element(
            By.XPATH, "//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']").click()

        home_work_ids = ["20000344", "20000348",
                         "20000352", "20000356", "20000360"]
        random_home_work_id = random.choice(home_work_ids)
        driver.find_element(
            By.XPATH, "//label[@for=" + random_home_work_id + "]").click()

        private_teacher_ids = ["20000379", "20000383"]
        random_private_teacher_id = random.choice(private_teacher_ids)
        driver.find_element(
            By.XPATH, "//label[@for=" + random_private_teacher_id + "]").click()

        time.sleep(1)
        driver.find_element(
            By.XPATH, "//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']").click()

        improvement_helping_program_ids = ["20000408", "20000412", "20000416"]
        random_improvement_helping_program_id = random.choice(
            improvement_helping_program_ids)
        driver.find_element(
            By.XPATH, "//label[@for=" + random_improvement_helping_program_id + "]").click()

        objectivity_ids = ["20000435", "20000439",
                           "20000443", "20000447", "20000451"]
        random_objectivity_id = random.choice(objectivity_ids)
        driver.find_element(
            By.XPATH, "//label[@for=" + random_objectivity_id + "]").click()

        time.sleep(1)
        driver.find_element(
            By.XPATH, "//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']").click()

        free_sport_ids = ["20000476", "20000480", "20000484"]
        random_free_sport_id = random.choice(free_sport_ids)
        driver.find_element(
            By.XPATH, "//label[@for=" + random_free_sport_id + "]").click()

        art_ids = ["20000503", "20000507", "20000511"]
        random_art_id = random.choice(art_ids)
        driver.find_element(
            By.XPATH, "//label[@for=" + random_art_id + "]").click()

        time.sleep(1)
        driver.find_element(
            By.XPATH, "//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']").click()

        students_involvment_id = "20000536"
        driver.find_element(
            By.XPATH, "//label[@for=" + students_involvment_id + "]").click()

        driver.find_element(
            By.XPATH, "//textarea[@class='answer-input']").send_keys("Nyílt levél Pintér Sándor miniszter Úrhoz! Tisztelt Uram! Nem tudom mikor járt utóljára iskolába, de néhány tanácsot fogadjon el, egy több mint 40 éve tanító tanártól. Azt mondja, hogy tanítani akkor lehet, ha rend van a tanteremben. Alapvetően ez igaz. A kérdés az, Ön mit ért rend alatt? Kérem fogadja el, hogy a rend nem az, hogy bekamerázzuk a tantermeket, a rend nem az, hogy iskola rendőrséget hozunk létre, a rend nem az, hogy nincs választási lehetőségünk, a rend nem az, hogy egyen tankönyvekből tanítuk. Nézzen körül a világban. Javaslom, hogy először Finnországba menjen. A rend az oktatásban az, hogy minden osztályt, minden csoportot a saját képességei szerint oktatunk. Mert bár egyszerűbb lenne, de nincs két egyforma tanuló, osztály, tanulócsoport. Nem lehet uniformizálni. Azt mondja, hogy a tanárokat egy-két pofonnal megregulázza! Ezt különösen sértőnek és felháborítónak tartom. Kikérem magamnak, hogy fenyegessen, hogy megpróbáljon megfélemlíteni minket! Jogunk van kifejezni az elégedetlenségünket, jogunk van a szabad oktatáshoz, jogunk van az emberi méltósághoz, jogunk van a sztrájkhoz! Magának nincs joga minket megfélemlíteni! Magának az a feladata, hogy a feltételeket biztosítsa! Megfelelően felszerelt iskolák, megfelelő tantervek és piacképes fizetés. Megfelelő tanárképzés. A tanárok lejáratásának megszüntetése. Maguk államilag elfogadottan lejáratnak minket. És ez felháborító! Gondolkozzon el azon, hogy hogyan segíthet és ne fenyegetőzzön! Mert úgy tünik már elfelejtette, de tanulni jó! Tisztelettel: Dolgos Eszter okleveles közgazdász tanár, adótanácsadó, IFRS szerinti mérlegképes könyvelő és több mint 40 éve elhivatott tanár")

        time.sleep(1)
        driver.find_element(
            By.XPATH, "//button[@class='mat-ripple mat-tooltip-trigger paginator__btn']").click()

        driver.find_element(
            By.XPATH, "//button[@class='mat-ripple submit__button ng-tns-c117-0']").click()
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//button[@class='mat-ripple dialog__button dialog__button--ok ng-star-inserted']").click()
        time.sleep(1)
