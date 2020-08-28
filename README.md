# Alexia

An IOT clock that shows time and covid-19 count (among other things). (Submission for 2020 BotHacks hackathon)

## Functionality

### Displays

#### To be Implemented in the Hackathon

- Time
- Weather
- Covid-19 Count in end user's city
- Temperature sensor which will indicate whether a user is sick
- Buzzer for Notifications *potential*

#### To be Implemented after the Functionality

- Youtube Subscriber Count
- Easy configuration

## Run instructions

1. In the `api-client` directory, create `key.json`
2. In `key.json`, create this object (the value should be your open weather api key):

```json
{
  "openweather": "",
  "city": ""
}
```

3. Run `./run.sh`

## Api Data Sources

### [Weather](https://openweathermap.org/)

### [Covid Data Count? (unconfirmed; still looking)](https://www.programmableweb.com/api/novelcovid-rest-api-v10)

## Hardware 

## [Pictures](/pics)

## ![The Circuit](https://www.arduino.cc/en/uploads/Tutorial/LCD_Base_bb_Fritz.png)
