import pandas as pd
import datetime
import smtplib

GMAIL_ID = 'srudoy436@gmail.com'
GMAIL_PASSWORD = 'srudoy2299436'

def sendEmail(to, sub, msg):
    print(f"Email to {to} send with subject {sub} and massagae {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PASSWORD)

    s.sendmail(GMAIL_ID, to, f"Subject: {sub} and massage {msg}")
    s.quit()


if __name__ == '__main__':
    # sendEmail(GMAIL_ID, "Subject", " test Massage")
    # exit()
    df = pd.read_excel("data.xlsx")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    # print(type(today))
    
    writeInd = []

    for index, item in df.iterrows():
        # print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)
        if (today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)

    print(writeInd)
    for i in writeInd:
        yr = df.loc(i, 'Year')
        print(yr)
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)
        # print(df.loc[i, 'Year'])

    print(df)
    df.to_excel('data.xlsx', index=False)