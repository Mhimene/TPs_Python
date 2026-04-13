from django.db import models

# Modèle Message (table dans la base)
class Message(models.Model):
    source = models.CharField(max_length=60)  # expéditeur
    to = models.CharField(max_length=60)      # destinataire
    body = models.TextField()                # contenu

    # affichage lisible dans l’admin
    def __str__(self):
        return self.source + " -> " + self.to + " : " + self.body