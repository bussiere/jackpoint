from mp.models import MP


def SendMP(message,sender,receiver):
    mp = MP.objects.create(Texte=message,Sender=sender,Receiver=receiver)
    mp.save()
    