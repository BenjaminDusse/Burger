from django.db import models
from django.db.models import QuerySet

class BaseQuerySet(models.QuerySet):
    
    def delete(self):
        self.update(is_delete=True)
        
class DeleteManager(models.QuerySet):
    def get_queryset(self):
        return BaseQuerySet(self.model).filter(is_delete=False)