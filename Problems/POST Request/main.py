from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        task = request.POST.get('todo')  # request.todo
        if task not in self.all_todos:
            self.all_todos.append(task)
        return redirect('/')
