
# what is the omsender

omsender is a Output Messenger sending. You can send message to anyone person on Blackmagic Fusion. actually, it just has been pulling filename from Loader and Saver where blackmagic fusion and then it sends message with API of that connect

# installation
 1. install [Output Messenger](http://www.outputmessenger.com/lan-messenger-downloads/)
 2. make a API ([Api-Helper](http://support.outputmessenger.com/output-messenger/api-helper/))
 3. of course, you must install Python. ([Python](https://www.python.org/downloads/))
 4. install package `pip install omsender` (but if you have a common harddisk. you should download the omsender and you can put to a harddisk)
 
## configuration

you go to output .py then you should see **IP**, **API_KEY**, **USER**, **TRANSFER**, **COMP_PATHMAP**, **PATH_PATHMAP**, You have to fill blank correcly.

## usage

    from omsender import omsender as om
    om.run()
	