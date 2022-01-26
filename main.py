from datetime import datetime
import os, sys
import shutil, pprint
import smtplib

this_day = (datetime.today().strftime('%b %d'))   # defined the date, in order to add it to the naming of my log file
file_path  = "LogFile - " + this_day              # the name of the file to be created
sys.stdout = open(file_path, "w")                 # writing all the output to a file


# this function sends me an email to inform me of what the cronjob i scheduled has done
def log_mail():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login("my_email@gmail.com","password")
    smtpObj.sendmail("my_email@gmail.com", "recipient_email@gmail.com", "Subject:Folder Cleaned!! \nHi Ekow,\n\nNew log available of moved files.\n\nKind Regards\nPythonBlac")
    smtpObj.quit()

# defining the sources and destinations of the files to be processed and after processing
source = '/Users/ekow-lloyd/Downloads'
apps = '/Users/ekow-lloyd/Downloads/apps'
pdf = '/Users/ekow-lloyd/Downloads/pdf'
media = '/Users/ekow-lloyd/Downloads/media'
ppt = '/Users/ekow-lloyd/Downloads/ppt'
docs = '/Users/ekow-lloyd/Downloads/docs'
zips = '/Users/ekow-lloyd/Downloads/docs'
excel = '/Users/ekow-lloyd/Downloads/excel'
pyfiles = '/Users/ekow-lloyd/Downloads/pyfiles'
content = os.listdir(source)
des_log = '/Users/ekow-lloyd/Dev/VSCode/Python/Logs'

# what to do with the various file types
for files in content:
    if files.endswith('.pdf') or files.endswith('.csv') or files.endswith(".PDF") or files.endswith(".ics"):
        shutil.move(os.path.join(source, files), os.path.join(pdf, files))
        pprint.pprint(files + " moved to " + pdf + ": " + str(datetime.now()))
        print()
    if files.endswith('.jpeg') or files.endswith('.mp4') or files.endswith('png') or files.endswith("jpg"):
        shutil.move(os.path.join(source, files), os.path.join(media, files))
        pprint.pprint(files + " moved to : " + media + ": " + str(datetime.now()))
        print()
    if files.endswith('.pptx')or files.endswith('.ppt'):
        shutil.move(os.path.join(source, files), os.path.join(ppt, files))
        pprint.pprint(files + " moved to : " + ppt + ": " + str(datetime.now()))
        print()
    if files.endswith('.app') or files.endswith('.dmg') or files.endswith(".pkg")or files.endswith('.whl') or files.endswith('.iso') or files.endswith("exe"):
        shutil.move(os.path.join(source, files), os.path.join(apps, files))
        pprint.pprint(files + " moved to : " + apps + ": " + str(datetime.now()))
        print()
    if files.endswith('.docx') or files.endswith('.txt')or files.endswith('.doc'):
        shutil.move(os.path.join(source, files), os.path.join(docs, files))
        pprint.pprint(files + " moved to : " + docs + ": " + str(datetime.now()))
        print()
    if files.endswith('.zip'):
        shutil.move(os.path.join(source, files), os.path.join(zips, files))
        pprint.pprint(files + " moved to : " + zips + ": " + str(datetime.now()))
        print()
    if files.endswith('.xlsx'):
        shutil.move(os.path.join(source, files), os.path.join(excel, files))
        pprint.pprint(files + " moved to : " + excel + ": " + str(datetime.now()))
        print()
    if files.endswith('.py'):
        shutil.move(os.path.join(source, files), os.path.join(pyfiles, files))
        pprint.pprint(files + " moved to : " + pyfiles + ": " + str(datetime.now()))
        print()

# After all the files have been sorted, move them to a folder where i store all such logs
shutil.move(file_path,des_log)

# calling the mail function to remind me via mail
log_mail()




