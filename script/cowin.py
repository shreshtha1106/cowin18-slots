import datetime
import json
import time
import requests
import numpy as np
import simpleaudio as sa


class SolutionByShreshtha:
    # cron
    def cowinCron(self):
        print("\n\nPress Enter/Return for BBMP District or enter District ID:")
        district_id = input()
        if district_id != '' and not district_id.isdigit():
            print("Only numbers allowed!!")
            return None
        while True:
            print("Running Cron......")
            self.cowin18(district_id)
            time.sleep(30)

    # main functionality
    def cowin18(self, district_id: str):

        headers = {
            'authority': 'cdn-api.co-vin.in',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'accept': 'application/json, text/plain, */*',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'origin': 'https://www.cowin.gov.in',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.cowin.gov.in/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'if-none-match': 'W/"10a5d-Wi8W1DxxXxTcbAlc8tqyokJV5y0"',
        }
        date = datetime.date.today()
        # each date from today till 10 days
        for i in range(10):
            currDate = date + datetime.timedelta(days=i)
            currDateStr = currDate.strftime("%d-%m-%Y")
            if district_id == '' or int(district_id) <= 0:
                district_id = '294'  # for BBMP District
            params = (
                ('district_id', district_id),
                ('date', currDateStr),
            )
            response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict',
                                    headers=headers, params=params)
            if response is not None and response.ok == True:
                for centerData in response.json()['centers']:
                    for session in centerData['sessions']:
                        if session['min_age_limit'] == 18 and session['available_capacity'] > 0:
                            self.sound(300, 1)
                            print("Available Slots:  " + str(session['available_capacity']))
                            print("Date: " + str(session['date']))
                            print("Pincode:  " + str(centerData['pincode']))
                            print("Center Data")
                            print(json.dumps(centerData))
                            print("###################################################")

    def sound(self, x, z):
        frequency = x
        fs = 44100  # 44100 samples per second
        seconds = z

        # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
        t = np.linspace(0, seconds, seconds * fs, False)

        # Generate a 440 Hz sine wave
        note = np.sin(frequency * t * 2 * np.pi)

        # Ensure that highest value is in 16-bit range
        audio = note * (2 ** 15 - 1) / np.max(np.abs(note))
        # Convert to 16-bit data
        audio = audio.astype(np.int16)

        # Start playback
        play_obj = sa.play_buffer(audio, 1, 2, fs)

        # Wait for playback to finish before exiting
        play_obj.wait_done()


s = SolutionByShreshtha()
s.cowinCron()
