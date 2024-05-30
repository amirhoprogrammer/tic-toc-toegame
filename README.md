# tic-toc-toegame 
این پروژه 'tic-toc-toe' است. ما سعی کردیم بازی دوز یا 'tic-toc-toe' را با فریمورک 'tkinter' بنویسیم. این فریمورک برای زبان پایتون هست و با آن اکثر بازی ها یا پروژه های گرافیکی رو می نویسند. این بازی که ما نوشتیم دارای طراحی و ویژگی های خاصی هست در ادامه عرض خواهم کرد.
## تصویری از بازی
![tic-toc-toegame](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/unnamed.png).
## قواعد بازی
این بازی دو نفره و دارای جدولی 3x3 است که بازیکنان با "O" یا "X" بازی می کنن. در این بازی یک نفر به عنوان شروع کننده به قید قرعه بازی را شروع می کند یک خانه از جدول با "X" پر می کند بعد نوبت نفر بعدی است. هدف از پر کردن این است که یک سطر یا یک ستون یا یک قطر شامل "X" یا "O" باشد بازیکنی که بتواند یک سطر یا یک ستون یا یک قطر را پر کند برنده بازی است.
## اجزای اصلی بازی
وقتی بازی را اجرا می کنیم یک منوی دو گزینه ای می آید که بازیکن مشخص می کند که آیا با بازیکن دیگری به صورت دو نفره بازی می کند یا با کامپیوتر بازی می کند که منظور از "choose mode" انتخاب وضعیت است و گزینه های آن یکی          "Two Player" و "Vs Computer" است که به ترتیب به معنای بازی دونفره و بازی با کامپیوتر است. 

![choosemode](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/choosemode.png).
### Vs_computer
وقتی روی این گزینه کلیک کنیم. بازی به حالت بازی با کامپیوتر اجرا می شود که در ادامه اینکه کامپیونر چگونه با ما بازی می کند عرض خواهم کرد .
### Two_player
وقتی روی این گزینه کلیک کنیم. بازی به حالت بازی دو نفره اجرا می شود یعنی شما با دوست خودت یا رقیبت می تونی بازی کنی.
### Start_game 
از دیگر اجزا آن می توان به Start_game اشاره کرد وقتی روی گزینه های "Vs Computer" یا "Two player" کلیک می کنیم این صفحه به صفحه بازی انتقال پیدا می کند که به وسیله متد Start_game این اتفاق می افتد.

![boardgame](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/boardgame.png).
### on_click
و آخرین جزء آن On_click است که پس از پایان یک messagebox منتشر می شود که در آن برنده بازی و نتیجه مشخص می شود.
## winnig
حالت های پایانی مسابقه به شرح زیر است:
### Player-one win
بازیکن شماره یک با "X" شروع می کند برنده می شود.

![playerO](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/player%20O.png).
### Player-two win
بازیکن شماره دو با "o" شروع می کند برنده می شود.

![playerX](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/player%20X.png).
### computer win
کامپیوتر برنده بازی میشود.
### draw
هیچ کس برنده نمی شود.

![draw](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/draw.png).
## کد بازی
![code bazi](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-25%2017-58-28-997.jpg).
![code bazi](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-25%2018-00-04-322.jpg).
![code bazi](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-25%2018-01-18-294.jpg).
![code bazi](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-25%2018-01-49-882.jpg).
![code bazi](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-25%2018-02-38-863.jpg).
![code bazi](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-25%2018-03-09-910.jpg).
## معماری بازی
معماری این کد به گونه‌ای طراحی شده است که به راحتی قابل فهم و نگهداری باشد. این کد یک بازی ساده "Tic-Tac-Toe" (دوز) را با استفاده از کتابخانه tkinter پیاده‌سازی می‌کند. در اینجا معماری و اجزای کلیدی این کد توضیح داده شده است:

### 1. ساختار کلی
کد به چند بخش اصلی تقسیم شده است:
- کلاس TicTocToe: شامل منطق اصلی بازی و رابط کاربری.
- توابع start_game و choose_mode: برای شروع بازی و انتخاب حالت بازی.
- بلوک اصلی: برای اجرای برنامه.

### 2. کلاس TicTocToe
این کلاس مسئولیت‌های زیر را بر عهده دارد:
- ساخت و پیکربندی پنجره اصلی بازی: در سازنده کلاس (init).
- مدیریت حالت بازی: نگهداری نوبت بازیکن جاری، ذخیره وضعیت بورد، و به‌روزرسانی امتیازات.
- رابط کاربری: ایجاد و به‌روزرسانی دکمه‌ها و برچسب‌ها.
- منطق بازی: بررسی برد و باخت، حرکات کامپیوتر و بازنشانی بازی.

### 3. متدها و مسئولیت‌ها
#### init
- ورودی‌ها: ریشه (root) و حالت (mode) بازی.
- عملکردها: تنظیم پنجره، ایجاد برچسب‌های امتیاز، دکمه‌های بورد و تنظیم بازیکن جاری.

#### on_click
- ورودی‌ها: اندیس دکمه کلیک شده.
- عملکردها: بررسی و به‌روزرسانی وضعیت بورد، تغییر بازیکن جاری و بررسی برنده شدن.

#### check_winner
- عملکردها: بررسی الگوهای برد و تعیین برنده.

#### reset_game
- عملکردها: بازنشانی بورد و رابط کاربری.

#### update_score_labels
- عملکردها: به‌روزرسانی برچسب‌های امتیاز با امتیازات جدید.

#### computer_move
- عملکردها: تعیین حرکت کامپیوتر با بررسی حرکات برنده یا بلوکه کردن حریف و انتخاب یک خانه خالی به صورت تصادفی.

### 4. توابع شروع بازی و انتخاب حالت
#### start_game
- ورودی‌ها: حالت بازی.
- عملکردها: ایجاد و شروع پنجره اصلی بازی با حالت انتخاب شده.

#### choose_mode
- عملکردها: نمایش پنجره انتخاب حالت بازی و هدایت به تابع start_game.

### 5. بلوک اصلی
این بخش کد را در حالت مستقل اجرا می‌کند و با فراخوانی تابع choose_mode بازی را شروع می‌کند.

### نتیجه‌گیری
این معماری با استفاده از اصول ساده و ماژولار بودن کد، پیاده‌سازی شده است. هر بخش از کد دارای مسئولیت مشخصی است که به خوانایی و نگهداری آسان کد کمک می‌کند. استفاده از کلاس‌ها و توابع مجزا برای منطق بازی و رابط کاربری باعث شده تا تغییرات و به‌روزرسانی‌ها به راحتی اعمال شوند.

![architecture code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-05-28%2023-19-40-505.jpg).
## توضیح کد
### library
1. import tkinter as tk
   برای اینکه از ماژول و امکانات tkinter در پروژه مان استفاده کنیم آن library را import می کنیم.
2. import random
   برای اینکه بتونیم از توابع random در تعیین حرکات کامپیوتر استفاده کنیم.آن library را import میکنیم.
3. from tkinter import messagebox
   برای اینکه بتونیم messagebox در پروژه درست کنیم باید آن را از tkinter import کنیم.
![explain code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-26%2011-22-17-644.jpg).
###  run_the_game
موقعی برنامه ران می کنیم مقدار این متغیر برابر "__main__" می شود دستور داخل این شرط یعنی صدا زدن تابع ()choose_mode اجرا می شود.
![explain code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-26%2012-46-02-516.jpg).
###  start_game
زمانی کاربر یکی از دکمه برای بازی که در آن مشخص می شود بازیکن آیا با دوستش بازی می کند یا با کامپیوتر؟ ولی در بررسی دقیق این تابع می توان گفت ورودی تابع یعنی "mode" مشخص می کند کاربر کدام دکمه را زده و میاد از tkinter یک window می سازد و برای نمایش حتما متد mainloop را در آخر صدا زده بعد ساختن window کلاس TicTacToe را صدا زده است.
![explain code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-26%2012-46-35-483.jpg).
###  choose_mode

همانطور که می دانید این موقع ران کردن برنامه اجرا می شود. در این تابع ما صفحه اول بازی را می سازیم. ابتدا یک window از tkinter می سازیم و سپس متد mainloop را برای نمایش آن در انتها صدا می زنیم بعد ساختن این window برای آن title و رنگ پس زمینه انتخاب می کنیم بعد دو متد start_two_computer , start_vs_computer را می نویسم که ساز و کار هردو شبیه هم هستند. در واقع این پنجره صفحه پس از زدن دکمه یا صفحه بازی می شود بدین شکل پنجره صفحه حال حاضر را می بندد.تابع start_game را با mode مخصوص خود یعنی برای vs_computer(computer) , startcomputer(two_player) است را صدا می زنیم. در نهایت با تعریف label و button آن را تکمیل می کنیم با استفاده از متد grid آن را به window اضافه می کنیم علت استفاده از grid برای این است ما می توانیم محل قرار گیری آن ها را در سطر و ستون های خاصی قرار دهیم و فاصله بین ها را هم کنترل کنیم.
![explain code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-26%2012-38-02-822.jpg).
###  class TicTacToe
این کلاس برای ساخت صفحه ای پس از زدن دکمه نوع بازی و تعیین امتیازات و تعیین حرکات کامپیوتر و... هست. این کلاس حجم کد را کاهش و درک و فهم کد راحت تر کرده و نکته آخر این است این کلاس دارای متدهای on_click,__init,check_winner,update_score,computer_move است.
![explain code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-27%2011-58-17-701.jpg).
###  __init__
اولین متدی از کلاس که راجبش صحبت می کنیم متد سازنده این کلاس هست که داری دو ورودی mode , root هست که mode برای این است کاربر آیا با کامپیوتر بازی می کند یا با کاربر دیگری بازی می کند و root برای ساخت صفحه بازی پس از انتخاب mode هست. در ادامه رنگ بک گراند و تیتر آنرا مشخص می کنیم بعد یه سری متغیر به اسم های current_player(برای تعیین این که در حال حاضر نوبت کیست),player_scores(امتیازاتی که بازیکنان بدست می آورند)وboard(برای ساختن صفحه بازی) وجود دارد.بعد برای ساخت این صفحه از دو حلقه for استفاده یکی برای ساخت هدر که امتیازات را به نشان می دهد و دومی برای درست کردن صفحه بازی وانجام آن است. و در آخر از یک شرط برای زمانی که با کامپیوتر بازی می کردیم مشخص کی کامپیوتر حرکت خودش را انجام دهد.
![explain code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-27%2012-12-26-168.jpg).
###  on_click
![explain code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-27%2012-15-27-288.jpg).
###  check_winner
![explain code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-27%2012-27-21-640.jpg).
###  reset_game
![explain code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-27%2012-33-05-227.jpg).
###  update_score_labels
![explain code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-27%2012-36-26-531.jpg).
###  computer_move
![explain code](https://github.com/amirhoprogrammer/tic-toc-toegame/blob/main/%D9%BE%D8%B1%D9%88%DA%98%D9%87%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C/bandicam%202024-03-27%2013-10-10-465.jpg).




