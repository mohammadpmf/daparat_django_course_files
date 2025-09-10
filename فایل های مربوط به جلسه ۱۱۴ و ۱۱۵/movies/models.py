from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class GenreMovie(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Artist(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    nick_name = models.CharField(max_length=256, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.nick_name != "":
            return self.nick_name
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    STATUS_IN_DEVELOPMENT = "develope"  # 8 characters
    STATUS_PRE_PRODUCTION = "pre"  # 3 characters
    STATUS_FILMING = "filming"  # 7 characters
    STATUS_POST_PRODUCTION = "post"  # 4 characters
    STATUS_RELEASED = "released"  # 8 characters
    # The maximum characters of different STATUS is 8 characters
    STATUS_MOVIES = (
        (STATUS_IN_DEVELOPMENT, "In development"),
        (STATUS_PRE_PRODUCTION, "Pre production"),
        (STATUS_FILMING, "Filming"),
        (STATUS_POST_PRODUCTION, "Post production"),
        (STATUS_RELEASED, "Released"),
    )
    title = models.CharField(max_length=256)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1920), MaxValueValidator(2030)])
    status = models.CharField(max_length=8, choices=STATUS_MOVIES, default=STATUS_RELEASED)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    genre = models.ManyToManyField(to=GenreMovie, blank=True, related_name="movies")
    cast = models.ManyToManyField(to=Artist, blank=True, related_name="movies")

    def __str__(self):
        return f"{self.title} ({self.year})"


class Comment(models.Model):
    user = models.CharField(max_length=255)
    text = models.TextField()
    is_active = models.BooleanField(default=False)
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user}: {self.text[:30]}"
