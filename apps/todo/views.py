from django.shortcuts import render, redirect, get_object_or_404

from apps.todo.models import Todo


def homepage(request):
    todo = Todo.objects.all()
    return render(request,'index.html',locals())


def create(request):
    if request.method == 'POST':
        name = request.POST.get('title')
        text = request.POST.get('description')
        todo = Todo.objects.create(title=name,text=text,)
        return redirect('homepage')
    return render(request,'create.html')


def retrieve(request,pk):
    todo = Todo.objects.get(id=pk)
    return render(request,'detail.html',locals())


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get('title')
        description = request.POST.get('text')
        todo.title = name
        todo.text = description
        todo.save()
        return redirect('detail', pk=pk)
    return render(request, 'update.html', {'todo': todo})


def destroy(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('homepage')
    return render(request, 'destroy.html', locals())


def done_task(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('homepage')


