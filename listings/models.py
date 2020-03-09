from django.db import models

# Main model will be for the applicant, containing necessary information
class Applicant(models.Model):
    app_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    applied = models.CharField(max_length=100)
    experience = models.IntegerField(default=0)
    availability = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Applicants can have as many questions as needed associated with them
class Question(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


# We specify a user akin to an admin saving listings on the site
class User(models.Model):
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name


# Save listings associated with the user will be stored as integer values
class Saved(models.Model):
    saved_applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    saved_pk = models.IntegerField(default=0)

    def __str__(self):
        return str(self.saved_pk)


