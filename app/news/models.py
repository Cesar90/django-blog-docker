from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="verbosenamenewstitle")
    content = models.TextField(blank=True, verbose_name="verbosenamenewscontent")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="createdat")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="verbosenamenewsupdatedat")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name="verbosenamenewsphoto", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="verbosenamenewsispublish")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']