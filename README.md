
# Yield Prediction System

This project is a prototype of a Yield Prediction System developed as a part of a course taught in our school. This prototype is meant to be employed in the Agriculture Sector, specifically targeting farmers. 
This project employs cloud technology to store data, Machine Learning and REST apis on a website to help farmers get the correct crop to grow. We use sensors and Arduino Uno to get real time data that is uploaded to cloud to later improve our ML model to help it give better and more accurate results.


## Authors

- [@megha70265](https://github.com/megha70265)
- [@AneghaJain](https://github.com/AneghaJain)
- [@aana0308](https://github.com/aana0308)
- [Shashank7000](https://github.com/Shashank7000)

## Acknowledgements

 - [Arduino Documentation](https://docs.arduino.cc/hardware/uno-rev3)
 - [Arduino Cloud Blog](https://blog.arduino.cc/2022/10/14/use-your-phone-as-an-iot-device-in-the-arduino-cloud/)
 - [ThingSpeak](https://in.mathworks.com/help/thingspeak/getting-started-with-thingspeak.html)
 - [Streamlit Web App Blog](https://medium.com/@u.praneel.nihar/streamlit-for-building-web-apps-9b8ab6b829fb)


## Packages

The following packages must be installed in your virtual environment for running the Streamlit web app:
- tensorflow
- streamlit
- numpy
- pandas
- pickle
- joblib

The following libraries to be installed in Arduino IDE:
- SoftwareSerial.h
- DHT.h
- SFE_BMP180.h
- Arduino.h


## Tech Stack

**Client:** HTML, CSS

**Server:** Streamlit, ThingSpeak

**ML Model:** RandomForestClassifer


## Deployment

To deploy this project download zip file. 
Make a Thingspeak account and make a channel to deploy this project on cloud. Make the following appropriate fields on the channel:
- field1: Temperature
- field2: Humidity
- field3: Pressure
Warning: ThingSpeak assumes a created_by(timestamp for upload) field.

Open '.ino' file on Arduino IDE. Change Write API key to your own Write API key found on your ThingSpeak channel. To test connected devices run the '.ino' and manually check each device using the option menu. 
Plug model.pickle file into the REST API and in your CLI type the following:

```bash
  python app.py
```
Website will open in active web browser.


## Report

[Access Report](https://drive.google.com/file/d/1F9Y1nY4nf8aHOwjQXIzeL5H8GYLGPEKR/view?usp=sharing)

