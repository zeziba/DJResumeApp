from django.db import models


class SocialMedia(models.Model):
    user_name = models.CharField(max_length=60)
    site = models.CharField(max_length=120)

    def __str__(self) -> str:
        return f"{self.user_name}@{self.site}"


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=16)
    self_photo = models.ImageField(
        verbose_name="Personal Picture", upload_to=f"{last_name}/", blank=True)
    social_media = models.ManyToManyField(
        to=SocialMedia, verbose_name="Social Media SItes", blank=True)

    class Meta:
        verbose_name = 'Personal Information'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return f"{self.first_name}|{self.last_name}"


class WorkExperience(models.Model):
    personal = models.ForeignKey(to=PersonalInfo, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(max_length=800)
    title = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Work Experience'
        verbose_name_plural = verbose_name
        ordering = ['-end_date']

    def __str__(self) -> str:
        return f"{self.company_name}"


class Education(models.Model):
    person = models.ForeignKey(to=PersonalInfo, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=120)
    end_date = models.DateField(verbose_name="Graduation Date")
    school_code = models.CharField(
        max_length=6, verbose_name="School's abbreviation")

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
        ordering = ['-end_date']

    def __str__(self) -> str:
        return f"{self.person.last_name}|{self.school_code}"


class Skills(models.Model):
    personal = models.ForeignKey(to=PersonalInfo, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=40)
    description = models.TextField(max_length=120)
    example = models.URLField()

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['-skill_name']

    def __str__(self) -> str:
        return f"{self.skill_name}"


class FiveWs(models.Model):
    # ForeignKey will point to the person it belongs too
    personal = models.ForeignKey(to=PersonalInfo, on_delete=models.CASCADE)
    # We are <identity>
    identity = models.TextField(max_length=400, verbose_name="I am <>")
    # We started <started>
    started = models.DateTimeField(verbose_name="I started <>")
    # We work <location>
    location = models.CharField(max_length=120, verbose_name="I work <>")
    # We strive <purpose>
    purpose = models.TextField(max_length=400, verbose_name="I strive to <>")
    # We believe <how_its_done>
    how_its_done = models.TextField(
        max_length=400, verbose_name="I believe <>")

    class Meta:
        verbose_name = 'The Five W'
        verbose_name_plural = 'The Five Ws'

    def __str__(self) -> str:
        return f"{self.personal.last_name}"


class FactsForFiveWs(models.Model):

    class PriorityLevel(models.IntegerChoices):
        LOW = 0
        MED = 1
        High = 2

    five_ws = models.ForeignKey(
        to=FiveWs, on_delete=models.CASCADE, verbose_name="Five 'w's")
    fact_score = models.IntegerField(
        choices=PriorityLevel.choices, verbose_name="Priority level of factoid")
    factoid = models.TextField(max_length=120, verbose_name="Factoid")

    class Meta:
        verbose_name = 'Factoid'
        verbose_name_plural = 'Factoids'
        ordering = ['fact_score']

    def __str__(self) -> str:
        return f"{self.five_ws.personal.last_name}"
