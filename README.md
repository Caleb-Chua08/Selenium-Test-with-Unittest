# Selenium Automated Testing for E-Commerce Website

This project demonstrates automated testing for an e-commerce website using Selenium WebDriver and Python's `unittest` framework. The tests cover various functionalities such as searching for products, adding items to the cart, verifying order details, calculating prices, and filtering products. The tests are designed to ensure the website behaves as expected under different scenarios.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Test Cases](#test-cases)
   - [Search Functionality](#search-functionality)
   - [Adding Items to Cart](#adding-items-to-cart)
   - [Price Calculation](#price-calculation)
   - [Filtering Products](#filtering-products)
5. [Running the Tests](#running-the-tests)
6. [Contributing](#contributing)

---

## Project Overview

This project automates the testing of an e-commerce website using Selenium WebDriver. The tests are written in Python and leverage the `unittest` framework for structured and maintainable test cases. The following functionalities are tested:

- **Search Functionality**: Verifies that the search bar returns the correct products.
- **Adding Items to Cart**: Ensures that items added to the cart are correctly reflected in the order summary.
- **Price Calculation**: Validates that the total price, discounts, and final amounts are calculated correctly.
- **Filtering Products**: Tests the sorting functionality of products in ascending and descending order.

The tests are designed to run in a headless Chrome browser, making them suitable for CI/CD pipelines.

---

## Prerequisites

Before running the tests, ensure you have the following installed:

- **Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
- **Selenium**: Install Selenium using pip:
  ```bash
  pip install selenium
  ```
- **ChromeDriver**: Download the appropriate version of ChromeDriver from [here](https://sites.google.com/chromium.org/driver/) and ensure it is in your system's PATH.

---

## Test Cases

### Search Functionality
- **Description**: Tests the search functionality by entering various product names and verifying that the correct items are displayed.
- **Test Data**: `["Banana", "Apple", "Brocolli", "Pears", "Watermelon"]`
- **Edge Case**: Skips the test for "Watermelon" due to a known spelling issue on the website.

### Adding Items to Cart
- **Description**: Searches for products, adds them to the cart, and verifies that the items in the cart match the items added.
- **Test Data**: Keyword `"be"` is used to search for products.

### Price Calculation
- **Description**: Adds random quantities of products to the cart, calculates the total price, applies a promo code, and verifies the final price after discount.
- **Test Data**: Keyword `"ca"` is used to search for products. Quantities are randomized between 1 and 5.

### Filtering Products
- **Description**: Tests the sorting functionality of products in ascending and descending order.
- **Test Data**: Products are sorted by name.

---

## Running the Tests

To run the tests, execute the following command in the terminal:

```bash
python -m unittest
```

### Running Specific Tests
You can run specific test cases by specifying the test class and method:

```bash
python -m unittest eCommerceTest.TestClassName.test_method_name
```

### Headless Mode
The tests are configured to run in headless mode by default. If you want to run the tests with a visible browser, modify the `setUpClass` method in the `eCommerceTest` class:

```python
chromeOption = webdriver.ChromeOptions()
# chromeOption.add_argument("headless")  # Comment this line to run in non-headless mode
cls.driver = webdriver.Chrome(options=chromeOption)
```

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and submit a pull request.


---

## Acknowledgments

- [Selenium](https://www.selenium.dev/) for providing the tools for browser automation.
- [Rahul Shetty Academy](https://rahulshettyacademy.com/) for the e-commerce website used in this project.

---

For any questions or feedback, feel free to reach out to the project maintainer. Happy testing! 🚀
