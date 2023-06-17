from django.db import models
# from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Artist(models.Model):
    artistName = models.CharField(("Artist Name"), max_length=255)
    created = models.DateTimeField(("Artists created date"),auto_now_add=True)
    last_updated = models.DateTimeField(("Latest Artists update"),auto_now_add=True)
    def __str__(self):
        return self.artistName
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, verbose_name=("Artist Album"),on_delete=models.CASCADE)
    albumName = models.CharField(("Album Name"),max_length=255)
    created = models.DateTimeField(("Album created date"),auto_now_add=True)
    last_updated = models.DateTimeField(("Latest Album update"),auto_now_add=True)
    def __str__(self):
        return self.albumName
    
class Song(models.Model): 
    album = models.ForeignKey(Album,verbose_name=("Song Album"),on_delete=models.CASCADE)
    songThumbnail = models.ImageField(("Song Thumbnail"),upload_to='thumbnail/',help_text=".jpg, .png,.jpeg , .svg supported")
    song = models.FileField(("song"),upload_to="songs/", help_text=".mp3 supported only")
    songname = models.CharField(("Song Name"),max_length=255)
    created = models.DateTimeField(("Song created date"),auto_now_add=True)
    last_updated = models.DateTimeField(("Latest Song update"),auto_now_add=True)
    
    
    
