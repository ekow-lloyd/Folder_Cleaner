import schedule
import time
from datetime import datetime
import os
import shutil, pprint


def job():
    source = '/Users/ekow-lloyd/Downloads'
    apps = '/Users/ekow-lloyd/Downloads/apps'
    pdf = '/Users/ekow-lloyd/Downloads/pdf'
    media = '/Users/ekow-lloyd/Downloads/media'
    ppt = '/Users/ekow-lloyd/Downloads/ppt'
    docs = '/Users/ekow-lloyd/Downloads/docs'
    zips = '/Users/ekow-lloyd/Downloads/docs'
    excel = '/Users/ekow-lloyd/Downloads/excel'
    content = os.listdir(source)

    for files in content:
        if files.endswith('.pdf') or files.endswith('.csv'):
            shutil.move(os.path.join(source, files), os.path.join(pdf, files))
            pprint.pprint(files, pdf + ": " + str(datetime.now()))
            print()
        if files.endswith('.jpeg') or files.endswith('.mp4') or files.endswith('png'):
            shutil.move(os.path.join(source, files), os.path.join(media, files))
            pprint.pprint(files, media + ": " + str(datetime.now()))
            print()
        if files.endswith('.pptx'):
            shutil.move(os.path.join(source, files), os.path.join(ppt, files))
            pprint.pprint(files, ppt + ": " + str(datetime.now()))
            print()
        if files.endswith('.app') or files.endswith('.dmg'):
            shutil.move(os.path.join(source, files), os.path.join(apps, files))
            pprint.pprint(files, apps + ": " + str(datetime.now()))
            print()
        if files.endswith('.docx') or files.endswith('.txt'):
            shutil.move(os.path.join(source, files), os.path.join(docs, files))
            pprint.pprint(files, docs + ": " + str(datetime.now()))
            print()
        if files.endswith('.zip'):
            shutil.move(os.path.join(source, files), os.path.join(zips, files))
            pprint.pprint(files, zips + ": " + str(datetime.now()))
            print()
        if files.endswith('.xlsx'):
            shutil.move(os.path.join(source, files), os.path.join(excel, files))
            pprint.pprint(files, excel + ": " + str(datetime.now()))
            print()
            
    # print("Monitoring")


# Run job every 3 second/minute/hour/day/week,
# Starting 3 second/minute/hour/day/week from now
schedule.every(3).seconds.do(job)
schedule.every(3).minutes.do(job)
schedule.every(3).hours.do(job)
schedule.every(3).days.do(job)
schedule.every(3).weeks.do(job)

while True:
    # run_pending
    schedule.run_pending()
    time.sleep(1)
