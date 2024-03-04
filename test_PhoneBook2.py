from unittest import TestCase

import PhoneBook2


class Test(TestCase):
    def test_search_contacts(self):
      list1 =  PhoneBook2.Contact("solomon", "08164556912","ayomidebanjo02@gmail.com","7 adebare street")
      self.assertEqual(PhoneBook2.search_contacts(list1,'solomon'),['solomon'])
