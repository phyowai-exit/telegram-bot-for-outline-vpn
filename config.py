import os


#Outline api servers settings
OUTLINE_API_URL_0 = os.getenv('https://5.78.95.223:5125/j5NPhn_PAEhUZGUIXgyO0g')

servers ={                          # {'server_id':'api_url'}
        '18b77702-b2fe-40e4-ba45-b11a9fb95035': OUTLINE_API_URL_0
        }


servers_description = {             # {'server_id' : 'description'}
        '18b77702-b2fe-40e4-ba45-b11a9fb95035': 'SkyLinkOutLineServer'
        }


#Main bot settings
BOT_API_TOKEN = os.getenv("7406367010:AAERVBptWKL1moUy8G81H4k0i8mO0ZQ54sI")
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
MONITOR_API_TOKEN = os.getenv("7406367010:AAERVBptWKL1moUy8G81H4k0i8mO0ZQ54sI")
ADMIN_CHAT_ID = os.getenv("7492564460")


BLOCKED_CHAT_IDS = [ 

        ]


