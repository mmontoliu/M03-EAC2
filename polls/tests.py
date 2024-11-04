from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User

class MySeleniumTests(StaticLiveServerTestCase):
    # no crearem una BD de test en aquesta ocasió (comentem la línia)
    #fixtures = ['testdb.json',]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)
        # creem superusuari
        user = User.objects.create_user("isard", "isard@isardvdi.com", "pirineus")
        user.is_superuser = True
        user.is_staff = True
        user.save()
 
    @classmethod
    def tearDownClass(cls):
        # tanquem browser
        # comentar la propera línia si volem veure el resultat de l'execució al navegador
        cls.selenium.quit()
        super().tearDownClass()

    def test_crear_usuari(self):
        # anem a la pàgina INICIAL del admin panel i ho comprovem
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
        self.assertEqual( self.selenium.title , "Log in | Django site admin" )
 
        # introduïm dades de login (isard) i cliquem el botó "Log in" per entrar
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('isard')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('pirineus')
        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()
    
        # Anem a la pàgina Add-Question i ho comprovem
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/polls/question/add/'))
        self.assertEqual( self.selenium.title , "Add question | Django site admin" )

        # Creem la Pregunta1 i cliquem el botó "Save and add another" per guardar-la i fer la següent
        question_text_input = self.selenium.find_element(By.NAME,"question_text")
        question_text_input .send_keys('Pregunta1')
        pub_date_input = self.selenium.find_element(By.NAME, 'pub_date_0')
        pub_date_input.send_keys('2024-10-31')
        pub_date_input = self.selenium.find_element(By.NAME, 'pub_date_1')
        pub_date_input.send_keys('21:18:33')
        save_button = self.selenium.find_element(By.NAME, "_addanother")
        save_button.click()

        # Comprobem que la pregunta s'ha creat correctament:
        self.assertIn(' was added successfully. You may add another question below.', self.selenium.page_source)

        # Creem la Pregunta2 i cliquem el botó "Save" per guardar-la
        question_text_input = self.selenium.find_element(By.NAME,"question_text")
        question_text_input .send_keys('Pregunta2')
        pub_date_input = self.selenium.find_element(By.NAME, 'pub_date_0')
        pub_date_input.send_keys('2024-10-31')
        pub_date_input = self.selenium.find_element(By.NAME, 'pub_date_1')
        pub_date_input.send_keys('21:20:33')
        save_button = self.selenium.find_element(By.NAME, "_save")
        save_button.click()

        # Comprobem que la pregunta s'ha creat correctament:
        self.assertIn(' was added successfully.', self.selenium.page_source)

        # Anem a la pàgina Add-Choice i ho comprovem
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/polls/choice/add/'))
        #self.assertEqual( self.selenium.title , "Add choice | Django site admin" )

        # Creem la Choice1 per la Pregunta1 i cliquem el botó "Save and add another" per guardar-la i fer la següent
        question_dropdown = self.selenium.find_element(By.NAME, 'question')
        question_dropdown.send_keys('Pregunta1')
        choice_text_field = self.selenium.find_element(By.NAME, 'choice_text')
        choice_text_field.send_keys('Choice1 per Pregunta1')
        save_button = self.selenium.find_element(By.NAME, "_addanother")
        save_button.click()

        # Comprobem que la Choice s'ha creat correctament:
        self.assertIn(' was added successfully. You may add another choice below.', self.selenium.page_source)

        # Creem la Choice2 per la Pregunta1 i cliquem el botó "Save and add another" per guardar-la i fer la següent
        question_dropdown = self.selenium.find_element(By.NAME, 'question')
        question_dropdown.send_keys('Pregunta1')
        choice_text_field = self.selenium.find_element(By.NAME, 'choice_text')
        choice_text_field.send_keys('Choice2 per Pregunta1')
        save_button = self.selenium.find_element(By.NAME, "_addanother")
        save_button.click()

        # Comprobem que la Choice s'ha creat correctament:
        self.assertIn(' was added successfully. You may add another choice below.', self.selenium.page_source)

        # Creem la Choice1 per la Pregunta2 i cliquem el botó "Save and add another" per guardar-la i fer la següent
        question_dropdown = self.selenium.find_element(By.NAME, 'question')
        question_dropdown.send_keys('Pregunta2')
        choice_text_field = self.selenium.find_element(By.NAME, 'choice_text')
        choice_text_field.send_keys('Choice1 per Pregunta2')
        save_button = self.selenium.find_element(By.NAME, "_addanother")
        save_button.click()

        # Comprobem que la Choice s'ha creat correctament:
        self.assertIn(' was added successfully. You may add another choice below.', self.selenium.page_source)

        # Creem la Choice2 per la Pregunta2 i cliquem el botó "Save" per guardar-la
        question_dropdown = self.selenium.find_element(By.NAME, 'question')
        question_dropdown.send_keys('Pregunta2')
        choice_text_field = self.selenium.find_element(By.NAME, 'choice_text')
        choice_text_field.send_keys('Choice2 per Pregunta2')
        save_button = self.selenium.find_element(By.NAME, "_save")
        save_button.click()

        # Comprobem que la Choice s'ha creat correctament:
        self.assertIn(' was added successfully.', self.selenium.page_source)
        
        # anem a la pàgina ADD-USER i ho comprovem
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/auth/user/add/'))
        self.assertEqual( self.selenium.title , "Add user | Django site admin" )

        # Creem usuari pagafantas i cliquem el botó "Save and continue editing" per guardar-lo
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('pagafantas')
        password_input = self.selenium.find_element(By.NAME,"password1")
        password_input.send_keys('manel.com')
        password_input = self.selenium.find_element(By.NAME,"password2")
        password_input.send_keys('manel.com')
        save_button = self.selenium.find_element(By.NAME, "_continue")
        save_button.click()

        # Comprobem que el usuari s'ha creat correctament:
        self.assertIn(' was added successfully. You may edit it again below.', self.selenium.page_source)

        # Li assignem permisos de "staff" al pagafantas i guardem canvis
        staff_status_checkbox = self.selenium.find_element(By.NAME, 'is_staff')
        staff_status_checkbox.click()
        save_button = self.selenium.find_element(By.NAME, "_continue")
        save_button.click()

        # Comprobem que el canvi s'ha fet correctament:
        self.assertIn(' was changed successfully. You may edit it again below.', self.selenium.page_source)

        # Li assignem permisos de lectura choice | question:
        read_permission = self.selenium.find_element(By.XPATH, "//option[contains(text(), 'Can view choice')]")
        read_permission.click()
        read_permission = self.selenium.find_element(By.XPATH, "//option[contains(text(), 'Can view question')]")
        read_permission.click()
        # Faig click per afegir els permisos seleccionats:
        permissions_input = self.selenium.find_element(By.ID, 'id_user_permissions_add_link')
        permissions_input.click()
        # Guardo els canvis del usuari:
        save_button = self.selenium.find_element(By.NAME, "_save")
        save_button.click()

        # Comprobem que el canvi s'ha fet correctament:
        self.assertIn(' was changed successfully.', self.selenium.page_source)

        # Miro la fitxa general del pagafantas
        #self.selenium.get('%s%s' % (self.live_server_url, '/admin/auth/user/'))
        #pagafantas_link = self.selenium.find_element(By.LINK_TEXT, 'pagafantas')
        #pagafantas_link.click()

        # Tanquem la sessió del super-usuari isard i ho comprovem
        logout_button = self.selenium.find_element(By.XPATH, '//button[text()="Log out"]')
        logout_button.click()
        self.assertEqual( self.selenium.title , "Logged out | Django site admin" )


        # Anem a la pàgina INICIAL del admin panel i ho comprovem
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
        self.assertEqual( self.selenium.title , "Log in | Django site admin" )

        # introduïm dades de login (pagafantas) i cliquem el botó "Log in" per entrar
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('pagafantas')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('manel.com')
        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()

        # Anem a la pàgina Question i ho comprovem
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/polls/question/'))
        self.assertEqual( self.selenium.title , "Select question to view | Django site admin" )

        # Comprovo que l'usuari pot veure les preguntes però no editar-les
        questions = self.selenium.find_elements(By.LINK_TEXT, "Pregunta1")
        self.assertTrue(questions)  # Assegurar que hi ha preguntes visibles

        # Accedeixo a la pregunta1 (per exemple)
        question_link = self.selenium.find_element(By.LINK_TEXT, "Pregunta1")
        question_link.click()

        # Comprovo que l'usuari no té permisos d'edició
        with self.assertRaises(Exception):
            self.selenium.find_element(By.NAME, "_save")  # Aquest botó no hauria d'estar present per usuaris només de lectura
