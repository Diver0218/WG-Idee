from django.test import TestCase, Client
from django.urls import reverse
from WGIdeeApp.models import Person, Ausgabe
from django.contrib.auth.models import User
from WGIdeeApp.calculations import *
from WGIdeeApp.views import persons

class Create_User(TestCase):
    # Testet ob ein User erstellt werden kann
    def setUp(self):
        
        # Erstellt einen Client mit Testuser
        
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.person = Person.objects.create(zugew_user=self.user)

    def test_landing_page_status_code(self):
        
        # Testet ob die Landing Page mit dem Testuser erreichbar ist
        
         self.client.login(username='testuser', password='12345')
         response = self.client.get(reverse('landing_page'))
         self.assertEqual(response.status_code, 200)

    def test_error(self):
        
        # Testet ob die Landing Page ohne Login nicht erreichbar ist
        
        self.client.login(username='testuser', password='123456')
        response = self.client.get(reverse('landing_page'))
        self.assertNotEqual(response.status_code, 200)
        
class Create_Ausgabe(TestCase):
    
    # Testet ob eine Ausgabe erstellt werden kann
    
    def setUp(self):
        
        # Erstellt einen Client mit Testuser zugehöriger Testausgabe
        
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.person = Person.objects.create(zugew_user=self.user)
        self.ausgabe = Ausgabe.objects.create(beschreibung='Test Ausgabe', preis=50.00, person=self.person)

    def test_ausgabe_page_status_code(self):
        
        # Testet ob die Ausgaben Seite mit dem Testuser erreichbar ist
        
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('outgoings'))
        self.assertEqual(response.status_code, 200)

    def test_Ausgabe_in_database(self):
        
        # Testet ob die Testausgabe in der Datenbank mit richtigen Werten vorhanden ist
        
        self.client.login(username='testuser', password='12345')
        ausgabe = Ausgabe.objects.get(beschreibung='Test Ausgabe')
        self.assertEqual(ausgabe.preis, 50.00)
        self.assertEqual(ausgabe.person, self.person)
        self.assertEqual(ausgabe.beschreibung, 'Test Ausgabe')

    def test_Anzahl_Ausgaben(self):
        
        # Testet ob die Anzahl der Ausgaben in der Datenbank stimmt
        
        self.client.login(username='testuser', password='12345')
        ausgabe = Ausgabe.objects.all()
        self.assertEqual(len(ausgabe), 1)

class depts(TestCase):
    
    # Testet ob die Berechnung der Schulden funktioniert
    
    def setUp(self):
        
        # Erstellt einen Client mit zwei Testusern und Testausgaben
        
        self.client = Client()
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.person1 = Person.objects.create(zugew_user=self.user1)
        self.person2 = Person.objects.create(zugew_user=self.user2)
        self.ausgabe1 = Ausgabe.objects.create(beschreibung='Test Ausgabe1', preis=50.00, person=self.person1)
        self.ausgabe2 = Ausgabe.objects.create(beschreibung='Test Ausgabe2', preis=60.00, person=self.person2)

    def test_debts(self):
        
        # Testet ob die Schulden der Testuser in der Datenbank richtig berechnet werden
        
        self.client.login(username='testuser1', password='12345')
        ausgeben_list = Ausgabe.objects.all()
        person_list = Person.objects.all()
        comp_list = compensation(ausgeben_list, person_list)
        comp_item = comp_list[0]
        self.assertEqual(comp_item['sender'], self.person1)
        self.assertEqual(comp_item['receiver'], self.person2)
        self.assertEqual(comp_item['amount'], 5.00)
        self.assertEqual(len(comp_list), 1)
