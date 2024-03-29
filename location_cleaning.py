# -*- coding: utf-8 -*-
"""Location cleaning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GaTpr7JhJXxaSEjVG8lHbAEQ9Oyvh829
"""

from google.colab import files

uploaded = files.upload()

import pandas as pd

df = pd.read_csv('df.csv')

df

df['Location'].value_counts() #دوستان ما اینجا یه مسئله داریم اونم اینکه من میخوام چیزی که مشاهده میکنم از لوکیشنها استانی باشه نه شهر به شهر
#من میخوام به داستانم دید استانی داشته باشم نه شهری مثل اینکه برای من مهم نیست که در شهرهای یک استان چه دیتایی هست چون مهم اینکه در کل استان با همه شهرهاش چه دیتایی وجود داره

df['Location'][0]   #تو خونه اولم شهر نیویورک و استان نیویورک رو نشون میده

df['Location'][0].split()[2]  #با این دستور من استان رو فقط فراخوانی میکنم که اندیکس ۲ است
#نکته مهم اینکه در هر سلول من نمیدونم که در اندیس ۲ ام دقیقا استان نوشته شده اما میدونم استان اخرین یا به اصطلاح راسترین خونه منه از لحاظظ نوشتار پسسس.....برو  دستور پایین

df['Location'][0].split()[-1] #تو این دستور من از راست اولین گزینه رو فراخوانی میکنم و میزنه -۱

df['Location'][2000].split()[-1] #من برای نمونه مثلا ریف ۲۰۰۰ رو هم فراخوانی کردم که تگزاز رو نشون داد و خوندش... پس دستور من درست کار میکنه

def state(a):   #حالا میام یه تابع مینویسم براش
  a= a.split()  #که بیا تو ستون ایالت هر سلول رو راست یعنی ایندکس -۱ بخون یا بنابر دستور جداش کن تا ما فقظ ایالتها رو یعنی استانها رو ببینیم
  a = a[-1]
  return(a)

df['State'] = df['Location'].apply(state)  #میگم با توجه به تابعی که تعریف کردم اینجا میام تابعم رو ص=دا میزنم و میگم رو کل ستون اعمالش کن
  #توجه کنید که که تمام دستور العملها رو برابر ستون استیت قرار میدم چون میخوام بمونه روی دیتاهام و تغییرات اعمال بشه کامل وسیو شه

df['State']  # یه خروجی میگیرم

df['State'].value_counts() #حالا با توجه به این دستور فراپانی و حجم و تجمع در ستون استیت رو میفهمم و دارم اینجا علنا داستان رو ایالتی میبینم
#یعنی کالیفرنیا بیشترین میزان شغل رو داشته

df['State'].info() #اینجا یه اینفو گرفتم که صرفا بعد از حذف کینگدوم متوجه کاهش سطرها یا به اصطلاح حذف دیتاهای بیخود بشم

df = df[df['State'] != 'Kingdom']  #توجه کنید در خروجی بالا ما یک ما یک عبارت کینگدوم رو میبینم که دیتای انگلستان است و به اشتباه داخل این دیتاها افتاده و من باید حذفش کنم
#من نمیدونم چندتا از این عبارت هست داخل این دیتا
#پس میام دستوری مینویسم که هرچی داخل دیتا این عبارت رو میبینی حذفش کن یعنی ستون استیت من برابر نباشه با هیچ گونه کینگدومی

df['State'].value_counts()  #یه حجم دیگه از از دیتاهامون میگیریم و میبینیم که کینگدوم حذف شد

df['State'].info()  #میبینی در اینفو جدید ۵۸۸۸ و در اینفو قدیم ۵۸۹۲ دیتا در ستون استیت داشتیم و نشانگر کلین شدن ستون است

df.info() #میبینید اینفو کلی هم همینو نشون میده