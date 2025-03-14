import random
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class eCommerceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chromeOption = webdriver.ChromeOptions()
        chromeOption.add_argument("headless")
        cls.driver = webdriver.Chrome(options=chromeOption)
        cls.driver.implicitly_wait(5)
        cls.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


    # def testSearch(self):
    #     testItems = ["Banana","Apple","Brocolli","Pears","Watermelon"]
    #     #Watermelon is spelled wrongly as Water Melon so it will fail
    #     #We will skip it
    #     for item in testItems:
    #         with self.subTest(item):
    #             # Find and enter item into the search bar
    #             self.driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys(item)
    #
    #             # Press on the search button
    #             self.driver.find_element(By.CSS_SELECTOR,".search-button").click()
    #             time.sleep(2)
    #             foundItems = self.driver.find_elements(By.XPATH,"//div[@class='product']")
    #             if item == "Watermelon":
    #                 self.skipTest("Skipping because Watermelon is mispelled as Water Melon ")
    #             self.assertGreater(len(foundItems),0,"Search Error as nothing is found")
    #             self.driver.find_element(By.CSS_SELECTOR, ".search-keyword").clear()

    # # Check the items search and added to cart is same as the item displayed in the order list
    # def testSearchingItems(self, expected_outcomes=None):
    #     keyword = "be"
    #     self.driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys(keyword)
    #     self.driver.find_element(By.CSS_SELECTOR, ".search-button").click()
    #     time.sleep(5)
    #     itemsBeforeSearch = []
    #     foundItems = self.driver.find_elements(By.XPATH, "//div[@class='product']")
    #     for item in foundItems:
    #         itemName = item.find_element(By.TAG_NAME,"h4").text
    #         itemsBeforeSearch.append(itemName)
    #          # Add all the item to the cart
    #         item.find_element(By.XPATH,"//button[text() = 'ADD TO CART']").click()
    #
    #     #Click on the cart
    #     self.driver.find_element(By.CSS_SELECTOR,".cart-icon img").click()
    #
    #     #Click on proceed to checkout
    #     self.driver.find_element(By.XPATH,"//div[@class='action-block']/button").click()
    #     wait = WebDriverWait(self.driver,10)
    #     wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".product-name")))
    #     itemsAfterSearch = []
    #     rows = self.driver.find_elements(By.CSS_SELECTOR,".cartTable tbody tr")
    #     for row in rows:
    #         itemsAfterSearch.append(row.find_element(By.CSS_SELECTOR,".product-name").get_attribute("textContent"))
    #     self.assertEqual(itemsBeforeSearch,itemsAfterSearch,"The order receipt returns not same as those entered in the cart")

    # def testCalculation(self):
    #     keyword = "ca"
    #     self.driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys(keyword)
    #     self.driver.find_element(By.CSS_SELECTOR, ".search-button").click()
    #     time.sleep(5)
    #     foundItems = self.driver.find_elements(By.XPATH, "//div[@class='product']")
    #     # Randomised the quantity
    #     quantityItems = [random.randint(1, 5) for i in range(len(foundItems))]
    #     unitPrices = []
    #     amountPrices = []
    #     for index,item in enumerate(foundItems):
    #         incrementBtn = item.find_element(By.CSS_SELECTOR,".increment")
    #         for i in range(quantityItems[index]-1):
    #             incrementBtn.click()
    #
    #         unitPrice = item.find_element(By.CSS_SELECTOR,".product-price").get_attribute("textContent")
    #         unitPrices.append(int(unitPrice))
    #
    #         # Add all the item to the cart
    #         item.find_element(By.XPATH,".//button[text() = 'ADD TO CART']").click()
    #
    #     # Click on the cart
    #     self.driver.find_element(By.CSS_SELECTOR,".cart-icon img").click()
    #
    #     #Click on proceed to checkout
    #     self.driver.find_element(By.XPATH,"//div[@class='action-block']/button").click()
    #     wait = WebDriverWait(self.driver,10)
    #     wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".cartTable tbody tr")))
    #
    #     quantityAfterAdd = []
    #     unitPriceAfterAdd = []
    #     totalPriceAfterAdd = []
    #
    #     rows = self.driver.find_elements(By.CSS_SELECTOR,".cartTable tbody tr")
    #     for row in rows:
    #         quantityAfterAdd.append(int(row.find_element(By.CSS_SELECTOR,".quantity").get_attribute("textContent")))
    #         unitPriceAfterAdd.append(int(row.find_element(By.CSS_SELECTOR,"td:nth-child(4) p").get_attribute("textContent")))
    #         totalPriceAfterAdd.append(int(row.find_element(By.CSS_SELECTOR, "td:nth-child(5) p").get_attribute("textContent")))
    #     self.assertEqual(quantityItems,quantityAfterAdd,"The quantity added to cart is not the same as the order receipt")
    #     self.assertEqual(unitPrices,unitPriceAfterAdd,"The unit prices of item added to cart is not the same as in the order receipt")
    #     # Check whether the calculation of amount is correct or not
    #     for i in range(len(totalPriceAfterAdd)):
    #         self.assertEqual(quantityAfterAdd[i]*unitPriceAfterAdd[i],totalPriceAfterAdd[i],"Calculation of amount is not correct based on unit price and quantity")
    #
    #     totalPrice = 0
    #     for price in totalPriceAfterAdd:
    #         totalPrice+=price
    #
    #     #Apply promo code
    #     promoCode = "rahulshettyacademy"
    #     self.driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys(promoCode)
    #     self.driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
    #     promoWait = WebDriverWait(self.driver,10)
    #     promoWait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
    #
    #     # Check website calculated total with actual total before and after discount
    #     totalPriceBeforeDiscount =int(self.driver.find_element(By.CSS_SELECTOR,".totAmt").get_attribute("textContent"))
    #     discountPercentage = int(self.driver.find_element(By.CSS_SELECTOR,".discountPerc").get_attribute("textContent")[:-1])
    #     totalPriceAfterDiscount = round(float(self.driver.find_element(By.CSS_SELECTOR,".discountAmt").get_attribute("textContent")),2)
    #
    #     calculatedPriceAfterDiscount = round((((100 - discountPercentage) / 100) * totalPrice),2)
    #     self.assertEqual(totalPriceBeforeDiscount,totalPrice)
    #     self.assertEqual(totalPriceAfterDiscount,calculatedPriceAfterDiscount)

    # Test Filer in Ascending and Descending Manner
    def testFilter(self):
        #Click on the top deals
        self.driver.find_element(By.XPATH,"//a[text()='Top Deals']").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.driver.find_element(By.XPATH,"//span[text() = 'Veg/fruit name']").click()

        # Find the list of item names
        nameList = []
        names = self.driver.find_elements(By.CSS_SELECTOR,"tbody tr")
        for name in names:
            nameList.append(name.find_element(By.CSS_SELECTOR,"td:first-child").get_attribute("textContent"))

        if len(self.driver.find_elements(By.CSS_SELECTOR,".sort-ascending")) != 0:
            for i in range(len(nameList)-1):
                name = nameList[i]
                self.assertGreater(nameList[i+1],name)
        else:
            for i in range(len(nameList)-1):
                name = nameList[i]
                self.assertLess(nameList[i+1],name)

        # Try to filter again
        self.driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()

        # Find the list of item names
        nameList = []
        names = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        for name in names:
            nameList.append(name.find_element(By.CSS_SELECTOR, "td:first-child").get_attribute("textContent"))

        if len(self.driver.find_elements(By.CSS_SELECTOR, ".sort-ascending")) != 0:
            for i in range(len(nameList) - 1):
                name = nameList[i]
                self.assertGreater(nameList[i + 1], name)
        else:
            for i in range(len(nameList) - 1):
                name = nameList[i]
                self.assertLess(nameList[i + 1], name)





if __name__ == '__main__':
    unittest.main()
