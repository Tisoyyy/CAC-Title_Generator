import datetime

loop = 1
date = datetime.datetime.now()
sundate = date.strftime("%B %d, %Y")
description = "For your giving, you may send it to our church bank account: Security Bank City Alliance Church 0231-022229-001 " \
              "\nAll music used is for church purposes only. No copyright infringement intended. All rights reserved to its rightful owners."

print("\tCAC Title Generator v1.0\nTo start, enter the necessary information below.\n*IF SPEAKER IS PTR. NANO, YOU CAN LEAVE THE SPEAKER FIELD BLANK*")
print("\nType 1 for Ptr. Nano\nType 2 for Ptr. Roanne\nType 3 for Ptr. Mobida\nFor other speakers, type the full name of the Speaker"
      "\nPress 2 to change Title/Description") #Title and description under development

while (loop == 1):
    speaker = input("\nSpeaker: ")
    if speaker == "":
        speaker = "Rev. Lorenzo Nano Jr."
    elif speaker == "1":
        speaker = "Rev. Lorenzo Nano Jr."
    elif speaker == "2":
        speaker = "Ptr. Roanne Vergara"
    elif speaker == "3":
        speaker = "Ptr. Jun Mobida"
    elif (speaker == 'exit'):
        break
    sermon_title = input("Sermon Title: ")

    print("Title:")
    print(f"CAC CDO Sunday Online Worship  | {sundate} | {sermon_title} | Speaker: {speaker}")
    print(description)
