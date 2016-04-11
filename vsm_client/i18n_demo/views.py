# _*_ coding: utf-8 _*_
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext, pgettext
from django.utils.translation import get_language_info
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #/django/conf/locale
    #li = get_language_info("en")
    li = get_language_info("ca")
    print li["name"]
    print li["name_local"]
    print li["bidi"]

    # Translators: the example for the translator comments
    output1 = _("Welcome to my site.")

    words = ['Welcome', 'to', 'my', 'site.']
    output2 = _(' '.join(words))

    output3 = _('Today is %(month)s %(day)s.') % {'month': "April", 'day': "11"}

    # 使用 django.utils.translation.gettext_noop() 函数来标记一个不需要立即翻译的字符串。

    # ngettext 函数包括三个参数：
    # 单数形式的翻译字符串，复数形式的翻译字符串，和对象的个数（将以 count 变量传递给需要翻译的语言）。
    count = 1
    pluralization = ungettext(
        'there is %(count)d object',
        'there are %(count)d objects',
    count) % {
        'count': count,
    }

    # 根据上下文来选择
    May = pgettext("month name", "May")

    #the name list of info0811
    # info0811 = _(["Xu Shou","Lou Zhigang"])
    info0811 = [_("Xu Shouan"),_("Lou Zhigang")]

    #student object
    student = {"name":_("Xu Shouan"), "age":28, "gender":_("male")}
 
    info0821 = [_("LLLLLLLLLLLLLL"),_("XXXXXXXXXXXXXXXXXXX")]
 
    # lazy的编写方式与普通的翻译方式相似，只是在访问时才被翻译
    return render(request, 'i18n_demo/index.html',{
        "output1": output1,
        "output2": output2,
        "output3": output3,
        "pluralization": pluralization,
        "May": May,
        "info0811":info0811,
        "student":student,
        })
