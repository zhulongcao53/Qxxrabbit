#-*- encoding: utf-8 -*-
from django.db import models  
from django.contrib import admin  
from DjangoUeditor.models import UEditorField
  
# Create your models here.  
class BlogPost(models.Model):  
    title = models.CharField(u'标题',max_length=150)  
    body = UEditorField(u'内容',height=300, width=1000, default=u'', blank=True, imagePath="uploads/images/", toolbars='besttome', filePath='uploads/files/')
    category = models.CharField(u'标签',max_length = 50, blank = True)
    timestamp = models.DateTimeField(u'时间')  

    class Meta:
        ordering =('-timestamp',)   #以最新时间显示

    def __unicode__(self):
        return u'%s %s' % (self.title, self.timestamp)
 
class BlogPostAdmin(admin.ModelAdmin):  
    list_display = ( 'title', 'body', 'category', 'timestamp')  #后台blog栏目显示内容
    list_filter = ('timestamp',)        # 过滤器
    search_fields = ('title', 'body', 'category') #快速查询栏
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)


admin.site.register(BlogPost, BlogPostAdmin)  
