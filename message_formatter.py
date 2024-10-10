from config import (
    OUTLINE_WINDOWS_DOWNLOAD_LINK,
    OUTLINE_MACOS_DOWNLOAD_LINK,
    OUTLINE_LINUX_DOWNLOAD_LINK,
    OUTLINE_CHOMEOS_DOWNLOAD_LINK,
    OUTLINE_IOS_DOWNLOAD_LINK,
    OUTLINE_ANDROID_DOWNLOAD_LINK,
    OUTLINE_ANDROID_APK_DOWNLOAD_LINK,
    servers_description
    )
from aliases import ServerId
from textwrap import dedent


def make_message_for_new_key(access_url: str, server_id: ServerId) -> str:

   message_to_send = dedent(
VPN KEY:
   \n<code>{access_url}</code>
   \nကော်ပီကူးရန် ၎င်းကိုနှိပ်ပါ။
   \nဆာဗာတည်နေရာ: <b>{servers_description.get(server_id)}</b>
   \nဤကီးကို အပလီကေးရှင်းထဲသို့ ထည့်သွင်းရပါမည်။ <b>Outline Client.</b>
   """)
   return message_to_send


def make_download_message() -> str:
    message_to_send = dedent(
    f"""
   <a href="{OUTLINE_WINDOWS_DOWNLOAD_LINK}">Windows အတွက် ဒေါင်းလုဒ်လုပ်ပါ။</a>
   <a href="{OUTLINE_MACOS_DOWNLOAD_LINK}">MacOS အတွက်ဒေါင်းလုဒ်လုပ်ပါ။</a>
   <a href="{OUTLINE_LINUX_DOWNLOAD_LINK}">Linux အတွက် ဒေါင်းလုဒ်လုပ်ပါ။</a>
   <a href="{OUTLINE_CHOMEOS_DOWNLOAD_LINK}">ChromeOS အတွက် ဒေါင်းလုဒ်လုပ်ပါ။</a>
   <a href="{OUTLINE_IOS_DOWNLOAD_LINK}">iOS အတွက် ဒေါင်းလုဒ်လုပ်ပါ။</a>
   <a href="{OUTLINE_ANDROID_DOWNLOAD_LINK}">Android အတွက် ဒေါင်းလုဒ်လုပ်ပါ။</a>
   <a href="{OUTLINE_ANDROID_APK_DOWNLOAD_LINK}">Android အတွက် apk ဖိုင်ကိုဒေါင်းလုဒ်လုပ်ပါ။</a>
    """)
    return message_to_send


def make_help_message() -> str:

    message_to_send = "VPN Key တစ်ခုထုတ်လုပ်ရန် ခလုတ်ကိုနှိပ်ပါ။ "\
            "\n\nအောက်ဖော်ပြပါ command ကိုလည်း သုံးနိုင်သည်။:\n\n"\
            "<code>/newkey server_id key_name</code>\n\n"\
            "<i>server_id</i> - ဒါက ဆာဗာနံပါတ်ပါ။\n"\
            "<i>key_name</i> - ဒါက အဓိက နာမည်ပါ။\n"\
            "ရနိုင်သောဆာဗာများစာရင်းကိုကြည့်ရန် /ဆာဗာများကိုထည့်ပါ။\n"\
            "Command ကိုအသုံးပြုပုံဥပမာ:\n\n"\
            "<code>/newkey 0 </code>\n\n"\


    return message_to_send


def make_servers_list() -> str:

    message_to_send = ""
    for server_id, description in servers_description.items():
        message_to_send += f'server_id: {server_id}, location: {description}\n'
    return message_to_send

