# cowin18-slots

You can run this to get notification when slots show up for 18+ Age on the Cowin website. 
The code is closer to the system and sends an alert on the system itself intead of relaying it to mobile phones so its a bit faster than phone notifications. 
The system needs to be on all that time when code is required to run and send alerts. 

Steps to run in console:
1. git clone git@github.com:shreshtha1106/cowin18-slots.git
2. python3 PATH/cowin18-slots/script/cowin.py
PATH is the path to the pulled cowin18-slots directories
3. Enter district id if the district is not BBMP in Bangalore. How to fetch district id => 1. https://media.giphy.com/media/fKc75qEjcIBiBLem8D/giphy.gif
                                                                                           2. https://gph.is/g/460bnAx

To Run this you will need the following installed in your system:

-> python3
-> simpleaudio (run "pip3 install simpleaudio" on terminal/console)
-> numpy (run "pip3 install numpy" on terminal/console)
-> requests (run "pip3 install requests" on terminal/console)

PS: This is a small personal project and my first on python so please feel free to drop review comments. 
    Have tried to keep this code as procudural as possible to save some runtime as running it fast is the key.
