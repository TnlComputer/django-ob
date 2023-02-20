from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment


def test(request):
    return HttpResponse('Funciona correctamente')


def create(request):
    # comment = Comment(name="Jorge", score=5,
    #                   coment="Este es un comentario")
    # comment.save()
    # comment = Comment.objects.create(name='Alex')
    return HttpResponse("Ruta para agregar comentarios")


def delete(request):
    # comment = Comment.objects.get(id=2)
    # comment.delete()
    Comment.objects.filter(id=1).delete()
    return HttpResponse("Ruta para eliminar comentarios")
