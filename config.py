import os


#Outline api servers settings
OUTLINE_API_URL_0 = os.getenv('https://54.251.27.188:19364/hVwbqd0arSo9ydGbgCz2WA')

servers ={                          # {'server_id':'api_url'}
        '0': OUTLINE_API_URL_0
        }


servers_description = {             # {'server_id' : 'description'}
        '0': 'Us-Server'
        }


#Main bot settings
BOT_API_TOKEN = os.getenv("7667240966:AAGEsq93yPqO5LBusP4pejef-FJdilsSHu8")
DEFAULT_SERVER_ID = "0"


#Message formatter settings
OUTLINE_WINDOWS_DOWNLOAD_LINK = "https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe"
OUTLINE_MACOS_DOWNLOAD_LINK = "https://itunes.apple.com/us/app/outline-app/id1356178125"
OUTLINE_LINUX_DOWNLOAD_LINK = "https://s3.amazonaws.com/outline-releases/client/linux/stable/Outline-Client.AppImage"
OUTLINE_CHOMEOS_DOWNLOAD_LINK = "https://play.google.com/store/apps/details?id=org.outline.android.client"
OUTLINE_IOS_DOWNLOAD_LINK = "https://itunes.apple.com/us/app/outline-app/id1356177741"
OUTLINE_ANDROID_DOWNLOAD_LINK = "https://play.google.com/store/apps/details?id=org.outline.android.client"
OUTLINE_ANDROID_APK_DOWNLOAD_LINK = "https://s3.amazonaws.com/outline-releases/client/android/stable/Outline-Client.apk"


#Monitoring bot settings
MONITOR_API_TOKEN = os.getenv("7667240966:AAGEsq93yPqO5LBusP4pejef-FJdilsSHu8")
ADMIN_CHAT_ID = os.getenv("7492564460")


BLOCKED_CHAT_IDS = [ 

        ]


