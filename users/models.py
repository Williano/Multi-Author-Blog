# Standard Library imports
from PIL import Image

# Third Party imports
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
       Creates User profile after registration.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """
            A string representation of the profile model.
        """
        return f"{self.user.username}'s Profile"

    def save(self, **kwargs):
        """
            Overrides the default save method to resize the user profile image.

            Opens the uploaded image path.
            
            It then checks if the image's height and width is greater than 300.
            If it is greater than, it reduces both the height and width to 300. 
        """
        super().save()
        # Opens the path of the uploaded image.
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
