from django.db import models
from django.contrib.auth.models import User

class ThyroidResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.FloatField()
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    on_thyroxine = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    query_on_thyroxine = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    on_antithyroid_medication = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    sick = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    pregnant = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    thyroid_surgery = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    I131_treatment = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    query_hypothyroid = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    query_hyperthyroid = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    lithium = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    goitre = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    tumor = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    hypopituitary = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    psych = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    TSH_measured = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    TSH = models.FloatField()
    T3_measured = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    T3 = models.FloatField()
    TT4_measured = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    TT4 = models.FloatField()
    T4U_measured = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    T4U = models.FloatField()
    FTI_measured = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    FTI = models.FloatField()
    TBG_measured = models.CharField(max_length=1, choices=[('f', 'False'), ('t', 'True')])
    referral_source = models.CharField(max_length=5, choices=[('WEST', 'WEST'), ('STMW', 'STMW'), ('SVHC', 'SVHC'),
                                                              ('SVI', 'SVI'), ('SVHD', 'SVHD'), ('other', 'other')])
    result_value = models.CharField(max_length=20) 
    timestamp = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Thyroid Result for {self.user.username} at {self.timestamp}"
