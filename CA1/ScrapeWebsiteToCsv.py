
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA1 - Scrape website graphics cards to CSV.
Description  : This is the main controlling module.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

from TomsHardwareGraphicsCards import TomsHardwareGraphicsCards

def main():
    # Startup method for scraping the list of graphics cards
    # on Tom's Hardware website.
    graphics_cards = TomsHardwareGraphicsCards();
    print('Scraped {0} graphics card details from web page.'
          .format(len(graphics_cards.get_table_rows())))
    file_name = 'GraphicsCards.csv'
    graphics_cards.write_csv(file_name)
    print('The card details have been exported to file {0}.'
          .format(file_name))

main()
