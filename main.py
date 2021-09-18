from twilio.rest import Client
import pandas

client = Client('AC24286c0d33aa8692aba6aec95e068c1d',
                'b56f2b5fb1cfcd661d2d32896b256cd1')

# Read data from excel
excel_data = pandas.read_excel(
    'C:\\Users\\ASUS\\Desktop\\PythonProjects\\WhatsAppSenderTwilio\\Check contacts.xlsx', sheet_name='Customers')

count = 0

# Iterate excel rows till to finish
for column in excel_data['Name'].tolist():
    # Assign customized message
    message = excel_data['Message'][0]

    # Format the message from excel sheet
    message = column + ", " + message
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+972' + str(excel_data['Contact'][count])

    count = count + 1

    message = client.messages.create(body=message,
                                     media_url="https://th.bing.com/th/id/OIP.WtnU9WUh7x3E6z1MbalbnwHaE7?pid=ImgDet&rs=1",
                                     from_=from_whatsapp_number,
                                     to=to_whatsapp_number)

    print(to_whatsapp_number)
    print(message.sid)
