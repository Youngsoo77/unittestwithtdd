from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('TDD', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Hello', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )
        # 공작 깃털 사기 라고 텍스트 상자에 입력한다.
        inputbox.send_keys('공작 깃털 사기')

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에 추가된다.
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작 깃털 사기' for row in rows),
        )
        self.fail('Finish the Test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
