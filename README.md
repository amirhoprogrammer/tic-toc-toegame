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
وقتی روی این گزینه کلیک کنیم. بازی به حالت بازی با کامپیوتر اجرا می شود که در ادامه اینکه کامپیونر چگونه با ما بازی می کند عرض خواهم کرد 
### Two_player
وقتی روی این گزینه کلیک کنیم. بازی به حالت بازی دو نفره اجرا می شود یعنی شما با دوست خودت یا رقیبت می تونی بازی کنی.
### Start_game 
از دیگر اجزا آن می توان به Start_game اشاره کرد وقتی روی گزینه های "Vs Computer" یا "Two player" کلیک می کنیم این صفحه به صفحه بازی انتقال پیدا می کند که به وسیله متد Start_game این اتفاق می افتد
### on_click
و آخرین جزء آن On_click است که پس از پایان یک messagebox منتشر می شود که در آن برنده بازی و نتیجه مشخص می شود


