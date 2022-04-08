from django.conf.urls import url,include
from django.contrib import admin
from data.views import home
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/', home.index),
    url(r'^search/', home.search),
    url(r'^stuindex/', home.stuindex),
    url(r'^teaindex/', home.teaindex),
    url(r'^login/', home.login),
    url(r'^logout/', home.logout),
    url(r'^stulogout/', home.stulogout),
    url(r'^tealogout/', home.tealogout),



    url(r'^studentinfolist/', home.studentinfolist),
    url(r'^addstudentinfo/', home.addstudentinfo),
    url(r'^editstudentinfo/(\d+)/', home.editstudentinfo),
    url(r'^delstudentinfo/(\d+)/', home.delstudentinfo),

    url(r'^adminstudentinfolist/', home.adminstudentinfolist),
    url(r'^addadminstudentinfo/', home.addadminstudentinfo),
    url(r'^editadminstudentinfo/(\d+)/', home.editadminstudentinfo),
    url(r'^deladminstudentinfo/(\d+)/', home.deladminstudentinfo),


    url(r'^stupasswdlist/', home.stupasswdlist),
    url(r'^teapasswdlist/', home.teapasswdlist),

    url(r'^teachinfolist/', home.teachinfolist),
    url(r'^addteachinfo/', home.addteachinfo),
    url(r'^editteachinfo/(\d+)/', home.editteachinfo),
    url(r'^delteachinfo/(\d+)/', home.delteachinfo),

    url(r'^adminscoreinfolist/', home.adminscoreinfolist),

    url(r'^studentscoreinfolist/', home.studentscoreinfolist),
    url(r'^studentorderscore/', home.studentorderscore),

    url(r'^studentselectgradelist/', home.studentselectgradelist),
    url(r'^addstudentselectgradelist/', home.addstudentselectgradelist),
    url(r'^editstudentselectgradelist/(\d+)/', home.editstudentselectgradelist),
    url(r'^delstudentselectgradelist/(\d+)/', home.delstudentselectgradelist),

    url(r'^scoreinfolist/', home.scoreinfolist),
    url(r'^addscoreinfo/', home.addscoreinfo),
    url(r'^editscoreinfo/(\d+)/', home.editscoreinfo),
    url(r'^delscoreinfo/(\d+)/', home.delscoreinfo),

    url(r'^teainfolist/', home.teainfolist),
    url(r'^addteainfo/', home.addteainfo),
    url(r'^editteainfo/(\d+)/', home.editteainfo),
    url(r'^delteainfo/(\d+)/', home.delteainfo),

    url(r'^teachgradeinfolist/', home.teachgradeinfolist),
    url(r'^teachkechenginfolist/', home.teachkechenginfolist),
    url(r'^teachzhuanyeinfolist/', home.teachzhuanyeinfolist),

    url(r'^gradeinfolist/', home.gradeinfolist),
    url(r'^addgradeinfo/', home.addgradeinfo),
    url(r'^editgradeinfo/(\d+)/', home.editgradeinfo),
    url(r'^delgradeinfo/(\d+)/', home.delgradeinfo),

    url(r'^batchinfolist/', home.batchinfolist),
    url(r'^addbatchinfo/', home.addbatchinfo),
    url(r'^editbatchinfo/(\d+)/', home.editbatchinfo),
    url(r'^delbatchinfo/(\d+)/', home.delbatchinfo),

    url(r'^adminkechenginfolist/', home.adminkechenginfolist),
    url(r'^editadminkechenginfolist/(\d+)/', home.editadminkechenginfolist),
    url(r'^addadminkechenginfolist/', home.addadminkechenginfolist),
    url(r'^deladminkechenginfolist/(\d+)/', home.deladminkechenginfolist),

    url(r'^adminzhuanyeinfolist/', home.adminzhuanyeinfolist),
    url(r'^addadminzhuanyeinfolist/', home.addadminzhuanyeinfolist),
    url(r'^editadminzhuanyeinfolist/(\d+)/', home.editadminzhuanyeinfolist),
    url(r'^deladminzhuanyeinfolist/(\d+)/', home.deladminzhuanyeinfolist),

]