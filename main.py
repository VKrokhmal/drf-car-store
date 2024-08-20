#
# class Lesson(models.Model):
#     class Meta:
#         verbose_name = "Lesson"
#
#     name = models.CharField(_("Name of lesson"), max_length=255)
#     teacher = models.ForeignKey(
#         "user.Teacher", on_delete=models.CASCADE, verbose_name=_("Teacher")
#     )
#     price = models.DecimalField(_("Price"), max_digits=5, decimal_places=2)
#     currency = models.CharField(_("Currency of price"), max_length=255)
#     lesson_time = models.PositiveIntegerField()
#
#     def __str__(self):
#         return f"Lesson: {self.name}"
#
#
# class Series(models.Model):
#     class Meta:
#         verbose_name = "Series"
#
#     class DayOfWeeks(models.IntegerChoices):
#         Monday = 1
#         Tuesday = 2
#         Wednesday = 3
#         Thursday = 4
#         Friday = 5
#         Saturday = 6
#         Sunday = 7
#
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
#     student = models.ForeignKey("user.Student", on_delete=models.CASCADE)
#     day_of_week = models.IntegerField(choices=DayOfWeeks)
#     time = models.TimeField()
#     created_datetime = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Series: {self.lesson}"
