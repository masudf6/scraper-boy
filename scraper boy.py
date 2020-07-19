from bs4 import BeautifulSoup
import requests
import csv
import time

# Open a CSV file, set the mode to 'a' (for append)
csv_file = open('goru_scrape.csv', 'a', encoding='utf-8', newline='')

# Write the CSV file
csv_writer = csv.writer(csv_file)
# Create the first row which is going to be the title row
csv_writer.writerow(['Code', 'Price', 'Age', 'Teeth', 'Height', 'Length', 'Weight', 'Color', 'Category', 'Subcategory','Orgin'])

# I split the url into 2 parts because the cow code is in the middle of the original url
url1 = 'https://goruchai.com/front/1548'
url2= '-details-cow-information'

# Iterate for the cow code
# There are more that 650 items, I just scraped through 58 items
for i in range(42, 100):
    # String the url together
    urls = url1 + str(i) + url2

    source = requests.get(urls).text   # Getting the source code from website
    soup = BeautifulSoup(source, 'lxml')

    # Set the url1 and url2 to initial state
    url1 = 'https://goruchai.com/front/1548'
    url2= '-details-cow-information'


    # print(soup.prettify())

    # find the tag needed to be parsed
    goru = soup.find('table', class_='table table-bordered')
    codePath = soup.find('div', class_='sec-heading-area')
    pricePath = soup.find('div', class_='pr-wt-area')
    # print(goru.prettify())

    # Set the variables
    goru_code = codePath.h3.text[10:16]    # Slicing the returned string to need
    goru_price = pricePath.h5.text

    goru_age = goru.find_all('td')[0].text.strip()      # find_all returns a list. Access the list. 
    goru_teeth = goru.find_all('td')[1].text.strip()
    goru_ht = goru.find_all('td')[2].text.strip()
    goru_len = goru.find_all('td')[3].text.strip()
    goru_wt = goru.find_all('td')[4].text.strip()
    goru_color = goru.find_all('td')[5].text.strip()
    goru_cat = goru.find_all('td')[6].text.strip()
    goru_subcat = goru.find_all('td')[7].text.strip()
    goru_ori = goru.find_all('td')[8].text.strip()


    print(goru_price)
    time.sleep(2)

    # Fil the CSV file created
    csv_writer.writerow([goru_code, goru_price, goru_age, goru_teeth, goru_ht, goru_len, goru_wt, goru_color, goru_cat, goru_subcat, goru_ori])

# Close the file
csv_file.close()

