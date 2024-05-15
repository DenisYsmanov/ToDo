from django.shortcuts import render, redirect

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
    if request.method == "POST":
        name = request.POST['title']
        description = request.POST['text']
        todo = Todo.objects.get(id=pk)
        todo.title = name
        todo.text = description
        todo.save()
        return redirect('detail', todo.id)
    return render(request, 'update.html', locals())


def destroy(request, pk):
    if request.method == 'POST':
        todos = Todo.objects.get(id=pk)
        todos.delete()
        return redirect('homepage')
    return render (request, 'destroy.html', locals())


def done_task(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('homepage')


